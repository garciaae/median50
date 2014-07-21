"""This is the median 50 coding exercise. We're going to compute the
median of a given set with the restriction of not processing more than
50 numbers at a time."""

import array
from math import ceil, floor
import heapq
import os
import struct
import sys
import tempfile
import unittest

from statistics.medianAlgorithms import selectMedian as selectMedian
from statistics.medianAlgorithms import simpleMedian as simpleMedian

FILEPREFIX = "./temp/merge50_"
INPUTFILENAME = "./data/500numbers.txt"
DELETETEMPFILES = True


def readnfromfile(order, n):
    """
    Given a set of files returns the n-th value of the order-th file
    """
    with open(FILEPREFIX + "{:0>3d}".format(int(order)), "r") as filehandler:
        # Put a cursor in its place before reading
        filehandler.seek(int(n - 1) * 4)
        elementn, = struct.unpack('i', filehandler.read(4))
    return elementn


def pickmedianfromcollection(numelements, elementsperfile):
    """
    Returns the median of a set of numbers sorted in a file
    collection
    """
    #numberoffiles = ceil(numelements / elementsperfile)
    oddmedian = ceil(numelements / 2)
    whichfile1 = ceil(oddmedian / elementsperfile) - 1
    file1order = oddmedian - elementsperfile * whichfile1
    firstvalue = readnfromfile(whichfile1, file1order)
    evenmedian = 0
    whichfile2 = 0
    file2order = 0
    # Par
    if numelements % 2 == 0:
        evenmedian = numelements / 2 + 1
        whichfile2 = int(floor(evenmedian / elementsperfile))
        file2order = evenmedian - elementsperfile * whichfile2
        # fetch in files!
        secondvalue = readnfromfile(whichfile2, file2order)
        medianvalue = (firstvalue + secondvalue) / 2
    else:
        medianvalue = firstvalue

    return medianvalue


def intsfromfile(filehandler):
    """
    Generator for reading from file
    """
    while True:
        a = array.array('i')
        a.fromstring(filehandler.read(4))
        if not a:
            break
        for x in a:
            yield x


def externalmedian(filename, blocksize=50):
    """
    Computes the median for a file with an unsortered list of numbers
    with the constraint of not processing more than 50 numbers at a time
    """
    lista = []
    iters = []
    i = 0

    # We read in blocks of size = blocksize / 2 for compliance with the
    # constraints
    for number in open(filename, "r"):
        lista.append(int(number.strip()))
        i = i + 1
        if i % (blocksize / 2) == 0:
            a = array.array('i')
            a.fromlist(lista)
            filehandler = tempfile.TemporaryFile()
            array.array('i', sorted(a)).tofile(filehandler)
            filehandler.seek(0)
            # Create a generators list
            iters.append(intsfromfile(filehandler))
            lista = []
    # Check if we have not processed data
    if len(lista) > 0:
        a = array.array('i')
        a.fromlist(lista)
        filehandler = tempfile.TemporaryFile()
        array.array('i', sorted(a)).tofile(filehandler)
        filehandler.seek(0)
        iters.append(intsfromfile(filehandler))

    a = array.array('i')

    # Merge blocksize/2 sized lists for compliance with the constraints
    i = 0
    numberoffiles = 0
    for element in heapq.merge(*iters):
        a.append(element)
        i = i + 1
        # In compliance of the question constraints
        if len(a) % blocksize == 0:
            with open(FILEPREFIX + "{:0>3d}".format(numberoffiles), "w") as \
                filehandler2:
                a.tofile(filehandler2)
            del a[:]
            numberoffiles = numberoffiles + 1
    if a:
        with open(FILEPREFIX + "{:0>3d}".format(numberoffiles), "w") as \
            filehandler2:
            a.tofile(filehandler2)

    numberofelements = numberoffiles * blocksize + len(a)

    # Find the median into the merged files
    median = pickmedianfromcollection(numberofelements, blocksize)

    # If chosen, delete temporary files
    if DELETETEMPFILES:
        [os.remove(FILEPREFIX + "{:0>3d}".format(i))
         for i in range(numberoffiles)]

    return median


def getdatafromfile(filename):
    """Gets all the numbers from file. Used for testing."""
    exitvalue = []
    for line in open(filename, "r"):
        try:
            exitvalue.append(int(line.strip()))
        except ValueError:
            print "Not a number!"
            continue
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise
    return exitvalue


class MedianCase(unittest.TestCase):

    """Test cases for Median"""

    def test_starting_out(self):
        """Simple test!"""
        self.assertEqual(1, 1)

    def test_list_contains_numbers(self):
        """Checks if the list contains only numbers"""
        errorinlist = False
        for value in getdatafromfile(INPUTFILENAME):
            try:
                int(value)
            except ValueError:
                errorinlist = True
                continue
        self.assertEqual(errorinlist, False)

    def test_list_size(self):
        """Checks if the list has a length of 500 elements"""
        self.assertEqual(len(getdatafromfile(INPUTFILENAME)), 500)

    def test_simple_median(self):
        """Test the simple median"""
        self.assertEqual(simpleMedian([1, 2, 3, 4, 5]), 3)

    def test_select_median(self):
        """Based on previous, test the select median"""
        a = [5, 1, 2, 4, 3]
        self.assertEqual(simpleMedian(sorted(a)), selectMedian(a))

    def test_select_median_for_data(self):
        """Based on previous, test the select median with data from file
        """
        l = getdatafromfile(INPUTFILENAME)
        a = selectMedian(l)
        b = simpleMedian(sorted(l))
        self.assertEqual(a, b)

    def test_external_median(self):
        """Based on previous, test the external median with data from
        file"""
        l = getdatafromfile(INPUTFILENAME)
        a = selectMedian(l)
        b = externalmedian(INPUTFILENAME, 50)
        self.assertEqual(a, b)


def main():
    """main method for testing purposes"""
    unittest.main()

if __name__ == '__main__':
    main()
