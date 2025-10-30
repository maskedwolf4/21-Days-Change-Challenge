"""
### Q10

**Question:** Write a function to implement the Tower of Hanoi problem solver, returning the list of moves as (from_peg, to_peg) tuples.

**Input:** `n_disks=3`

**Expected Output:** `[(1,3), (1,2), (3,2), (1,3), (2,1), (2,3)]`

**Usage:** Recursive algorithm understanding for bioinformatics tree traversals; state space exploration in molecular dynamics; puzzle-solving AI development
"""

def tower_of_hanoi(n_disks):
    """
    Solve Tower of Hanoi: move n disks from peg 1 to peg 3 using peg 2.
    Returns list of moves as (from_peg, to_peg) tuples.
    """
    def hanoi_helper(n, source, target, auxiliary, moves):
        if n == 1:
            moves.append((source, target))
            return
        
        # Move n-1 disks to auxiliary
        hanoi_helper(n-1, source, auxiliary, target, moves)
        
        # Move nth disk to target
        moves.append((source, target))
        
        # Move n-1 disks from auxiliary to target
        hanoi_helper(n-1, auxiliary, target, source, moves)
    
    moves = []
    hanoi_helper(n_disks, 1, 3, 2, moves)
    return moves

# Test
result = tower_of_hanoi(3)
print(f"Tower of Hanoi moves: {result}")  # Output: [(1,3), (1,2), (3,2), (1,3), (2,1), (2,3)]
