###############################################################################################################
#Construct a Segment Tree
###############################################################################################################

def seg_tree (array, pos):
	l_child, r_child = ((pos + 1) * 2) - 1, (pos + 1) * 2;

	if (array [l_child] == None):
		print ('.');
		seg_tree (array, l_child);
	if (array [r_child] == None):
		print ('.');
		seg_tree (array, r_child);
	array [pos] = array [l_child] + array [r_child];

user_array = [int (i) for i in input ().split ()];
array = [None for i in range (len (user_array) - 1)] + user_array;

#sample call to seg_tree ()
seg_tree (array, 0);
print (array);
