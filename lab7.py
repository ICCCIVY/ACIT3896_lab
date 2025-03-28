from collections import deque


class Queue:
    """Custom queue using a list (inefficient for removing from the front)"""
    def __init__(self):
        self.items = []

    def add(self, item):
        """Enqueue an item (adds to the back)"""
        self.items.append(item)

    def remove(self):
        """Dequeue an item (removes from the front)"""
        if self.isNotEmpty():
            return self.items.pop(0)
        raise IndexError("Queue is empty!")

    def isNotEmpty(self):
        """Check if the queue has elements"""
        return len(self.items) > 0


class TreeNode:
    """Tree Node Implementation"""
    def __init__(self, contents):
        self.contents = contents
        self.children = []

    def __repr__(self):
        return f"TreeNode('{self.contents}')"

    def addChildren(self, *contents):
        """Add multiple children nodes"""
        children = [TreeNode(c) for c in contents]
        self.children.extend(children)
        return children

    def bfs_badqueue(self):
        """Breadth-First Search using inefficient Queue implementation"""
        queue = Queue()
        queue.add(self)
        result = []

        while queue.isNotEmpty():
            node = queue.remove()
            result.append(node.contents)

            for child in node.children:
                queue.add(child)  # Enqueue all children

        return result

    def bfs_deque(self):
        """Breadth-First Search using collections.deque"""
        queue = deque([self])
        result = []

        while queue:
            node = queue.popleft()  # More efficient than pop(0)
            result.append(node.contents)

            for child in node.children:
                queue.append(child)  # Enqueue all children

        return result

    def dfs_deque(self):
        """Depth-First Search using collections.deque (stack behavior)"""
        stack = deque([self])
        result = []

        while stack:
            node = stack.pop()  # LIFO order
            result.append(node.contents)

            # Reverse the order of children so that leftmost is visited first
            for child in reversed(node.children):
                stack.append(child)

        return result


"""
A tree could look like this:
               Z
           /   |   \ 
        Q      R      S
      / | \   / \   / | \ 
    A   B  C  D E  F  G  H
   / \        |      / \ 
  T   U       W     X   Y
              |
              J
"""

root1 = TreeNode("Z")
[Q, R, S] = root1.addChildren("Q", "R", "S")
[A, B, C] = Q.addChildren("A", "B", "C")
[D, E] = R.addChildren("D", "E")
[F, G, H] = S.addChildren("F", "G", "H")
[T, U] = A.addChildren("T", "U")
[W] = D.addChildren("W")
[X, Y] = G.addChildren("X", "Y")
[J] = W.addChildren("J")

correct_dfs = "Z Q A T U B C R D W J E S F G X Y H".split(" ")
correct_bfs = "Z Q R S A B C D E F G H T U W X Y J".split(" ")

# **Testing bfs_badqueue**
part1_ans = root1.bfs_badqueue()
print("\npart 1 goal:   ", correct_bfs)
print("part 1 actual: ", part1_ans)
print("part 1 successful match" if part1_ans == correct_bfs else "Mismatch!")

# **Testing bfs_deque**
part2_ans = root1.bfs_deque()
print("\npart 2 goal:   ", correct_bfs)
print("part 2 actual: ", part2_ans)
print("part 2 successful match" if part2_ans == correct_bfs else "Mismatch!")

# **Testing dfs_deque**
part3_ans = root1.dfs_deque()
print("\npart 3 goal:   ", correct_dfs)
print("part 3 actual: ", part3_ans)
print("part 3 successful match" if part3_ans == correct_dfs else "Mismatch!")
