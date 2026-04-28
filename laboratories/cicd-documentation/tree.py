from node import Node
import unittest

class Tree:
    """ Tree class for binary tree """

    def __init__(self):
        """ Constructor for Tree class """
        self.root = None

    def getRoot(self):
        """ Method for get root of the tree """
        return self.root

    def add(self, data):
        """ Method for add data to the tree """
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        """Method for add data to the tree

        Args:
            data (int): data to add

        Returns:
            None
        """
        if data < node.data:
            if node.left is not None:
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right is not None:
                self._add(data, node.right)
            else:
                node.right = Node(data)

    def find(self, data):
        """Method for find data in the tree

        Args:
            data (int): data to find

        Returns:
            Node: node with data
        """
        if self.root is not None:
            return self._find(data, self.root)
        else:
            return None

    def _find(self, data, node):
        if data == node.data:
            return node
        elif (data < node.data and node.left is not None):
            return self._find(data, node.left)
        elif (data > node.data and node.right is not None):
            return self._find(data, node.right)

    def deleteTree(self):
        self.root = None

    def printTree(self):
        if self.root is not None:
            self._printInorderTree(self.root)

    def _printInorderTree(self, node):
        if node is not None:
            self._printInorderTree(node.left)
            print(str(node.data) + ' ')
            self._printInorderTree(node.right)

    def _printPreorderTree(self, node):
        # TODO
        if node is not None:
            print(str(node.data) + ' ')
            self._printPreorderTree(node.left)
            self._printPostorderTree(node.right)

    def _printPostorderTree(self, node):
        # TODO
        if node is not None:
            self._printPreorderTree(node.left)
            self._printPostorderTree(node.right)
            print(str(node.data) + ' ')


class TestTreeFind(unittest.TestCase):
    def setUp(self):
        self.tree = Tree()
        values = [50, 30, 70, 20, 40]
        for v in values:
            self.tree.add(v)

    def test_find_non_existing_element(self):
        result = self.tree.find(100)
        self.assertIsNone(result, "Should be none")

    def test_find_root(self):
        result = self.tree.find(50)
        self.assertEqual(result, self.tree.getRoot(), "Root was not found.")

if __name__ == '__main__':
    unittest.main()
