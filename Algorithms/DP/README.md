# Dynamic Programming

| Content                                           |
| :------------------------------------------------ |
| [Definition](#definition)                         |
| [Types of DP Approaches](#types-of-dp-approaches) |
| [Problems](#problems)                             |

## Definition

Dynamic Programming is an optimization technique used to solve complex problems by breaking them down into smaller subproblem. The solutions to subproblem are stored to avoid redundant calculations, making the approach efficient.

### Key Characteristics

1. **Overlapping Subproblem**: Subproblem are solved multiple times.
2. **Optimal Substructure**: The solution to the problem can be constructed from solutions to subproblem.
3. **Memoization**: It is a technique of storing the results of expensive function calls and reusing them when the same inputs occur again.
4. **Tabulation**: It is a technique of filling a table with the results of all possible subproblem in a bottom-up manner.

### Steps to Solve a DP Problem

1. Identify if the problem has overlapping subproblem and optimal substructure.
2. Define the state (DP array or table).
3. Derive the recurrence relation.
4. Base case initialization.
5. Iterative computation or recursive approach with memoization.
6. Retrieve the result from the DP table.

Readings:

- [What Is Dynamic Programming and How To Use It](https://www.youtube.com/watch?v=vYquumk4nWw&t=740s)
- [Dynamic Programming](https://www.w3schools.com/dsa/dsa_ref_dynamic_programming.php)

## Types of DP Approaches

1. **Top-Down (Memoization)**:
   - Solves the problem recursively.
   - Stores results of subproblem to avoid recomputation.
2. **Bottom-Up (Tabulation)**:
   - Solves the problem iteratively.
   - Uses a table to store intermediate results.

Readings:

- [Memoization](https://www.w3schools.com/dsa/dsa_ref_memoization.php)
- [Tabulation](https://www.w3schools.com/dsa/dsa_ref_tabulation.php)

### Example

**Fibonacci Numbers**: The Fibonacci sequence is a classic example that demonstrates the power of dynamic programming. The sequence is defined as follows:

- $F(0) = 0$
- $F(1) = 1$
- $F(n) = F(n-1) + F(n-2), \text{for } n > 1$

A naive recursive implementation to find the nth Fibonacci number would involve a lot of redundant calculations. For instance, to calculate $F(5)$, we would need to calculate $F(4)$ and $F(3)$. But calculating $F(4)$ would again require calculating $F(3)$, leading to redundant computations.

```python
def fibonacci(n):
    if n <= 1:  # Base cases: F(0) = 0, F(1) = 1
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive calls
```

Here’s how we can use dynamic programming to optimize this:

**Top-Down (Memoization)**

```python
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

print(fib(10))  # Output: 55
```

**Tabulation (Bottom-Up Approach)**

```python
def fib(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print(fib(10))  # Output: 55
```

## Problems
