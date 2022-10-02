#include <iostream>
#include <cmath>
using namespace std;

int main() {
	float x, y, sol;
	cin >> x >> y;
	sol = (abs(x)) - abs(y) / (1 + abs(x * y));
	cout << sol;
}