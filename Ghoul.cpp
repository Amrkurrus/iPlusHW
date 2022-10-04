#include <iostream>
#include <Windows.h>
using namespace std;

int main()
{
	setlocale(LC_ALL, "Russian");

	string text = "?    LET ME DIE!!! I don't really know what the point in life is everybody knows that we won't survive...";

	for (int i = 100; i > 0; i--)
	{
		cout << "Я..." << endl;
		Sleep(5);
	}

	for (int g = 100; g > 0; g--)
	{
		cout << "Гуль!!!" << endl;
		Sleep(5);
	}

	for (int num = 1000; num > 0; num -= 7)
	{
		cout << num << " - 7 = " << num - 7 << text << endl;
		Sleep(50);

	}

	cin.get();
	return 0;
}