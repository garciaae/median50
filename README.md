#Median50, a coding exercise!
This is **median50** a *Python* coding exercise
##Problem:
Given a list of numbers say 500 in a file, find the median of the list. The constraint is none of your functions can process more than 50 numbers at a time.
##Analyzing the solution
We know nothing about data. The only restriction is to process elements in groups of no more than 50 because the main goal is to simulate the case when the list is very big and we want to treat each function as a machine.
Having said that, I have decided to apply an **external software algorithm**. This kind of algorithms uses external memory units as intermediate memory. 
###First stage, ordering
1. Read chunks of data with 50 numbers.
2. Order them and store in disk keeping a generator pointing to them O nlog(n)

###Second stage, merging
1. Read a file from disk of size BS/2
2. Read a second one and merge with the first
3. Repeat the 2nd step until all the data is sorted in disk O(n)
4. Select the median from the proper file or files O(1)

##Complexity
Is a mergesort (with external memory) so it's a O(n log n).It also takes O(n) to merge the partial lists. Once the data is ordered, it takes O(1) to fetch the median.

##Instalation
```
git clone https://github.com/garciaae/median50.git
python median50.py
```

###References
* [PEP8 Style Guide](http://legacy.python.org/dev/peps/pep-0008/)
* [External sorting algorithms](http://en.wikipedia.org/wiki/External_sorting)
* [Pylint](http://www.pylint.org)
* [Unit tests](http://docs.python-guide.org/en/latest/writing/tests/)
