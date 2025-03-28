class LLN:
    def __init__(self, contents):
        """
        Initialize a node with the given contents.
        """
        self.contents = contents  
        self.next = None 
    def __repr__(self):
        """
        Return a string representation of the node.
        """
        return f"LLN({str(self.contents)})"

    def addAfter(self, contents):
        """
        Create a new node with 'contents' and insert it after the current node.
        - If there was already a next node, the new node takes its place, and the old next node is pushed forward.
        - Returns the new node.
        """
        new_node = LLN(contents)  # Create new node
        new_node.next = self.next  # Link new node to the current node's next node
        self.next = new_node  # Set new node as the next node of the current one
        return new_node  # Return the new node

    def toList(self):
        """
        Convert the linked list starting from this node into a Python list.
        """
        result = []
        current = self  # Start from the current node
        while current:
            result.append(current.contents)  # Add node contents to the list
            current = current.next  # Move to the next node
        return result  # Return the list

    def findLast(self):
        """
        Return the last node in the linked list.
        """
        current = self  # Start from the current node
        while current.next:  # Traverse until the last node (where next is None)
            current = current.next
        return current  # Return the last node

    def findAfter(self, needle):
        """
        Find the first node after the current node that contains 'needle'.
        - If found, return that node.
        - If not found, raise a KeyError.
        """
        current = self  # Start searching from this node
        while current:
            if current.contents == needle:
                return current  # Return the matching node
            current = current.next  # Move to the next node
        raise KeyError(f"{needle} not found in linked list")  # Raise an error if not found


# === ✅ MAIN FUNCTION (TESTING) ===
if __name__ == "__main__":
    # Step 1: Create the first node (head of the list)
    head = LLN("A")
    
    # Step 2: Add nodes
    node_b = head.addAfter("B")
    node_c = node_b.addAfter("C")
    node_d = node_c.addAfter("D")
    
    # Step 3: Print the list
    print("Linked List:", head.toList())  # Output: ['A', 'B', 'C', 'D']
    
    # Step 4: Find the last node
    last_node = head.findLast()
    print("Last Node:", last_node)  # Output: LLN(D)
    
    # Step 5: Find a specific node
    try:
        found_node = head.findAfter("C")
        print("Found Node:", found_node)  # Output: LLN(C)
    except KeyError as e:
        print(e)
    
    # Step 6: Attempt to find a non-existent value
    try:
        head.findAfter("X")
    except KeyError as e:
        print("Error:", e)  # Output: Error: 'X not found in linked list'
