from unittest import TestCase
from results import Results
from dfs import in_order_traversal, pre_order_traversal, post_order_traversal


class TestBst(TestCase):
    def test_insert(self):

        def __init__(self):
            self.results = Results()

        def test_tree_one(self):
            try:
                from build import Bst
            except ImportError:
                self.assertFalse("no class found")

            bst = Bst()
            bst.insert(5)
            bst.insert(2)
            bst.insert(8)
            bst.insert(1)
            bst.insert(3)
            in_order_traversal(bst.root, self.results.add_result)
            self.assertEqual(str(self.results), '[1, 2, 3, 5, 8]')
            self.results.clear_results()

        def test_tree_two(self):
            try:
                from build import Bst
            except ImportError:
                self.assertFalse("no class found")

            bst = Bst()
            bst.insert(1)
            bst.insert(2)
            bst.insert(3)
            bst.insert(4)
            bst.insert(5)
            in_order_traversal(bst.root, self.results.add_result)
            self.assertEqual(str(self.results), '[1, 2, 3, 4, 5]')
