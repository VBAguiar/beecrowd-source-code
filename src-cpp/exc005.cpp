#include <iostream>

using namespace std;

int main() {
	int cont = 1;
	int contnums = 0;
	while (true) {
		double num;
		cin >> num;
		if (num > 0) {
			++contnums;
		}
		
		if (cont >= 6) {
			break;
		}
		
		cont+=1;
	}
	cout << contnums << " valores positivos" << endl;
	return 0;
}
