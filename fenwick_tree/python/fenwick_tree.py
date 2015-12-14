#################################################################################################################################
#Implementation of Binary Indexed Tree OR Fenwick Tree
#Time Complexities:
#	Construction of Tree: O (n.log (n))
#	Updating an element: O (log (n))
#	Prefix Query (sum of elements 0 to i) or Range Minimum Query (sum of elements x to y): O (log (n))
#Space Complexity: O (n)
#################################################################################################################################

class FenTree (object):
	def __init__ (self, array):
		self.array = array;
		self.construct_tree ();

	def construct_tree (self):
		self.tree = [0 for i in range (len (self.array) + 1)];
		for i in range (len (self.array)):
			self.update (i, self.array [i]);

	def get_parent (self, child):
		return (child - (child & -child));

	def get_next (self, index):
		return (index + (index & -index));

	def update (self, index, item):
		index += 1;
		while (index <= len (self.array)):
			self.tree [index] += item;
			index = self.get_next (index);

	def prefix_sum (self, index):
		index += 1;
		total = 0;
		while (index > 0):
			total += self.tree [index];
			index = self.get_parent (index);
		return (total);

	def range_sum (self, x, y):
		x, y = min (x, y), max (x, y);
		return (self.prefix_sum (y) - self.prefix_sum (x-1));

	def describe (self):
		print ('ARRAY =>\t', self.array);
		print ('Binary Indexed Tree =>\t', self.tree);

if (__name__ == '__main__'):
#	tree = FenTree ([3,2,-1,6,5,4]);
	tree = FenTree ([int (i) for i in input ().split ()]);
	tree.describe ();
	print (tree.range_sum (2, 5));
