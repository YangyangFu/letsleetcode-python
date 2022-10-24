# Lecture 1: Introduction

## Algorithm

- Procedure mapping each input to a single output (deterministic)
- Algorithm solves a problem if it returns a correct output for every problem input
- Examples: An algorithm tp solve birthday matching
    - maintain a record of names and birthdays
    - interview each student in some order
        - if birthday exists in record, return found pairs
        - else add name and birthday to record
    - return none if last student inteviewed without success

## Correctness

- Induction: recursion for arbitrarily large inputs
- Example: proof of correctness of birthday matching lagorithm
    - induct on $k$: the number of student in the record
    - Hypothesis; if first $k$ contain match, return match before interviewing student $k+1$
    - Base case: $k=0$, first $k$ contains no match
    - Assume for induction hypothesis holds for $k=k'$, and consider $k=k'+1$.
    - If first $k'$ contains a match, already returned a match by induction
    - Else first $k'$ do not have match, so if first $k' + 1$ has match, match contains $k'+1$
    - Then algoithm checks directly whether birday of student $k'+1$ exists in first $k'$.

## Efficiency

- How fast does an algorithm produce a correct output?
    - Could measure time, but want performance to ne machine independent.
    - *Idea!!!* count number of fixed-time operations algorithm takes to return - asympototic 
    - Expect to depend on the size of input: larger input suggests longer time
    - Efficient if returns in `polynomial time` with respect to input
    - Sometimes no efficient algorithm exists for a problem: `L20`

- Asympototic Notation: ignore constant factors and lower order terms
    - upper bounds $O$, lower bounds $\Omega$, tight bounds $\Theta$
    - $O(1), O(logn), O(n), O(nlogn), O(n^2), O(n^c), O(2^n)$

## Model of Computation

- specification for what operations on the machine can be performed in $O(1)$ time
- Model in this class is called the `Word-RAM`
- Machine word: block of $w$ bits ($w$ is the word size of a $w$-bit Word-RAM)
- Memory: addressable sequence of machine words
- Processor supports many constant time operation on a $O(1)$ number of words (integers):
    - integer arithmetic: (+, -, *, //, %)
    - logical operators: (&&, ||, !, ==, <, >, <=, >=)
    - given word $a$, can read work at address $a$, write word to address $a$
- Memory address must be able to access every place in memory
    - Requirement: $w \ge$ # bits represent the largest memory address,e.g., $log_2n$
    - 32-bit words -> max ~ 4 GB memory, 64-bit words -> max ~ 16 exabytes of memory

In order to precisely calculate the resources used by an algorithm, we need to model how long a computer takes to perform basic operations. 
Specifying such a set of operations provides a model of computation upon which we can base our analysis. 
In this class, we will use the w-bit Word- RAM model of computation, which models a computer as a random access array of machine words called memory, together with a processor that can perform operations on the memory. 
A machine word is a sequence of $w$ bits representing an integer from the set $\{0, . . . , 2^w − 1\}$. 
A `Word-RAM` processor can perform basic binary operations on two machine words in constant time, including addition, subtraction, multiplication, integer division, modulo, bitwise operations, and binary comparisons. 
In addition, given a word $a$, the processor can read or write the word in memory located at address $a$ in constant time. 
If a machine word contains only $w$ bits, the processor will only be able to read and write from at most $2^w$ addresses in memory. So when solving a problem on an input stored in $n$ machine words, we will always assume our `Word-RAM` has a word size of at least $w > log_2 n$ bits, or else the machine would not be able to access all of the input in memory. To put this limitation in perspective, a `Word-RAM` model of a byte-addressable 64-bit machine allows inputs up to `∼ 1010 GB` in size.
