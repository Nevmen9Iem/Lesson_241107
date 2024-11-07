# Бінарне дерево Binery Tree

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current, key):
        if key < current.key:
            if current.left is None:
                current.left = TreeNode(key)
            self._insert(current.left, key)
        else:
            if current.right is None:
                current.right = TreeNode(key)
            else:
                self._insert(current.right, key)

    def to_dict(self):
        def node_to_dict(node):
            if node is None:
                return None
            return {
                'key': node.key,
                'left': node_to_dict(node.left),
                'right': node_to_dict(node.right)
            }
        return node_to_dict(self.root)

tree = BinaryTree()
tree.insert(50)
tree.insert(30)
tree.insert(20)
tree.insert(40)
tree.insert(70)
tree.insert(60)
tree.insert(80)
print(tree.to_dict())