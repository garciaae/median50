from sorting.quickselect import select as select
from sorting.quicksort import quickSort as quickSort
from sorting.mergeSort import mergesort


def selectMedian(l):
    if len(l) % 2 == 0:
        n = len(l)
        salida = (select(l, n / 2 - 1) + select(l, n / 2)) / 2
    else:
        salida = select(l, len(l) / 2)
    return salida


def simpleMedian(l):
    if len(l) % 2 == 0:
        n = len(l)
        salida = (l[n / 2 - 1] + l[n / 2]) / 2
    else:
        salida = l[len(l) / 2]
    return salida


def mergeMedian(l):
    l = mergesort(l)
    if len(l) % 2 == 0:
        n = len(l)
        salida = (l[n / 2 - 1] + l[n / 2]) / 2
    else:
        salida = l[len(l) / 2]
    return salida


def quickMedian(l):
    l = quickSort(l)
    if len(l) % 2 == 0:
        n = len(l)
        salida = (l[n / 2 - 1] + l[n / 2]) / 2
    else:
        salida = l[len(l) / 2]
    return salida
