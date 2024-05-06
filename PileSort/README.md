# Problem

Mr Pile has just written an exceptionally long report on his latest findings - up to thousands of pages long. Unfortunately, on retrieving the document from the printers, he dropped the report on the floor. Quickly, he gathered all the pages together, but now they are out of order.

He needs help to sort N pages. However, he decides that he will only handle each page twice:

When he first picks up each page, he places it on top of one of K piles.
After all the pages are in the K piles, he picks up each page in order, from page 1 to page N.
Naturally, a page can only be picked up if it is on the top. Therefore, a higher numbered page cannot be placed on top of a lower numbered page in a pile.

Your job is to find out the minimum number of piles K so that Mr Pile can sort all the pages.

## Input
The first line will contain a single integer N (1≤100,000).

The second line will have N space-separated integers, the page numbers in the order that Mr Pile first places them on top of one of the K piles.

## Output
On a single line, print a single integer, the minimum possible K.

## Subtasks
Subtask 1 (20%), N≤20
Subtask 2 (40%), N≤1000
Subtask 3 (40%), no further constraints apply
Explanation
In the first example, 4 piles are required. The pages can be sorted by placing page 1 in the first pile, page 2 in the second pile, pages 4 and 6 in the third pile, and pages 3 and 5 in the fourth pile. Note that page 2 cannot be placed in the same pile as page 1 because otherwise, Mr Pile wouldn't be able to pick up page 1 before page 2.

## Sample Input 1
```
6
1 2 6 4 5 3
```
## Sample Output 1
```
4
```

# Solution

> ![WARNING]
> The Python solution for this problem is not memory efficient enough to pass the last subtask of this problem.

This problem can be broken down into 4 steps:
- iterate over each page number
- store the index of the pile where the top page has **lowest** number in the list of piles that is **greater** than the current page number
- if the current page is **greater** than all the top pages in the pile (index outside range): create a new pile
- else: place the current page on top of the pile at the index

Whenever Mr Pile encounters a pile, he can only place the current page on the pile if the current page has a page number **less** than the top page. Otherwise, he needs to make a new pile. This makes sure that each pile will always be individually sorted in reverse order.

An important detail to remember is that only the **top page number** matters because it is the only page number that the current page number is checked against. This means we do not have to store the whole stack of pages in the list of piles. Instead, we can save memory by only storing the top page number.

```py
N = int(input())
piles = []

for num in list(map(int, input().split())):
    index = len(piles)
    min_pile = 10 ** 6 # custom infinity
    for j in range(len(piles)):
        if num < piles[j]:
            if piles[j] < min_pile:
                min_pile = piles[j]
                index = j
    if index < len(piles):
        piles[index] = num
    else:
        piles.append(num)

print(len(piles))
```

The code above works but it is **time inefficient**. This is because we are performing a linear search on a list that is always going to be sorted. We can improve the time complexity of that loop from `O(n)` to `O(log n)` by replacing the linear search with binary search. In python, using `bisect.bisect_left` is quicker than making our own binary search function.

```py
import bisect

N = int(input())
piles = []

for num in list(map(int, input().split())):
    index = bisect.bisect_left(piles, num)
    if index < len(piles):
        piles[index] = num
    else:
        piles.append(num)

print(len(piles))
```

Everything is working well, but this code exceeds the memory limit on the last subtask. This is because Python is an interpreted language, but we can fix this issue by rewriting it in C++. The C++ solution is just as simple as the Python one.

```cpp
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
```