#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
  int N, X, M;
  cin >> N >> X >> M;

  int k[N];
  for (int i = 0; i < N; i++)
  {
    cin >> k[i];
  }

  int h[M];
  int d[M];
  for (int j = 0; j < M; j++)
  {
    cin >> h[j] >> d[j];
    h[j]--;
    d[j] /= X;
  }

  vector<int> adj[M];
  for (int j = 0; j < M; j++)
  {
    for (int i = 0; i < N; i++)
    {
      if (k[i] == 0)
      {
        continue;
      }
      if (abs(h[j] - i) <= d[j])
      {
        adj[j].push_back(i);
      }
    }
  }

  int sum = 0;
  for (int i = 0; i < N; i++)
  {
    sum += k[i];
  }

  int p[M];
  for (int j = 0; j < M; j++)
  {
    p[j] = j;
  }

  sort(p, p + M, [&](int j1, int j2)
  {
    return adj[j1].size() < adj[j2].size();
  });

  bool trivial = sum >= M;

  for (int j : p)
  {
    if (!trivial)
    {
      break;
    }
    trivial = false;
    for (int i : adj[j])
    {
      if (k[i] == 0)
      {
        continue;
      }
      trivial = true;
      k[i]--;
      h[j] = i;
      break;
    }
  }

  if (trivial)
  {
    cout << "SOLUTION IS TRIVIAL" << endl;
    for (int i : h)
    {
      cout << i + 1 << endl;
    }
  }
  else
  {
    cout << "SOLUTION IS NON-TRIVIAL";
  }
}