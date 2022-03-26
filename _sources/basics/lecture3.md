# Lecture 3: Set and Sorting

## Set Interface

| Type      | Function       | Note                                                   |
| --------- | -------------- | ------------------------------------------------------ |
| Container | `build(x)`     | given an iterable $x$, build set from items in $x$     |
| --        | `len(x)`       | return the number of stored values                     |
| Static    | `find(k)`      | return the stored item with key $k                     |
| Dynamic   | `insert(x)`    | add $x$ to set                                         |
| --        | `delete(k)`    | remove and return the stored item with key $k$         |
| Order     | `iter_ord()`   | return the stored items one-by-one in key order        |
| --        | `find_min()`   | return the item with smallest key                      |
| --        | `find_max()`   | return the item with largest key                       |
| --        | `find_next(k)` | return the item with smallest key larger than $k$      |
| --        | `find_prev(k)` | return the stored item with largest key smaller than k |

- storing items in an array in arbitrary order can implement a (`not so efficient`) set
- stored items sorted increasing by key allows:
  - faster find min/max (at first/last index of array)
  - faster find via binary search: $O(logn)$
- how to construct a sorted array?

! **Confused**: set and sequence are two types of interface. So `array` as a data structure can have both interfaces?

## Sorting

- given a sorted array, we can leverage binary search to make an efficient set data structure
- input: `static array` $A$ of $n$ numbers
- output: `static array` $B$ of which is a sorted permutation of $A$
- example: [8,2,4,9,3] -> [2,3,4,8,9]
  
## Permutation Sort

- there are $n!$ permuations of $A$, at least one of which is sorted
- for each permutation, check wether sorted, $\Theta(n)$ time

```python
def permutation_sort(A):
    '''Sort A'''
    for B in permutations(A):               # O(n!)
        if is_sorted(B):                    # O(n)
return B                                    # O(1)
```

- `permulation_sort` analysis:
  - try all possibilities - brute force
  - running time $O(n!*n)$, which is `exponential`

## Recurrences

- substitution:
- recurrence tree: draw a tree representing the recursive calls and sum computation at nodes
- master theorem:

## Selection Sort
- select the smallest (forward from 0 to n)/greatest (reverse from n to 0) element from the remaining elements and place it a the correct position
- forward
  - find a smallest number in the remaining array $A[i:]$ and swap it to $A[i]$
  - example: [8,2,4,9,3] -> [2,8,4,9,3] -> [2,3,4,9,8] -> [2,3,4,9,8] -> [2,3,4,8,9]
- reverse
  - find a largest number in prefix $A[:i+1]$ and swap it to $A[i]$
  - recursively sort prefix $A[:i]$
  - example: [8,2,4,9,3] -> [8,2,4,3,9] -> [3,2,4,8,9] -> [3,2,4,8,9] -> [2,3,4,8,9]

```python
def selection_sort(A, i = None):            # T(i)
    '''Sort A[:i + 1]'''                
    if i is None: i = len(A) - 1            # O(1)
    if i > 0:                               # O(1)
        j = prefix_max(A, i)                # O()
        A[i], A[j] = A[j], A[i]             # O(1)
        selection_sort(A, i - 1)            # T(i-1)

def prefix_max(A, i):                       # S(i)
    ''' Return index of maximum in A[:i+1]'''
    if i > 0:                               # O(1)
        j = prefix_max(A, i - 1)            # S(i-1)
        if A[i] < A[j]:                     # O(1)
            return j                        # O(1)
    return i                                # O(1)
```

- `prefix_max` analysis:
  - idea: 
    - for an array $A$, with prefix $i$, the maximum of $A[:i+1]$ is either $A[i]$ or the maximum of $A[:i]$.
    - recursion
  - Induction: assume correct for $i$, maximum is either $A[i]$ or the maximum of $A[:i]$, returns correct index in either case.
  - $S(1) = O(1), S(n) = S(n-1) + O(1)$
    - substitution: $S(n) = O(n)$
    - recurrence tree


- `selection_sort` analysis:
  - idea:
    - recursively find the largest number in the prefix $A[:i+1], i = n, n-1, ..., 0$

## Insertion Sort
- build the final sorted array one item at a time by inserting the element into a particular position and shifting the remaining element. A good animation can be found at https://en.wikipedia.org/wiki/Insertion_sort.

