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