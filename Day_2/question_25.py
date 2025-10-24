"""
### Q25

**Question:** Implement a FastAPI endpoint with WebSocket support that streams real-time analysis results as they're computed, with proper error handling and connection management.

**Input:** WebSocket connection with initial parameters

**Expected Output:** Streaming JSON messages with incremental results and progress updates

**Usage:** Real-time bioinformatics pipeline monitoring and interactive data analysis dashboards.
"""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import Dict
import asyncio
import json
import numpy as np

app = FastAPI()

class ConnectionManager:
    """Manage WebSocket connections"""
    
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}
    
    async def connect(self, websocket: WebSocket, client_id: str):
        await websocket.accept()
        self.active_connections[client_id] = websocket
    
    def disconnect(self, client_id: str):
        if client_id in self.active_connections:
            del self.active_connections[client_id]
    
    async def send_message(self, client_id: str, message: dict):
        if client_id in self.active_connections:
            await self.active_connections[client_id].send_json(message)

manager = ConnectionManager()

async def analyze_sequence(sequence: str, websocket: WebSocket, client_id: str):
    """Simulate streaming analysis with progress updates"""
    try:
        total_steps = 10
        
        for step in range(1, total_steps + 1):
            # Simulate computation
            await asyncio.sleep(0.5)
            
            # Send progress update
            await manager.send_message(client_id, {
                "type": "progress",
                "step": step,
                "total_steps": total_steps,
                "message": f"Processing step {step}/{total_steps}",
                "percentage": (step / total_steps) * 100
            })
            
            # Simulate intermediate results
            if step % 3 == 0:
                await manager.send_message(client_id, {
                    "type": "intermediate_result",
                    "data": {
                        "gc_content": np.random.rand() * 100,
                        "length": len(sequence)
                    }
                })
        
        # Send final result
        await manager.send_message(client_id, {
            "type": "complete",
            "result": {
                "sequence": sequence,
                "gc_content": 45.6,
                "molecular_weight": len(sequence) * 100,
                "status": "success"
            }
        })
        
    except Exception as e:
        await manager.send_message(client_id, {
            "type": "error",
            "message": str(e)
        })

@app.websocket("/ws/analyze/{client_id}")
async def websocket_analysis(websocket: WebSocket, client_id: str):
    """WebSocket endpoint for real-time sequence analysis"""
    await manager.connect(websocket, client_id)
    
    try:
        while True:
            # Receive analysis parameters
            data = await websocket.receive_json()
            
            if data.get("action") == "analyze":
                sequence = data.get("sequence", "")
                
                if not sequence:
                    await manager.send_message(client_id, {
                        "type": "error",
                        "message": "No sequence provided"
                    })
                    continue
                
                # Start analysis
                await analyze_sequence(sequence, websocket, client_id)
            
            elif data.get("action") == "cancel":
                await manager.send_message(client_id, {
                    "type": "cancelled",
                    "message": "Analysis cancelled"
                })
                break
                
    except WebSocketDisconnect:
        manager.disconnect(client_id)
        print(f"Client {client_id} disconnected")
    except Exception as e:
        await manager.send_message(client_id, {
            "type": "error",
            "message": f"Unexpected error: {str(e)}"
        })
        manager.disconnect(client_id)

# Run with: uvicorn app:app --reload
# Connect with JavaScript: const ws = new WebSocket("ws://localhost:8000/ws/analyze/user123");
