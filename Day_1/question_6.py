"""
**Q6 - Batch Request Processor**
Question: Create a class `BatchProcessor` that groups API requests into batches of size N and tracks processing status (pending/completed/failed).
Input: `requests=[req1, req2, req3, req4, req5]`, `batch_size=2`
Expected Output: `[[req1, req2], [req3, req4], [req5]]` with status tracking
Usage: Optimizing throughput in LLM API calls and rate-limited services
"""

class BatchProcessor:
    """Processes requests in batches with status tracking"""
    
    def __init__(self, batch_size):
        self.batch_size = batch_size
        self.batches = []
        self.status = {}
    
    def create_batches(self, requests):
        """Groups requests into batches"""
        self.batches = [requests[i:i + self.batch_size] 
                       for i in range(0, len(requests), self.batch_size)]
        
        for idx, batch in enumerate(self.batches):
            self.status[idx] = 'pending'
        
        return self.batches
    
    def update_status(self, batch_idx, status):
        """Updates status of a batch"""
        if status in ['pending', 'completed', 'failed']:
            self.status[batch_idx] = status
    
    def get_status(self):
        """Returns current status of all batches"""
        return self.status

# Test
requests = ['req1', 'req2', 'req3', 'req4', 'req5']
processor = BatchProcessor(batch_size=2)
batches = processor.create_batches(requests)
print(batches)  # [['req1', 'req2'], ['req3', 'req4'], ['req5']]
processor.update_status(0, 'completed')
print(processor.get_status())  # {0: 'completed', 1: 'pending', 2: 'pending'}
