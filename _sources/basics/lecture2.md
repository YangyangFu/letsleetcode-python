# Lecture 2: Data Structure and Dynamic Array

## Data Structure vs Interfaces
- data structure 
    - A data structure is a way to store data, with algorithms that support operations on the data
    - 2 main data structure: **array based** and **pointer based**
- interfaces
    - Collection of supported operations is called an interface (also API or ADT)
    - Interface is a specification: what operations are supported (the problem!)
    - 2 main interfaces: sequence and set

## Interfaces

- Sequence interface -> maintain a sequence of items such as $x_0, x_1, ..., x_n$ subject to these operations:
    - Container
        - `build(x)` - make a new DS
        - `len()` - return n
    - Static
        - `iter_seq` - main the sequence order
        - `get_at(i)` - return $x_i$
        - `set_at(i, x)` - set $x_i$
    - Dynamic
        - `insert_at(i,x)` 
        - `delete_at(i)`
        - `insert_first(x)`
        - `insert_last(x)`
        - `delete_first()`
        - `delete_last()`


- Set interface -> future lectures

## Static Array Sequence
- Static array -> python has no static array, only dynamic array.
    - word RAM -> model of computation
        - memory: array of $w$-bits of words
        - array: consecutive chunk of memory
        - array[i] = memeory[address[array]+i]
        - array access in $O(1)$ time
    - the size of static arrary is fixed
    - $O(1)$ per `get_at`, `set_at`, `len`
    - $O(n)$ per `build`, `iter_seq`
    - Memory Allocation Model: allocate array of size n in $\Theta (n)$ time
        - The above constant time operations assumes $w \ge log(n)$
    - Apply dynamic sequence interface to static array:
        - `insert/delete_at()` cost $\Theta(n)$ time, the same holds for `insert/delete_last`.
            - shift all ites after the modified item
            - allocate a new array and throw away the old one
        - not efficient for dynamic operations


## Dynamic Array Sequence
- Dynamic Arrays; e.g., List in Python
    - make an array efficient for `insert/delete_last` dynamic operations
    - Ideas: allocate extra space so reallocation doesn't occur with every dynamic operation
        - relax the constraints size(array) = n <- # of items in the sequences
        - enforce the size of array=$\Theta (n)$ -> $\ge n$, which means the size of array is greater than its length
        - maitain $A[i] = x_i$
        - `insert_last` can be run in $O(1)$ time with extra space 
        ``` python
            A[len] = x, len +=1
        ```
    - fill ratio: $1 \le r \le 1$ the ratio of items to space. If the size of array is $n$, with fill ratio, it will take $n/r$ space instead of $n$ as in static array.
    - whenever the array is full ($r=1$), allocate $\Theta(n)$ extra space at the end to fill ratio $r_i$ (e.g., 1/2)
    - will have to insert $\Theta(n)$ items before the size is full and the next reallocation
    - example
        - allocate a new array of 2*size
            - why not size + 5
        - n `insert_last` from an empty array
            - resize at n = 1, 2, 4, 8, 16, ...
            - resize cost: $\Theta(1+2+4+8+16+,..., logn) = \Theta(2^(logn)) = \Theta(n)$
    - time complexity
        - a single operation take $\Theta(n)$ time for reallocation
        - however, any sequence of $\Theta(n)$ operations takes $\Theta(n)$ time
        - so each operation takes $\Theta(1)$ time "on average"
        - see "Amortized Analysis"
    
- Dynamic array deletion
    - delete from the back? $\Theta(1)$ time 
    - however, wasteful in space. Want size of the data structure to stay $\Theta(n)$.

## Linked List Sequence
- Linked List
    - pointer-based: pointer is the index for the memeory arrays
    - Each item stored in a node which contains a pointer to the next node in sequence 
    - Each node has two fields: `node.item` and `node.next`
    - Can manipulate nodes simply by relinking pointers!
    - Maintain pointers to the first node in sequence (called the `head`)
    - Appy dynamic sequence interface to linked list
        - `insert/delete_first`: very efficient in $\Theta(1)$ time
        - accessing the `i`th item needs follow the next $i$ pointers `i` times
            - `get_at(i)` or `set_at(i)`: $\Theta(i)$ time, and the worst scenario is $\Theta(n)$
        - `insert_last`: $O(n)$
            - how to improve: 
                - add a `tail` pointer at the front -> $O(1)$
                - `double linked list`

## Amortized Analysis
- Data structure analysis technique to distribute cost over many operations
- Operation has amortized cost $T (n)$ if $k$ operations cost at most $≤ kT (n)$ 
- “T (n) amortized” roughly means $T (n)$ “on average” over many operations 
- Inserting into a dynamic array takes $Θ(1)$ **amortized** time

