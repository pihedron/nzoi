#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int N, M, V_A, V_B;
vector<pair<int, int>> common;

bool versions_match(vector<vector<int>> &A, vector<vector<int>> &B, int i, int j)
{
  for (auto [a, b] : common)
  {
    if (A[i][a] != B[j][b])
    {
      return false;
    }
  }
  return true;
}

pair<int, int> find_latest_version(vector<vector<int>> &A, vector<vector<int>> &B)
{
  for (int i = V_A - 1; i >= 0; i--)
  {
    for (int j = V_B - 1; j >= 0; j--)
    {
      if (versions_match(A, B, i, j))
      {
        return {i, j};
      }
    }
  }
  return {-1, -1};
} 

int main()
{
  cin >> N >> M >> V_A >> V_B;

  string A_deps[N];
  string B_deps[M];

  vector<vector<int>> A(V_A, vector<int>(N));
  vector<vector<int>> B(V_B, vector<int>(M));

  for (int a = 0; a < N; a++)
  {
    cin >> A_deps[a];
  }

  for (int i = 0; i < V_A; i++)
  {
    for (int a = 0; a < N; a++)
    {
      cin >> A[i][a];
    }
  }

  for (int b = 0; b < M; b++)
  {
    cin >> B_deps[b];
  }

  for (int j = 0; j < V_B; j++)
  {
    for (int b = 0; b < M; b++)
    {
      cin >> B[j][b];
    }
  }

  int v_a;
  int v_b;

  for (int a = 0; a < N; a++)
  {
    for (int b = 0; b < M; b++)
    {
      if (A_deps[a] == B_deps[b])
      {
        common.push_back({a, b});
      }
    }
  }

  pair<int, int> v = find_latest_version(A, B);

  cout << v.first << " " << v.second << endl;
  return 0;
}