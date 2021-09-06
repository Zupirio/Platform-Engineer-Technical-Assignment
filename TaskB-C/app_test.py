import unittest

from bubbleSort import bubbleSort as bubble


class TestBubbleSortVOneAlgorithm(unittest.TestCase):

    def test_bubble_sort_with_positive_numbers(self):
        self.assertEqual(bubble([5, 5, 7, 8, 2, 4, 1]), [1, 2, 4, 5, 5, 7, 8])

    def test_bubble_sort_negative_numbers_only(self):
        self.assertEqual(bubble([-1, -3, -5, -7, -9, -5]),
                         [-9, -7, -5, -5, -3, -1])

    def test_bubble_sort_nested_list(self):
        self.assertEqual(bubble([6, 2, [4, 3], [5, 1, 1, [2, 3]]]), [
                         1, 1, 2, 2, 3, 3, 4, 5, 6])

    # def test_bubble_sort_with_long_nest(self):
    #     self.assertEqual(bubble([96, [[6, 2, [4, 3],[5, 1, 1,[2, 3]]], 94, [6, 2, [4, 3],[5, 1,[6, 2, [4, 3],[5, 1, 1,[2,[ 88,2, [4, 3],[5, 1, 1,[2,3]]],[6, 2, [4, 3],[1, 1,[2,3]]],3]]],[2,3]]], 4, 100, 65, 72, 51], 64, 92,[6, 2, [4, 3],[5, 1, 1,[2,3]]], 50, 94,[6, 2, [4, 3],[5, 1,[6, 2, [4, 3],[5, 1, 1,[2,[6, 2, [4, 3],[[2,3]]],[6, 2, [4, 3],[5, 1, 1,[2,3]]],3]]],[2,3]]], 4, 100, 65, 72, 51], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 50, 51, 51, 64, 65, 65, 72, 72, 88, 92, 94, 94, 96, 100, 100]))

    def test_bubble_sort_None_value(self):
        self.assertEqual(bubble([1, None, 1, 1]), [1, 1, 1])

    def test_bubble_sort_empty_list(self):
        self.assertEqual(bubble([]), [])

    def test_bubble_sort_thousands(self):
        self.assertEqual(bubble([1, 2, 3, 4, [100, 200, 300, [1000, 2000, 3000]]]), [
                         1, 2, 3, 4, 100, 200, 300, 1000, 2000, 3000])


if __name__ == '__main__':
    unittest.main()
