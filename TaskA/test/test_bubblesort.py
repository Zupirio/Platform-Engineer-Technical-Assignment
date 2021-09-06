import unittest

from bubbleSort import bubbleSort as bubble 

class TestBubbleSortVOneAlgorithm(unittest.TestCase):

    def test_bubble_sort_with_positive_numbers(self):
        self.assertEqual(bubble([5, 5, 7, 8, 2, 4, 1]),
                         [1, 2, 4, 5, 5, 7, 8])

#     def test_bubble_sort_negative_numbers_only(self):
#         self.assertEqual(bubble_one([-1, -3, -5, -7, -9, -5]),
#                          [-9, -7, -5, -5, -3, -1])

#     def test_bubble_sort_with_negative_and_positive_numbers(self):
#         self.assertEqual(bubble_one([-6, -5, -4, 0, 5, 5, 7, 8, 2, 4, 1]),
#                          [-6, -5, -4, 0, 1, 2, 4, 5, 5, 7, 8])

#     def test_bubble_sort_same_numbers(self):
#         self.assertEqual(bubble_one([1, 1, 1, 1]), [1, 1, 1, 1])

#     def test_bubble_sort_empty_list(self):
#         self.assertEqual(bubble_one([]), [])

# class TestBubbleSortVTwoAlgorithm(unittest.TestCase):

#     def test_bubble_sort_with_positive_numbers(self):
#         self.assertEqual(bubble_two([5, 5, 7, 8, 2, 4, 1]),
#                          [1, 2, 4, 5, 5, 7, 8])

#     def test_bubble_sort_negative_numbers_only(self):
#         self.assertEqual(bubble_two([-1, -3, -5, -7, -9, -5]),
#                          [-9, -7, -5, -5, -3, -1])

#     def test_bubble_sort_with_negative_and_positive_numbers(self):
#         self.assertEqual(bubble_two([-6, -5, -4, 0, 5, 5, 7, 8, 2, 4, 1]),
#                          [-6, -5, -4, 0, 1, 2, 4, 5, 5, 7, 8])

#     def test_bubble_sort_same_numbers(self):
#         self.assertEqual(bubble_two([1, 1, 1, 1]), [1, 1, 1, 1])

#     def test_bubble_sort_empty_list(self):
#         self.assertEqual(bubble_two([]), [])


if __name__ == '__main__':
    unittest.main()