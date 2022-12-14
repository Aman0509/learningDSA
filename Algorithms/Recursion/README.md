# Recursion

## What is Recursion?

Recursion is a way of solving a problem by having a function calling itself.

```
def recursionMethod (parameters):
    if exit from condition satisfied:
        return some value
    else:
        recursionMethod (modified parameters)
```
    

- Performing the same operation multiple times with different inputs.

- In every step, we try smaller inputs to make the problem smaller.

- Base condition is needed to stop the recursion, otherwise infinite loop will occur.

> Importance of base condition
>
> A programmer's wife tells him as he leaves the house: "While you're out, buy some milk." He never returns home and the universe runs out of milk. :rofl::rofl::rofl:

## Why do we need Recursion?

- Recursion is made for solving problems that can be broken down into smaller, repetitive problems. It is especially good for working on things that have many possible branches and are too complex for an iterative approach.

- Using recursion makes the code clearer.

- The prominent usage of recursion in data structures like Trees and Graphs.

- It is used in many algorithms (Divide and Conquer, Greedy and Dynamic Programming).

## How to write Recursion in 3 steps?

Let's take the example of finding factorial.

**Step 1: Recursive case - the flow**

```
n! = n * (n-1) * (n-2) * ... * 2 * 1

(n-1)! = (n-1) * (n-1-1) * (n-1-2) * ... * 2 * 1 = (n-1) * (n-2) * ... * 2 * 1
```

So, the Recursive case can be `n! = n * (n-1)!`, both left & right side we have factorials, which means we can call the function recursively.

**Step 2: Base case - the stopping criterion**

In case of factorial of any number, base condition would be:

```
0! = 1
1! = 1
```

**Step 3: Unintentional case - the constraint**

As factorial of decimals or negative integers can't be calculated, we need to handle it.

```
factorial(-1) ??
factorial(1.5) ??
```

After following all the above 3 steps, our code will look like below:

```
def factorial(n):
    assert n >= 0 and int(n) == n, 'The number must be positive integer only!'
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)
```

Let's follow the similar approach and write steps for Fibonacci Numbers

**Step 1: Recursive case - the flow**

```
f(n) = f(n-1) + f(n-2)
```

**Step 2: Base case - the stopping criterion**

```
0 & 1
```

**Step 3: Unintentional case - the constraint**

```
fibonacci(-1) ??
fibonacci(1.5) ??
```

After following all the above 3 steps, our code will look like below:

```
def fibonacci(n):
    assert n >=0 and int(n) == n, "Fibonacci number cannot be negative number or non integer
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

To learn more about Recursion, follow below links:

- [Recursion - GeeksForGeeks](https://www.geeksforgeeks.org/learn-data-structures-and-algorithms-dsa-tutorial/#recursion)

- [Fundamentals of Recursion in Programming - Enjoy Algorithms](https://www.enjoyalgorithms.com/blog/recursion-explained-how-recursion-works-in-programming)

- [Analysis of Recursion in Programming - AfterAcademy](https://afteracademy.com/blog/analysis-of-recursion-in-programming/#:~:text=The%20number%20of%20levels%20in,tree%20is%20log2(N).&text=The%20cost%20at%20the%20last,number%20of%20subproblems%20is%20N.&text=The%20time%20complexity%20of%20the%20above,is%20O(N%20logN))

- [The Handshake Problem](http://mason.gmu.edu/~jsuh4/impact/Handshake_Problem%20teaching.pdf)

## Problems

1. [Sum of digits of a number using recursion](Problems/sum_of_digits.py)
2. [Power of given number using recursion](Problems/power_of_num.py)
3. [GCD of two given numbers using recursion](Problems/gcd.py)