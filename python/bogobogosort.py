'''

Implementation of bogobogosort. To be familiar with this sorting algorithm, clients
must be aware of the general algorithm for the original bogosort. Bogosort to sort
a deck of cards, for example, is:

proc bogosort(deck):

	WHILE deck is not sorted:
		throw cards into the air and pick them up    # aka randomize the deck
	ENDWHILE

endproc

The average-case time complexity of bogosort, assuming that checking the condition that
the deck is sorted is O(n), is O(n*n!), since there are n! permutations of a list.

----------------------------------------------------------------------------------------

However, what if checking if the deck is sorted was to be done with more bogosort?

Every computer scientist knows that recursion should be incorporated in any algorithm
if at all possible, since recursion is good. We then modify bogosort such that the
fundamental logic stays the same, but the checking of whether the list is sorted can
be described, in pseudocode, as:

func isSorted(list):
	
	1. newList = copyOf(list)
	2. sort the first n-1 elements of newList by recursively calling bogobogosort

	IF last element of newList > max element of the first n-1 elements of newList THEN:
		newList is now sorted
	ELSE:   # newList is not sorted!
		randomize newList
		go back to step 2
	ENDIF

	return TRUE if newList is in the same order as the original list
			FALSE if not

endfunc

In English, this algorithm starts from the singleton list as sorted, and as the program
tacks on more and more numbers to the list, uses bogosort to sort increasingly large 
subsets up until the original list. However, if the list is ever not sorted, we start 
over entirely from square one!

The time complexity of bogobogosort is currently unknown and heavily debated in the
computer science community. However it is safe to assume that it is at least
O((n!)^(n)), perhaps even O((n!)^(n!))!

On a computer with CPU i7-3630QM and a clock speed of 2.4GHz, the following tests
were made. Compare these times with the original bogosort:

size of list |  bogosort time (s) |  bogobogosort time (s)
-----------------------------------------------------------------------
	  1      |  0.00023819227034  |      0.000205
	  2      |  0.00028352149953  |      0.000278
	  3      |  0.00032414675210  |      0.000534
	  4      |  0.00060125373806  |      0.022259
	  5      |  0.00073125454629  |     31.690154
	  6      |  0.00642520441985  |  34093.653116 (almost half a day!)
	  7      |  0.00506618281278  |  likely several decades...........

In conclusion, it is quite beneficial for large-scale companies to replace all sorting
in their code with bogobogosort as it is likely more efficient than the crap that they
do now - it takes A WHOLE FREAKING SECOND after I hit Enter on a Google search to get
my search results!!

(C) Allen Cheng 2015

'''

from random import shuffle
from timeit import default_timer as timer


def isSorted(li):

	copy = list(li)  # Make a copy of the list

	# (Recursively) Sort the first n-1 elements
	sortedMinusLast = mostEfficientSort(copy[:-1])  

	# Is the nth element of the list greater than the sorted first n-1 elements?
	while copy[-1] < max(sortedMinusLast):
		# If not, randomize the list and return to recursively bogobogosorting
		shuffle(copy)
		sortedMinusLast = mostEfficientSort(copy[:-1])

	# The copy is sorted correctly - check whether the ORIGINAL list reflects the
	# sorted list.
	return sortedMinusLast == li[:-1]


def mostEfficientSort(li):

	# Base case: The singleton list is already sorted
	if len(li) == 1:
		return li

	# Otherwise, apply bogosort logic
	while isSorted(li) == False:
		shuffle(li)

	return li

l = list(range(5, 0, -1))
start = timer()
print(mostEfficientSort(l))
print("Bogobogosort finished in " + str(timer() - start) + " seconds!")