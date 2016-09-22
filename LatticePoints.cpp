#include <iostream>

using namespace std;

int main()
{
	int n;
	cin >> n;
	int bound = n+1;
	int count = 0;

	for (int i=-bound; i<bound; i++) {
		for (int j=-bound; j<bound; j++) {
			if (i*i + j*j <= n*n) {
				count++;
			}
		}
	}
	cout << count;

	system("pause");
	return 0;
}