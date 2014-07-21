from sorting.quickselect import select as select
from sorting.quicksort import quick_sort as quick_sort
from sorting.mergeSort import mergesort


def select_median(l):
    """Returns the median without ordering the input list"""
    if len(l) % 2 == 0:
        n = len(l)
        output = (select(l, n / 2 - 1) + select(l, n / 2)) / 2
    else:
        output = select(l, len(l) / 2)
    return output


def simple_median(l):
    """Returns the median in an ordered input list"""
    if len(l) % 2 == 0:
        n = len(l)
        output = (l[n / 2 - 1] + l[n / 2]) / 2
    else:
        output = l[len(l) / 2]
    return output


def merge_median(l):
    """Sorts an input list and then return the median"""
    l = mergesort(l)
    if len(l) % 2 == 0:
        n = len(l)
        output = (l[n / 2 - 1] + l[n / 2]) / 2
    else:
        output = l[len(l) / 2]
    return output


def quick_median(l):
    """Sorts an input list and then return the median"""
    l = quick_sort(l)
    if len(l) % 2 == 0:
        n = len(l)
        output = (l[n / 2 - 1] + l[n / 2]) / 2
    else:
        output = l[len(l) / 2]
    return output
