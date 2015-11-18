class Node:
	def __init__ (self):
		self.children = {};

	def insert (self, key):
		self.children [key] = Node ();

	def successors (self):
		return (self.children);

	def get_child (self, key):
		return (self.children [key]);

class Trie:
	def __init__ (self):
		self.root = Node ();

	def get_root (self):
		return (self.root);

	def insert (self, current_node, string, start_pos = 0):
		if (start_pos == len (string)):
			return;

		if (not (string [start_pos] in current_node.successors ())):
			current_node.insert (string [start_pos]);

		self.insert (current_node.get_child (string [start_pos]), string, start_pos + 1);

	def search (self, current_node, string, start_pos = 0):
		if (string [start_pos] in current_node.successors ()):
			return (True if (start_pos == len (string) - 1) else self.search (current_node.get_child (string [start_pos]), string, start_pos + 1));
		return (False);

	def describe (self):
		#needs to be written
		pass;

if (__name__ ==  '__main__'):
	myT = Trie ();
	myT.insert (myT.get_root (), input ());
	print (myT.search (myT.get_root (), input ()));
#	myT.describe ();
