class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def isNotEmpty(self):
        return len(self.items) > 0


class TreeNode:
    def __init__(self, contents):
        self.contents = contents
        # self.parent = None
        self.children = []
      
    def __repr__(self):
        return f"TreeNode('{self.contents}')"

    def addChildren(self, *contents):
        children = [TreeNode(c) for c in contents]
        self.children.extend(children)
        return children

    def dfs_stack_of_pairs(self):
        """DFS using stack of pairs (node, child index)"""
        ans = []
        s = Stack()
        s.push([self, 0])  # Start with root and child index 0
        
        while s.isNotEmpty():
            node, index = s.pop()
            if index == 0:
                ans.append(node.contents)  # Process node on first visit
            
            if index < len(node.children):
                s.push([node, index + 1])  # Update index
                s.push([node.children[index], 0])  # Push the next child

        return ans

    def dfs_todos_badorder(self):
        """DFS by pushing all children at once (causes incorrect order)"""
        ans = []
        s = Stack()
        s.push(self)  # Start with root
        
        while s.isNotEmpty():
            node = s.pop()
            ans.append(node.contents)  # Process node
            
            # Push all children at once (causes reverse order)
            for child in node.children:
                s.push(child)

        return ans

    def dfs_todos_goodorder(self):
        """DFS with correct order by reversing children before pushing"""
        ans = []
        s = Stack()
        s.push(self)  # Start with root
        
        while s.isNotEmpty():
            node = s.pop()
            ans.append(node.contents)  # Process node
            
            # Push children in reverse order to maintain correct order
            for child in reversed(node.children):
                s.push(child)

        return ans


# Creating the tree
root1 = TreeNode("Z")
[Q, R, S] = root1.addChildren('Q', 'R', 'S')
[A, B, C] = Q.addChildren('A', 'B', 'C')
[D, E] = R.addChildren('D', 'E')
[F, G, H] = S.addChildren('F', 'G', 'H')
[T, U] = A.addChildren('T', 'U')
[W] = D.addChildren('W')
[X, Y] = G.addChildren('X', 'Y')
[J] = W.addChildren('J')

correct_dfs = "Z Q A T U B C R D W J E S F G X Y H".split(' ')
weird_correct_dfs = "Z S H G Y X F R E D W J Q C B A U T".split(' ')

# Testing part 1
part1_ans = root1.dfs_stack_of_pairs()
print("\nPart 1 Goal:   ", correct_dfs)
print("Part 1 Result: ", part1_ans)
print("✅ Success!" if part1_ans == correct_dfs else "❌ Failed")

# Testing part 2
part2_ans = root1.dfs_todos_badorder()
print("\nPart 2 Goal:   ", weird_correct_dfs)
print("Part 2 Result: ", part2_ans)
print("✅ Success!" if part2_ans == weird_correct_dfs else "❌ Failed")

# Testing part 3
part3_ans = root1.dfs_todos_goodorder()
print("\nPart 3 Goal:   ", correct_dfs)
print("Part 3 Result: ", part3_ans)
print("✅ Success!" if part3_ans == correct_dfs else "❌ Failed")
