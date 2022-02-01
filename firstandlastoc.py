def binarySearch(A, B):
    start = 0
    end = len(A) - 1
    while start <= end:
        mid = (start + end) / 2
        if A[mid] == B:
            return mid
        if B > A[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1


def binarySearchFirst(A, B):
    start = 0
    end = len(A) - 1
    result = -1
    while start <= end:
        mid = (start + end) / 2
        if A[mid] == B:
            result = mid
            end = mid - 1
        else:
            if B > A[mid]:
                start = mid + 1
            else:
                end = mid - 1
    return result


def binarySearchLast(A, B):
    start = 0
    end = len(A) - 1
    result = -1
    while (start <= end):
        mid = (start + end) / 2
        if A[mid] == B:
            result = mid
            start = mid + 1
        else:
            if (B > A[mid]):
                start = mid + 1
            else:
                end = mid - 1
    return result


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer

    def findCount(self, A, B):
        rv1 = binarySearchLast(A, B)
        rv2 = binarySearchFirst(A, B)
        if rv1 == -1:
            return 0
        return rv1 - rv2 + 1
