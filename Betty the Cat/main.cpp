#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int P;
    cin >> P;
    int A[4]{0};
    int B[4]{0};
    for (int i = 1; i <= P; i++)
    {
        int v;
        cin >> v;
        B[0] = *max_element(A, A + 4);
        for (int j = 1; j < 4; j++)
        {
            if (i >= j) B[j] = A[j - 1] + v;
        }
        swap(A, B);
    }
    cout << *max_element(A, A + 4);
}