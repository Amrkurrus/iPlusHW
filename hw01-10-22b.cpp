#include <iostream>
#include <cmath>
using namespace std;

int main() {
	int x, y;
	float sol;
	cin >> x >> y;
	sol = (fabs(x)) - fabs(y) / (1 + fabs(x * y));
	cout << sol;
}
