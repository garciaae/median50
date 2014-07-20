import array
from math import ceil, floor
import heapq
import os
import struct
import sys
import tempfile
import time

from statistics.medianAlgorithms import mergeMedian as mergeMedian
from statistics.medianAlgorithms import selectMedian as selectMedian
from statistics.medianAlgorithms import quickMedian as quickMedian


FILEPREFIX = "./temp/merge50_"
INPUTFILENAME = "./data/500numbers.txt"
DELETETEMPFILES = True


def chronometer(funcion):
    def funcion_a_ejecutar(*argumentos):
        # Starting time
        inicio = time.time()
        # launch the function
        ret = funcion(*argumentos)
        # Finishing time
        fin = time.time()
        # Total time
        tiempo_total = fin - inicio
        return tiempo_total
    # return the main function
    return funcion_a_ejecutar


def readNFromFile(order, n):
    with open(FILEPREFIX + "{:0>3d}".format(int(order)), "r") as f:
        f.seek(int(n - 1) * 4)
        n1, = struct.unpack('i', f.read(4))
    return n1


def pickMedianFromCollection(numElements, elementsPerFile):
    numberOfFiles = ceil(numElements / elementsPerFile)
    n1 = ceil(numElements / 2)
    whichFile1 = ceil(n1 / elementsPerFile) - 1
    file1Order = n1 - elementsPerFile * whichFile1
    firstValue = readNFromFile(whichFile1, file1Order)
    n2 = 0
    whichFile2 = 0
    file2Order = 0
    # Par
    if numElements % 2 == 0:
        n2 = numElements / 2 + 1
        whichFile2 = int(floor(n2 / elementsPerFile))
        file2Order = n2 - elementsPerFile * whichFile2
        # fetch in files!
        secondValue = readNFromFile(whichFile2, file2Order)
        medianValue = (firstValue + secondValue) / 2
    else:
        medianValue = firstValue

    return medianValue


def intsfromfile(f):
    while True:
        a = array.array('i')
        a.fromstring(f.read(4))
        if not a:
            break
        for x in a:
            yield x


def externalMedian(filename, BS=50):
    lista = []
    iters = []
    i = 0

    # We read from BS to BS
    for number in open(filename, "r"):
        lista.append(int(number.strip()))
        i = i + 1
        if i % (BS / 2) == 0:
            a = array.array('i')
            a.fromlist(lista)
            # Creamos un archivo temporal
            f = tempfile.TemporaryFile()
            # Adjuntamos el array ordenado
            array.array('i', sorted(a)).tofile(f)
            # Rebobinamos
            f.seek(0)
            # Adjuntamos a la lista de generadores
            iters.append(intsfromfile(f))
            # limpiamos la lista
            lista = []
    if len(lista) > 0:
        a = array.array('i')
        a.fromlist(lista)
        # Creamos un archivo temporal
        f = tempfile.TemporaryFile()
        # Adjuntamos el array ordenado
        array.array('i', sorted(a)).tofile(f)
        # Rebobinamos
        f.seek(0)
        # Adjuntamos a la lista de generadores
        iters.append(intsfromfile(f))

    # print i, "numbers read and", i / 25, "lists generated"

    a = array.array('i')

    # Merge BS/2 sized lists
    i = 0
    numberOfFiles = 0
    for element in heapq.merge(*iters):
        a.append(element)
        i = i + 1
        if len(a) % BS == 0:
            with open(FILEPREFIX + "{:0>3d}".format(numberOfFiles), "w") as f2:
                a.tofile(f2)
            del a[:]
            numberOfFiles = numberOfFiles + 1
    if a:
        with open(FILEPREFIX + "{:0>3d}".format(numberOfFiles), "w") as f2:
            a.tofile(f2)
        # print "Last file named", FILEPREFIX +
        # "{:0>3d}".format(numberOfFiles), "has a length of", len(a)

    # print numberOfFiles, "files of", BS, "elements each has been generated"
    # print i, "elements read"

    numberOfElements = numberOfFiles * BS + len(a)

    # Find the median into the merged files
    median = pickMedianFromCollection(numberOfElements, BS)
    if DELETETEMPFILES:
        [os.remove(FILEPREFIX + "{:0>3d}".format(i))
         for i in range(numberOfFiles)]

    return median


if __name__ == '__main__':
    data = [int(line.strip()) for line in open(INPUTFILENAME, "r")]
    print "Computing time for a set of", len(data), "elements"
    salida1 = chronometer(selectMedian)(data)
    salida2 = chronometer(quickMedian)(data)
    salida3 = chronometer(mergeMedian)(data)
    salida4 = chronometer(externalMedian)(INPUTFILENAME, 50)

    # salida3 = cronometro(mergeMedian)(data)
    print "Selection median: ", salida1
    print "Quicksort median: ", salida2
    print "Mergesort median: ", salida3
    print "External sort median: ", salida4
