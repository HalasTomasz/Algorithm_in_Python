Implemenetion of some basic selection algorithms for coruse Algorithms and Data Structures.

RandomSelect - randomized select algorithm. Pivot picks random numbers from array.

Select - median-of-medians algorithm. We recursively we find median-of-medians and assign it as pivot. In this case w split input array modulo 5.

UpdatedSelect - median-of-medians algorithm, but contrarily to upper Select file, we recursively we split input array modulo n. 

BstSearch - searching through sorted array recursively using the same technic as is implemented in BST Search. Retunrs 0 if element isn't in array or 1 if it is.

Every implemented algorithm retunrs a number of comparison and swaps between elements
