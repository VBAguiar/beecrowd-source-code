#include <iostream>

using namespace std;

int main() {
	int max = 0;
	int num = 0;
	
	cin >> max;
	while (true) {
		if (num % 2 != 0) {
			cout << num << endl;
		}

		num += 1;
		if (num > max) {
			break;
		}
	}
	return 0;
}