- procedure using recursion 
  - assume we have an array $A[:i+1]$, with the sorted prefix $A[:i]$, and the element $A[i]$, 
  - compare $A[i-1]$ and $A[i]$. 
    - if $A[i] >= A[i-1]$, then move forward the pointer $i$ by 1 and repeat the loop 
    - else swap $A[i]$ with $A[i-1]$, and using the same `insert_sort` procedure to sort $A[:i-1]$. This is necessary because the swapping will lead a unsorted $A[:i]$, See the last step in the following example.
  
      ``` python
      [2, 9, 8, 4] -> [2, 9, 8, 4] -> [2, 8, 9, 4] -> [2, 4, 8, 9] 
      ```
        The last step internally proceeds as follows:
      ```python
      [2, 8, 9, 4] -> [2, 8, 4, 9] -> [2, 4, 8, 9]
      ```
      
```python
def insert_last(A, i):
    '''Sort A[:i+1] assuming sorted A[:i]'''
    if i > 0 and A[i] < A[i-1]:
        A[i-1], A[i] = A[i], A[i-1]
        insert_last(A, i-1)
    return A

def insert_sort(A, i):
    '''Sort A[:i+1]'''
    if i > 0:
        insert_sort(A, i-1)
        insert_last(A, i)
    return A

print(insert_last([2, 8, 9, 3], 3)) -> [2, 3, 8, 9]
print(insert_sort([2, 8, 9, 3], 3)) -> [2, 3, 8, 9]

print(insert_last([2, 9, 8, 3], 3)) -> [2, 3, 9, 8]
print(insert_sort([2, 9, 8, 3], 3)) -> [2, 3, 8, 9]
```

- `insert_last` analysis
  - base case: for $i=0$, array has one element so is sorted.
  - induction: assume correct for $i$, if $A[i] > A[i-1]$, array is sorted. Otherwise swapping the last two elements allows up to sort $A[:i]$ by induction.
  - $S(1) = O(1),S(n)=S(n-1)+O(1), S(n)=O(n)$

- `insert_sort` analysi
  - base case: for $i=0$, arrya has one element so is sorted
  - induction: assume correct for $i$, algorithm sorts $A[:i]$ by induction, and then `insert_last` correctly sorts the rest as proved before
  - $T(1)=O(1), T(n) = T(n-1) + S(n) = T(n-1) + O(n) \rArr T(n)=O(n^2)$  

## Merge Sort

- recursively sort first half and second half
- merge sorted halves into one sorted list (two-pointer algorithm)
- example: $[7,1,5,6,2,4,9,3] \rArr [1,7,5,6,2,4,3,9] \rArr [1,5,6,7,2,3,4,9] \rArr [1,2,3,4,5,6,7,9]$

```python
def merge(L, R, A, i, j, a, b):
    '''Merge sorted L[:i] and R[:j] into A[a:b] using two-pointer algorithm'''
    if a < b:
        if (j <= 0) or (i > 0 and L[i-1] > R[j-1]):
            A[b-1] = L[i-1]
            i = i - 1
        else:
            A[b-1] = R[j-1]
            j = j -1
        merge(L, R, A, i, j, a, b-1)

def merge_sort(A, a , b):
    '''Sort A[a:b]'''
    a = 0 
    b = len(A)
    if 1 < b - a:
        c = (a + b + 1) // 2
        merge_sort(A, a, c)
        merge_sort(A, c, b)
        L, R = A[a:c], A[c:b]
        merge(L, R, A, len(L), len(R), a, b)
```

## Summary

- `insertion_sort`, `selection_sort`, `merge_sort` requires $O(n^2), O(n^2), O(nlogn)$ time on arrays. They may have different time complexity for other data strucutures, which depends on the operations of `get`, `set` and `compare`.
  - `insertion_sort` requires $O(n^2)$ times of `get`, `set`, and `compare`. Static operations in arrays are $O(1)$ time, so this sorting on arrays uses $O(n^2)$ time.
  - `selection_sort` requires $O(n^2)$ times of `get` and `compare`, and $O(n)$ times of `set`. So this sorting on arrays uses $O(n^2)$ time.
  - `merge_sort` requires $O(nlogn)$ times of `get`, `set` and `compare`. So this sorting on arrays uses $O(nlogn)$ time.
  - `insert_sort` and `selection_sort` are in-place sorting, which doesnt require additional space. `merge_sort` requires additional $O(n)$ space to merge two sorted sub-arrays.
