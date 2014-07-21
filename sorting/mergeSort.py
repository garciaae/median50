

def mergesort(data):
    """
    Mergesort algorithm
    O(n log (n))
    """
    if len(data) < 2:
        return data
    middle = len(data) / 2
    left = mergesort(data[:middle])
    right = mergesort(data[middle:])
    return merge(left, right)


def merge(left, right):
    """
    Merge two sorted lists
    O(n)
    """
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
