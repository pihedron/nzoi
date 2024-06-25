#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int N, M, V_A, V_B;
vector<pair<int, int>> common;

bool versions_match(int (&A)[V_A][N], int (&B)[V_A][N], int i, int j)
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

pair<int, int> find_latest_version(int (&A)[V_A][N], int (&B)[V_A][N])
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
} 

int main()
{
  cin >> N >> M >> V_A >> V_B;

  int A_deps[N];
  int B_deps[M];

  for (int a = 0; a < N; a++)
  {
    cin >> A_deps[a];
  }

  for (int b = 0; b < M; b++)
  {
    cin >> B_deps[b];
  }

  int A[V_A][N];
  int B[V_B][M];

  for (int i = 0; i < V_A; i++)
  {
    for (int a = 0; a < N; a++)
    {
      cin >> A[i][a];
    }
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

  v_a = find_latest_version(A, B).first;
  v_b = find_latest_version(A, B).second;

  cout << v_a << " " << v_b << endl;
  return 0;
}