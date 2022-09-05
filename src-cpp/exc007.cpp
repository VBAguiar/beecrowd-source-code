#include <iostream>

using namespace std;

int main() {
	int x, y;
	int i, c;
	cin >> x; cin >> y;
	for (i=x; i<=y; i++) {
		if (i/13 != 0 and i != 201) {
			c += i;
		}
	}
	cout << c; 
	return 0;
}
