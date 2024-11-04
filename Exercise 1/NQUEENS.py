def solve(queens, N):
    if len(queens) == N:
        print("\n".join(" ".join("Q" if i == c else "." for i in range(N)) for c in queens))
        return True
    for col in range(N):
        if all(col != c and abs(len(queens) - r) != abs(col - c) for r, c in enumerate(queens)):
            if solve(queens + [col], N):
                return True
    return False

N = int(input("Enter the number of Queens: "))
solve([], N)
