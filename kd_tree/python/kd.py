##########################################################################################################
#Implementation of KD Tree - Construction (through insert ()), find_minimum (), delete ()
##########################################################################################################

class Node (object):
	def __init__ (self, item, level, left, right):
		self.item = item;
		self.left, self.right = left, right;
		self.level = level;

class KDTree (object):
	def __init__ (self, dimension, array):
		self.dim = dimension;
		self.array = array;
		self.root = Node (self.array [0], 0, None, None);

		for item in array [1 : ]:
			self.insert (self.root, item);

	def insert (self, root, item):
		current_dim = root.level % self.dim;
		if (item [current_dim] < root.item [current_dim]):
			if (root.left):
				self.insert (root.left, item);
			else:
				root.left = Node (item, root.level + 1, None, None);
		else:
			if (root.right):
				self.insert (root.right, item);
			else:
				root.right = Node (item, root.level + 1, None, None);

	def find_min (self, root, dimension):
		if (not root):
			return (float ('inf'));
		if (root.level % self.dim == dimension):
			if (root.left):
				return (self.find_min (root.left, dimension));
			else:
				return (root.item [dimension]);
		else:
			return (min (
				root.item [dimension],
				self.find_min (root.left, dimension),
				self.find_min (root.right, dimension)
			));

	def delete (self, root, item):
		#################UNDER CONSTRUCTION######################
		if (root.item == item):
			if (root.right):
				pass;
			elif (root.left):
				pass;
			else:
				del root;
		else:
			current_dim = root.level % self.dim;
			if (item [current_dim] < root.item [current_dim]):
				self.delete (root.left, item);
			else:
				self.delete (root.right, item);

	def describe (self):
		print ('Array: ', self.array);
		print ('Root: ', self.root.item);

if (__name__ == '__main__'):
	array, dim = [(3,6),(17,15),(13,15),(6,12),(9,1),(2,7)], 2;
	myTree = KDTree (dim, array);
	
	myTree.insert (myTree.root, (10, 19));
	myTree.describe ();
	print (myTree.find_min (myTree.root, 1));
