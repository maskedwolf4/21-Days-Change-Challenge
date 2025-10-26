"""
### Q9

**Question:** Implement the Metropolis-Hastings MCMC algorithm for sampling from a target distribution (use normal distribution as proposal).

**Input:** `target_mean=5, target_std=2, n_samples=1000, initial_value=0, proposal_std=1`

**Expected Output:** `[sample_array]` with mean ≈ 5 and std ≈ 2

**Usage:** Bayesian inference in computational biology, parameter estimation in epidemiological models, sampling from posterior distributions
"""

import numpy as np

def metropolis_hastings(target_mean, target_std, n_samples, 
                       initial_value, proposal_std):
    """
    Metropolis-Hastings MCMC sampling from normal distribution.
    """
    samples = []
    current = initial_value
    
    def target_pdf(x):
        """Target distribution: normal PDF"""
        return np.exp(-0.5 * ((x - target_mean) / target_std)**2)
    
    for _ in range(n_samples):
        # Propose new value from normal distribution
        proposed = current + np.random.normal(0, proposal_std)
        
        # Calculate acceptance ratio
        acceptance_ratio = target_pdf(proposed) / target_pdf(current)
        
        # Accept or reject
        if np.random.uniform(0, 1) < acceptance_ratio:
            current = proposed
        
        samples.append(current)
    
    return samples

# Test
np.random.seed(42)
samples = metropolis_hastings(target_mean=5, target_std=2, 
                              n_samples=1000, initial_value=0, 
                              proposal_std=1)

print(f"Sample mean: {np.mean(samples):.2f}")
print(f"Sample std: {np.std(samples):.2f}")
print(f"First 10 samples: {samples[:10]}")
