#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
  vector<int> piles;
  int N;
  cin >> N;
  for (int i = 0; i < N; i++)
  {
    int num;
    cin >> num;
    int index = distance(piles.begin(), lower_bound(piles.begin(), piles.end(), num));
    if (index < piles.size())
    {
      piles[index] = num;
    }
    else
    {
      piles.push_back(num);
    }
  }
  cout << piles.size();
  return 0;
}