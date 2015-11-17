/*
	Construct a Segment Tree
	NOTE: This is just a temporary solution (and not a very good one, a better implementation using boost::variant is on its way.
	It is not a good one because the user can store any number in their vector array except -1, because that value signifies that that element of the array is empty and needs to be filled.
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void print_elem (int& elem) { cout << elem << '\t'; }
void seg_tree (vector< int >& array, int pos) {
	int l_child (((pos + 1) * 2) - 1), r_child ((pos + 1) * 2);

	if (array [l_child] == -1) {
		seg_tree (array, l_child);
	}
	if (array [r_child] == -1) {
		seg_tree (array, r_child);
	}
	array [pos] = array [l_child] + array [r_child];
}

int main () {
	int size (0);
	cin >> size;

	vector< int > array (2*size - 1, -1);
	for (int i = size - 1; i < array.size (); i++) { cin >> array [i]; }

	/* sample call to seg_tree () function for construction */
	seg_tree (array, 0);

	for_each (array.begin (), array.end (), print_elem);
	cout << endl;
	return (0);
}
