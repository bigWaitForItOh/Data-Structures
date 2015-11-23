#################################################################################################################
#Implementation of Trie Data Structure that supports insert ()-ing, search ()-ing and delete ()-ing a string
#################################################################################################################

class Node:
	def __init__ (self):
		self.children = {};

	def insert (self, key):
		self.children [key] = Node ();

	def insert_sentinal (self, value):
		self.children [-1] = value;

	def successors (self):
		return (self.children);

	def get_child (self, key):
		return (self.children [key]);

	def get_value (self):
		return (self.children [-1] if -1 in self.children else None);

class Trie:
	def __init__ (self):
		self.root = Node ();

	def get_root (self):
		return (self.root);

	def insert (self, current_node, string, value, start_pos = 0):
		if (start_pos == len (string)):
			current_node.insert_sentinal (value);
			return;

		if (not (string [start_pos] in current_node.successors ())):
			current_node.insert (string [start_pos]);

		self.insert (current_node.get_child (string [start_pos]), string, value, start_pos + 1);

	def search (self, current_node, string, start_pos = 0):
		if (string [start_pos] in current_node.successors ()):
			if (start_pos == len (string) - 1):
				return (current_node.get_child (string [start_pos]).get_value ());
			return (self.search (current_node.get_child (string [start_pos]), string, start_pos + 1));
		return (None);

	def delete (self, string):
		#needs to be written
		pass;

	def describe (self):
		#needs to be written
		pass;

if (__name__ ==  '__main__'):
	data = [ ('Stuxnet', 2010), ('Shellshock', 2014), ('Morris', 1988), ('Heartbleed', 2014) ];
	myT = Trie ();

	for pair in data: myT.insert (myT.get_root (), pair [0], pair [1]);
	print (myT.search (myT.get_root (), input ()));
#	myT.describe ();
