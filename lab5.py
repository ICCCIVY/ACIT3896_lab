
class TreeNode:
    def __init__(self, contents):
        self.contents = contents
        self.parent = None
        self.children = []
      
    def __repr__(self):
        # this is a mediocre repr function, it's not very good at all, but it'll do for now
        return f"TreeNode(contents={repr(self.contents)}, parent-contents={repr(self.parent.contents if self.parent else 'NOPARENT')}, num-children={len(self.children)})"

    def appendChild(self, contents):
        # should create a new node and add it as a child of the current node, AFTER any existing nodes
        # return the node you create
        new_node = TreeNode(contents)
        new_node.parent = self
        self.children.append(new_node)
        return new_node

    def prependChild(self, contents):
        # should create a new node and add it as a child of the current node, BEFORE any existing nodes
        # return the node you create
        new_node = TreeNode(contents)
        new_node.parent = self
        self.children.insert(0,new_node)
        return new_node

    def findRoot(self):
        # returns the root of the tree that the current node is in (note that current node might be root)
        if self.parent is None:  
            return self
        else:  
            return self.parent.findRoot() 

    def findLeftmostLeaf(self):
        # a "descendant" is a child, or a child-of-child, or child-of-child-of-child, etc
        # this method should travel only down the left edge of the tree, as far as it can
        if not self.children:
            return self
        else:
            return self.children[0].findLeftmostLeaf()

    def findRightmostLeaf(self):
        # a "descendant" is a child, or a child-of-child, or child-of-child-of-child, etc
        # this method should travel only down the right edge of the tree, as far as it can
        if not self.children:
            return self
        else:
            return self.children[-1].findRightmostLeaf()




def case1():
    # This is supposed to make this tree:
    #
    #            A
    #         /  |  \
    #        B   C   D
    #
    root = TreeNode("A")
    root.appendChild("B")
    root.appendChild("C")
    root.appendChild("D")

    print("\ncase1")

    # once you have implemented appendChild, the first print should work
    print("I hope the root has 3 children")
    print(root)

    # once you're nearly done, these prints should work too
    print("I hope the leftmost leaf is B, and B's parent is A")
    print(root.findLeftmostLeaf())
    print("I hope the rightmost leaf is D, and D's parent is A")
    print(root.findRightmostLeaf())


def case2():
    # This is supposed to make the same tree as last time, but differently:
    #
    #            A
    #         /  |  \
    #        B   C   D
    #
    root = TreeNode("A")
    root.prependChild("C")
    root.appendChild("D")
    root.prependChild("B")

    print("\ncase2")

    # once you have implemented prependChild, the first print should work
    print("I hope the root has 3 children")
    print(root)

    # once you're nearly done, these prints should work too
    print("I hope the leftmost leaf is B, and B's parent is A")
    print(root.findLeftmostLeaf())
    print("I hope the rightmost leaf is D, and D's parent is A")
    print(root.findRightmostLeaf())


def case3():
    # This is supposed to make this tree:
    #
    #            A
    #         /  |  \
    #        B   C   D
    #        |      / \
    #        E     F   G
    #
    root = TreeNode("A")
    c = root.appendChild("C")
    d = root.appendChild("D")
    b = root.prependChild("B")
    g = d.prependChild("G")
    f = d.prependChild("F")
    e = b.appendChild("E")

    print("\ncase3")


    # and all of the following should print the root node (each one prints itself and then the root):
    for node in [root, b, c, d, e, f, g]:
        r = node.findRoot()
        print("node:", node, "   found root:   ", r, "   is correct tho? ", r == root)

    # and the following should be able to find E:
    print("findLeftmostLeaf of root, should be E:", root.findLeftmostLeaf())
    # and the following should be able to find F:
    print("findLeftmostLeaf of D, should be F:", d.findLeftmostLeaf())
    # and the following should be able to find G:
    print("findRightmostLeaf of D, should be G:", d.findRightmostLeaf())



def main(args):
    case1()
    case2()
    case3()




if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
