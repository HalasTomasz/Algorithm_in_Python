List number 3

Implemenetion of some basic selection algorithms during coruse Algorithms and Data Structures:

- RandomSelect as randomized select algorithm. Pivot in partition method is randomly choosen from array.

- Select as median-of-medians algorithm. We recursively we find median-of-medians and assign it as pivot. In this case w split input array modulo 5.

- UpdatedSelect as median-of-medians algorithm, but contrarily to upper Select file, we recursively we split input array modulo n. 

- BstSearch - searching through sorted array recursively using the same technic as is implemented in BST Search. Returns 0 if element isn't in array or 1 if it is.

Every implemented algorithm returns a number of comparison and swaps between elements
