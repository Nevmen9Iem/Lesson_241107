# Бінарне дерево Binery Tree

# class TreeNode:
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None
#
#
# class BinaryTree:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, key):
#         if self.root is None:
#             self.root = TreeNode(key)
#         else:
#             self._insert(self.root, key)
#
#     def _insert(self, current, key):
#         if key < current.key:
#             if current.left is None:
#                 current.left = TreeNode(key)
#             self._insert(current.left, key)
#         else:
#             if current.right is None:
#                 current.right = TreeNode(key)
#             else:
#                 self._insert(current.right, key)
#
#     def to_dict(self):
#         def node_to_dict(node):
#             if node is None:
#                 return None
#             return {
#                 'key': node.key,
#                 'left': node_to_dict(node.left),
#                 'right': node_to_dict(node.right)
#             }
#         return node_to_dict(self.root)
#
# tree = BinaryTree()
# tree.insert(50)
# tree.insert(30)
# tree.insert(20)
# tree.insert(40)
# tree.insert(70)
# tree.insert(60)
# tree.insert(80)
# print(tree.to_dict())

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinaryColorTree:
    def __init__(self):
        self.root = None

    def hex_to_rgb(self, hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

    def calculate_luminance(self, color):
        r, g, b = self.hex_to_rgb(color)
        return 0.2126 * r + 0.7152 * g + 0.0722 * b

    def compare_colors(self, color1, color2):
        lum1 = self.calculate_luminance(color1)
        lum2 = self.calculate_luminance(color2)
        if lum1 > lum2:
            return True

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current, key):
        if self.compare_colors(key, current.key):
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


tree = BinaryColorTree()
tree.insert('#333333')
tree.insert('#000000')
tree.insert('#ffffff')
tree.insert('#123456')
tree.insert('#111111')
tree.insert('#222222')

tree.insert('#555555')
print(tree.to_dict())