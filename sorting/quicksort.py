

def quick_sort(arr):
    """
    Sorts an array with a lazy pivot strategy.
    O(n log(n))
    """
    less = []
    pivot_list = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivot_list.append(i)
        less = quick_sort(less)
        more = quick_sort(more)
        return less + pivot_list + more
