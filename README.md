#Median50, a coding exercise!
This **median50** a *Python* coding exercise
##Problem:
Given a list of numbers say 500 in a file, find the median of the list. The constraint is none of your functions can process more than 50 numbers at a time.
##Analysing the solution
We know nothing about data. The only restriction is to proccess elements in groups of no more than 50 because the main goal is to simulate the case when the list is very big and we want to treat each function as a machine.
Having said that, I have decided to apply an external software algorithm. This kind of algorithms use external memory units as intermediate memory. 
###First stage, ordering
1. Read chunks of data with 50 numbers.
2. Order them and store in disk keeping a generator pointing to them
###Second stage, merging
3. Read a file from disk of size BS/2
4. Read a second one and merge with the first
5. Repeat the 4th step until all the data is sorted in disk
6. Select the median from the proper file or files


###References
[PEP8 Style Guide](http://legacy.python.org/dev/peps/pep-0008/)
[External sorting algorithm](http://en.wikipedia.org/wiki/External_sorting)
