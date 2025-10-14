import unittest
from main import insertionSort, partitionArray, findMedianOfMedians

class TestMedianOfMedians(unittest.TestCase):

    def testInsertionSort(self):
        self.assertEqual(insertionSort([3, 1, 2]), [1, 2, 3])
        self.assertEqual(insertionSort([]), [])

    def testPartitioning(self):
        nums = [3, 5, 1, 5, 7, 5]
        less, equal, greater = partitionArray(nums, 5)
        self.assertTrue(all(i < 5 for i in less))
        self.assertTrue(all(i == 5 for i in equal))
        self.assertTrue(all(i > 5 for i in greater))
        self.assertEqual(len(less) + len(equal) + len(greater), len(nums))

    # check if the median of medians function works correctly by comparing 
    # its output to Python's built-in sorted function
    def testMedianOfRandom(self):
        import random
        nums = [random.randint(1, 1000) for _ in range(1000)]
        k = 500
        expected = sorted(nums)[k - 1]
        self.assertEqual(findMedianOfMedians(nums, k), expected)

    def testSmallArrays(self):
        self.assertEqual(findMedianOfMedians([45,2,44], 2), 44)
        self.assertEqual(findMedianOfMedians([3,1,2], 2), 2)
        self.assertEqual(findMedianOfMedians([5,3,8,6,2], 3), 5)
        self.assertEqual(findMedianOfMedians([7,10,4,3,20,15], 3), 7)
        self.assertEqual(findMedianOfMedians([12,3,5,7,19], 2), 5)

    def testSmallestValueOfK(self):
        self.assertEqual(findMedianOfMedians([1,2,3,4,5], 1), 1)
        self.assertEqual(findMedianOfMedians([5,4,3,2,1], 1), 1)
        self.assertEqual(findMedianOfMedians([2,3,1], 1), 1)
        self.assertEqual(findMedianOfMedians([10], 1), 10)

    def testLargestValueOfK(self):
        self.assertEqual(findMedianOfMedians([1,2,3,4,5], 5), 5)
        self.assertEqual(findMedianOfMedians([5,4,3,2,1], 5), 5)
        self.assertEqual(findMedianOfMedians([2,3,1], 3), 3)
        self.assertEqual(findMedianOfMedians([10], 1), 10)

    def testArrayWithDuplicates(self):
        self.assertEqual(findMedianOfMedians([1,2,2,3,4], 3), 2)
        self.assertEqual(findMedianOfMedians([5,5,5,5,5], 3), 5)
        self.assertEqual(findMedianOfMedians([1,1,1,2,2,2], 4), 2)
        self.assertEqual(findMedianOfMedians([3,3,3,3,3,3,3], 5), 3)

    # edge cases for k
    def testAllEqualElements(self):
        self.assertEqual(findMedianOfMedians([7,7,7,7,7], 3), 7)
        self.assertEqual(findMedianOfMedians([0,0,0,0], 2), 0)
        self.assertEqual(findMedianOfMedians([-1,-1,-1], 1), -1)
        self.assertEqual(findMedianOfMedians([-5,-5,-5,-5,-5,-5], 4), -5)

    def testNegativeNumbers(self):
        self.assertEqual(findMedianOfMedians([-3,-1,-2], 2), -2)
        self.assertEqual(findMedianOfMedians([-5,-4,-3,-2,-1], 3), -3)
        self.assertEqual(findMedianOfMedians([-10,-20,-30,-40], 2), -30)
        self.assertEqual(findMedianOfMedians([-7,0,7], 2), 0)

    

if __name__ == "__main__":
    unittest.main()
