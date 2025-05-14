def minimax(tree, node, is_maximizing_player):
    """Minimax algorithm for game trees.
    
    This function evaluates the best move for a player in a zero-sum game by
    alternating between maximizing and minimizing potential scores.
    
    Args:
        tree: Dictionary representing the game tree, where keys are nodes and values
              are either lists of children or integer values for leaf nodes
        node: Current node being evaluated
        is_maximizing_player: Boolean indicating if this is the maximizing player's turn
        
    Returns:
        The best possible score from this node
    """
    # Base case: If node is a leaf (has a numeric value), return its value
    if not isinstance(tree[node], list):
        return tree[node]
    
    # If maximizing player's turn
    if is_maximizing_player:
        # Initialize best value to negative infinity
        best_value = float('-inf')
        
        # Evaluate all child nodes
        for child in tree[node]:
            # Recursively call minimax for child (opponent's turn)
            value = minimax(tree, child, False)
            # Update best value if child's value is better
            best_value = max(best_value, value)
            
        return best_value
    
    # If minimizing player's turn
    else:
        # Initialize best value to positive infinity
        best_value = float('inf')
        
        # Evaluate all child nodes
        for child in tree[node]:
            # Recursively call minimax for child (opponent's turn)
            value = minimax(tree, child, True)
            # Update best value if child's value is lower
            best_value = min(best_value, value)
            
        return best_value

def build_tree_from_input():
    """Build a game tree from user input."""
    print("Minimax Algorithm for Game Trees")
    print("--------------------------------")
    print("This algorithm helps find the best move in turn-based games like Tic-Tac-Toe,")
    print("Chess, etc. by evaluating all possible future moves assuming optimal play.")
    print("\nTree Structure Input:")
    
    # Get internal (non-leaf) nodes
    n = int(input("Number of non-leaf nodes: "))
    tree = {}
    print("For each internal node, enter: node child1 child2 ...")
    print("Example: A B C (means node A has children B and C)")
    
    for _ in range(n):
        parts = input().split()
        if parts:
            node, children = parts[0], parts[1:]
            tree[node] = children
    
    # Get leaf nodes with their values
    m = int(input("Number of leaf nodes: "))
    print("For each leaf, enter: node value")
    print("Example: D 5 (means leaf node D has value 5)")
    
    for _ in range(m):
        parts = input().split()
        if len(parts) >= 2:
            leaf, val = parts[0], parts[1]
            try:
                tree[leaf] = int(val)
            except ValueError:
                print(f"Warning: Couldn't convert '{val}' to integer, using 0 instead")
                tree[leaf] = 0
    
    return tree

def main():
    """Main function that builds a tree and runs minimax on it."""
    # Build the game tree from user input
    tree = build_tree_from_input()
    
    # Get the root node
    root = input("Root node: ")
    
    # Ensure root exists in the tree
    if root not in tree:
        print(f"Error: Root node '{root}' not found in the tree")
        return
    
    # Run the minimax algorithm starting from the root
    best_value = minimax(tree, root, True)
    
    # Display result
    print("\nResults:")
    print("-" * 30)
    print(f"Minimax value at root: {best_value}")
    print("This is the best achievable outcome for the maximizing player")
    print("assuming both players play optimally.")

if __name__ == "__main__":
    main()