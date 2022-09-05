#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

const double PI = 3.14159;
double raio = 0;

double A(double raio) {
	long double area = PI * pow(raio, 2);
	return area;
}

int main() { 
	cin >> raio;
	double area = A(raio);
	cout << "A=" << fixed << setprecision(4) << area << endl;
	return 0;
}
