#############################################################################################################
#Implementation of Segment Tree
#Time Complexities:
#	Construction: O (n)
#############################################################################################################

import math;

class segTree (object):
	def __init__ (self, array):
		self.segTree = [float ('inf') for i in range (self.getSize (len (array)))];
		self.input = array;
		self.construct (self.input, self.segTree, 0, len (array) - 1, 0);

	def construct (self, array, segTree, lo, hi, pos):
		if (lo == hi):
			segTree [pos] = array [lo];
			return;
		
		mid = (lo + hi) // 2;
		self.construct (array, segTree, lo, mid, pos * 2 + 1);
		self.construct (array, segTree, mid + 1, hi, pos * 2 + 2);
		segTree [pos] = min (segTree [pos * 2 + 1], segTree [pos * 2 + 2]);

	def getSize (self, arrSize):
		exponent = math.log (arrSize, 2);
		if (exponent.is_integer ()):
			return (arrSize * 2 - 1);
		return ( (2 ** (int (exponent) + 1)) * 2 - 1 );

	def describe (self):
		print ('Array => ', self.input);
		print ('Segment Tree => ', self.segTree);


array = [int (i) for i in input ().split ()];
mySegTree = segTree (array);
mySegTree.describe ();