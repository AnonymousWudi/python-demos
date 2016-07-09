# coding=utf-8


class Tree_Node():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def setLeft(self, node):
        self.left = node

    def setRight(self, node):
        self.right = node

    def setVal(self, val):
        self.val = val

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getVal(self):
        return self.val

tree_array = []
path_node = []


def midTraversal(root):
    if root:
        midTraversal(root.left)
        tree_array.append(root.val)
        midTraversal(root.right)


def getMaxMin(array):
    if not array:
        return None, None
    elif len(array) == 1:
        return array[0], array[0]
    else:
        node_max = array[0]
        node_min = array[0]
        for i in array:
            node_max = max(i, node_max)
            node_min = min(i, node_min)
        return node_max, node_min


def findPath(root, value):
    if root and root.val == value:
        return True
    if not root:
        return
    if findPath(root.left, value):
        path_node.append(root.val)
        return True
    elif findPath(root.right, value):
        path_node.append(root.val)
        return True

if __name__ == '__main__':
    root = Tree_Node(5)
    node_one = Tree_Node(1)
    node_two = Tree_Node(4)
    node_three = Tree_Node(7)
    node_four = Tree_Node(2)
    node_five = Tree_Node(10)
    node_six = Tree_Node(6)
    node_seven = Tree_Node(8)
    node_eight = Tree_Node(9)

    root.setLeft(node_one)
    root.setRight(node_two)
    node_one.setLeft(node_three)
    node_one.setRight(node_four)
    node_two.setLeft(node_five)
    node_two.setRight(node_six)
    node_three.setLeft(node_seven)
    node_five.setRight(node_eight)

    midTraversal(root)
    node_max, node_min = getMaxMin(tree_array)
    findPath(root, node_min)
    step_min = len(path_node)
    path_node = []
    findPath(root, node_max)
    step_max = len(path_node)
    if step_max >= step_min:
        print step_max - step_min + 2
    else:
        print step_min - step_max + 2
