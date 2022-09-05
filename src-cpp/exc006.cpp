#include <iostream>
#include <iomanip>

using namespace std;

int main() {
	int numcont = 0;
	int c = 0;
	double total = 0;
	
	while (true) {
		double num = 0;
		cin >> num;
		if (num >= 0) {
			++numcont;
			total += num;
		}
		++c;
		if (c >= 6) {
			break;
		}
	}
	cout << numcont << " valores positivos" << endl;
	cout << fixed << setprecision(1)  << total/numcont << endl; 
	return 0;
}
