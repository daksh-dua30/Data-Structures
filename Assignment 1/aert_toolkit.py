# AERT - Algorithmic Efficiency & Recursion Toolkit
# Unit 1 Assignment - Data Structures


# STACK ADT


class StackADT:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# FACTORIAL (Recursive)


def factorial(n):
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# FIBONACCI (Naive Recursive)


fib_naive_calls = 0


def fib_naive(n):
    global fib_naive_calls
    fib_naive_calls += 1

    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


# FIBONACCI (Memoized Recursive)


fib_memo_calls = 0


def fib_memo(n, memo=None):
    global fib_memo_calls
    fib_memo_calls += 1

    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)

    return memo[n]


# TOWER OF HANOI


def hanoi(n, source, auxiliary, destination, stack):
    if n == 1:
        move = f"Move disk 1 from {source} to {destination}"
        print(move)
        stack.push(move)
        return

    hanoi(n - 1, source, destination, auxiliary, stack)

    move = f"Move disk {n} from {source} to {destination}"
    print(move)
    stack.push(move)

    hanoi(n - 1, auxiliary, source, destination, stack)


# RECURSIVE BINARY SEARCH


def binary_search(arr, key, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search(arr, key, low, mid - 1)
    else:
        return binary_search(arr, key, mid + 1, high)


# MAIN EXECUTION (test cases)


if __name__ == "__main__":

    print("===== AERT TOOLKIT OUTPUT =====")

    # FACTORIAL
    print("\n--- Factorial Tests ---")
    for n in [0, 1, 5, 10]:
        print(f"Factorial({n}) =", factorial(n))

    # FIBONACCI
    print("\n--- Fibonacci Tests ---")
    for n in [5, 10, 20, 30]:

        fib_naive_calls = 0
        result_naive = fib_naive(n)
        print(f"Naive Fib({n}) = {result_naive}, Calls = {fib_naive_calls}")

        fib_memo_calls = 0
        result_memo = fib_memo(n)
        print(f"Memo  Fib({n}) = {result_memo}, Calls = {fib_memo_calls}")

    # TOWER OF HANOI (N = 3)
    print("\n--- Tower of Hanoi (N = 3) ---")
    stack = StackADT()
    hanoi(3, "A", "B", "C", stack)
    print("Total Moves:", stack.size())

    # BINARY SEARCH
    print("\n--- Binary Search Tests ---")
    arr = [1, 3, 5, 7, 9, 11, 13]

    for key in [7, 1, 13, 2]:
        print(f"Search {key}:", binary_search(arr, key, 0, len(arr) - 1))

    print("Empty list test:", binary_search([], 5, 0, -1))
