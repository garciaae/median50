from sorting.quickselect import select as select
from sorting.quicksort import quickSort as quickSort
from sorting.mergeSort import mergesort


def selectMedian(l):
    """Returns the median without ordering the input list"""
    if len(l) % 2 == 0:
        n = len(l)
        salida = (select(l, n / 2 - 1) + select(l, n / 2)) / 2
    else:
        salida = select(l, len(l) / 2)
    return salida


def simpleMedian(l):
    """Returns the median in an ordered input list"""
    if len(l) % 2 == 0:
        n = len(l)
        salida = (l[n / 2 - 1] + l[n / 2]) / 2
    else:
        salida = l[len(l) / 2]
    return salida


def mergeMedian(l):
    """Sorts an input list and then return the median"""
    l = mergesort(l)
    if len(l) % 2 == 0:
        n = len(l)
        salida = (l[n / 2 - 1] + l[n / 2]) / 2
    else:
        salida = l[len(l) / 2]
    return salida


def quickMedian(l):
    """Sorts an input list and then return the median"""
    l = quickSort(l)
    if len(l) % 2 == 0:
        n = len(l)
        salida = (l[n / 2 - 1] + l[n / 2]) / 2
    else:
        salida = l[len(l) / 2]
    return salida
