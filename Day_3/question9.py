"""
### Q9
**Question:** Implement the Viterbi algorithm for finding the most likely sequence of hidden states in a Hidden Markov Model given observations.

**Input:** `observations=[0][1][2], states=[0][1], start_prob=[0.6,0.4], trans_prob=[[0.7,0.3],[0.4,0.6]], emit_prob=[[0.5,0.4,0.1],[0.1,0.3,0.6]]`

**Expected Output:** `[0][0][1]` (most likely state sequence)

**Usage:** Gene prediction in genomic sequences, protein secondary structure prediction, speech recognition in voice-controlled medical devices
"""

import numpy as np

def viterbi(observations, states, start_prob, trans_prob, emit_prob):
    n_obs = len(observations)
    n_states = len(states)
    
    # Initialize matrices
    V = np.zeros((n_obs, n_states))
    path = np.zeros((n_obs, n_states), dtype=int)
    
    # Initialization step (t=0)
    for s in range(n_states):
        V[0][s] = start_prob[s] * emit_prob[s][observations[0]]
        path[0][s] = s
    
    # Recursion step (t>0)
    for t in range(1, n_obs):
        for s in range(n_states):
            # Find max probability path to current state
            probs = [V[t-1][prev_s] * trans_prob[prev_s][s] * emit_prob[s][observations[t]] 
                     for prev_s in range(n_states)]
            V[t][s] = max(probs)
            path[t][s] = np.argmax(probs)
    
    # Backtrack to find best path
    best_path = [0] * n_obs
    best_path[-1] = np.argmax(V[-1])
    
    for t in range(n_obs - 2, -1, -1):
        best_path[t] = path[t+1][best_path[t+1]]
    
    return best_path

# Test
observations = [0, 1, 2]
states = [0, 1]
start_prob = [0.6, 0.4]
trans_prob = [[0.7, 0.3], [0.4, 0.6]]
emit_prob = [[0.5, 0.4, 0.1], [0.1, 0.3, 0.6]]

print(viterbi(observations, states, start_prob, trans_prob, emit_prob))  
# Output: [0, 0, 1]
