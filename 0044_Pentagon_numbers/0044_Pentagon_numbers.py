# Pentagonal numbers are generated by the formula,
# P_n=n(3n−1)/2. The first ten pentagonal numbers are:

# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

# It can be seen that P_4 + P_7 = 22 + 70 = 92 = P_8.
# However, their difference, 70 − 22 = 48, is not pentagonal.

# Find the pair of pentagonal numbers, P_j and P_k,
# for which their sum and difference are pentagonal
# and D = |P_k − P_j| is minimised; what is the value of D?

from __future__ import annotations

import math


class PentagonalNumber:
    def __init__(self, n: int = None, P_n=None) -> None:
        if n is None and P_n is None:
            raise ValueError("Either n or P_n must be specified")
        self.n = n if n is not None else PentagonalNumber.get_n_of_pentagonal_number(PentagonalNumber(P_n=P_n))
        self.P_n = P_n if P_n is not None else n * (3 * n - 1) // 2

    @staticmethod
    def get_n_of_pentagonal_number(pentagonal_number: PentagonalNumber) -> int:
        if pentagonal_number.P_n < 0:
            raise ValueError("Pentagonal number must be positive")
        if PentagonalNumber.is_pentagonal(pentagonal_number.P_n):
            return 1 + math.sqrt(1 + 24 * pentagonal_number.P_n) // 6
        else:
            raise ValueError("Pentagonal number must be pentagonal")

    def next_number(self) -> PentagonalNumber:
        return PentagonalNumber(n=self.n + 1)

    def get_pentagonal_p_n(self) -> int:
        return self.P_n

    def get_pentagonal_n(self) -> int:
        return self.n

    @staticmethod
    def is_pentagonal(P_n: int) -> bool:
        return (1 + math.sqrt(1 + 24 * P_n)) % 6 == 0

    def __str__(self) -> str:
        return f"n: {self.n} -> P_n: {self.P_n}"

    def __repr__(self) -> str:
        return f"PentagonalNumber({self.n})"

    def __eq__(self, other_pentagonal_number: PentagonalNumber) -> bool:
        return self.P_n == other_pentagonal_number.P_n

    def __hash__(self) -> int:
        return hash(self.P_n)

    def __lt__(self, other_pentagonal_number: PentagonalNumber) -> bool:
        return self.P_n < other_pentagonal_number.P_n

    def __gt__(self, other_pentagonal_number: PentagonalNumber) -> bool:
        return self.P_n > other_pentagonal_number.P_n

    def __le__(self, other_pentagonal_number: PentagonalNumber) -> bool:
        return self.P_n <= other_pentagonal_number.P_n

    def __ge__(self, other_pentagonal_number: PentagonalNumber) -> bool:
        return self.P_n >= other_pentagonal_number.P_n

    def __ne__(self, other_pentagonal_number: PentagonalNumber) -> bool:
        return self.P_n != other_pentagonal_number.P_n

    def __add__(self, other_pentagonal_number: PentagonalNumber) -> int:
        return self.P_n + other_pentagonal_number.P_n

    def __sub__(self, other_pentagonal_number: PentagonalNumber) -> int:
        return abs(self.P_n - other_pentagonal_number.P_n)

    def __abs__(self) -> int:
        return abs(self.P_n)

    def __bool__(self) -> bool:
        return self.P_n > 0

    def __int__(self) -> int:
        return int(self.P_n)

    def __float__(self) -> float:
        return float(self.P_n)

    def __index__(self) -> int:
        return int(self.P_n)

    def __iter__(self):
        return iter([self.P_n])


class Solution:
    def __init__(self, P_j: PentagonalNumber, P_k: PentagonalNumber, D: int) -> None:
        self.P_j = P_j
        self.P_k = P_k
        self.D = D

    def __str__(self) -> str:
        return f"Solution:\n    {self.P_j}\n     {self.P_k}\n    Distance: {self.D}"

    def __repr__(self) -> str:
        return f"Solution({self.P_j}, {self.P_k}, {self.D})"

    def __hash__(self) -> int:
        return hash((self.P_j, self.P_k, self.D))

    def __eq__(self, other_solution: Solution) -> bool:
        return (
            (self.P_j == other_solution.P_k and self.P_k == other_solution.P_j)
            or (self.P_j == other_solution.P_j and self.P_k == other_solution.P_k)
        ) and self.D == other_solution.D

    def __lt__(self, other_solution: Solution) -> bool:
        return self.D < other_solution.D

    def __gt__(self, other_solution: Solution) -> bool:
        return self.D > other_solution.D

    def __le__(self, other_solution: Solution) -> bool:
        return self.D <= other_solution.D

    def __ge__(self, other_solution: Solution) -> bool:
        return self.D >= other_solution.D

    def __ne__(self, other_solution: Solution) -> bool:
        return self.D != other_solution.D

    def __add__(self, other_solution: Solution) -> int:
        return self.D + other_solution.D

    def __sub__(self, other_solution: Solution) -> int:
        return self.D - other_solution.D

    def __abs__(self) -> int:
        return abs(self.D)

    def __bool__(self) -> bool:
        return self.D > 0

    def __int__(self) -> int:
        return int(self.D)

    def __float__(self) -> float:
        return float(self.D)


def main():
    pentagonal_number = PentagonalNumber(n=1)
    pentagonal_numbers = [pentagonal_number]
    for _ in range(5000):
        pentagonal_number = pentagonal_number.next_number()
        pentagonal_numbers.append(pentagonal_number)

    solutions = []
    for j in range(len(pentagonal_numbers)):
        p_j = pentagonal_numbers[j]
        for k in range(j + 1, len(pentagonal_numbers)):
            p_k = pentagonal_numbers[k]
            difference: int = p_j - p_k
            summation: int = p_j + p_k
            if PentagonalNumber.is_pentagonal(difference) and PentagonalNumber.is_pentagonal(summation):
                solutions.append(Solution(p_j, p_k, difference))

    min_solution = min(solutions if solutions else [Solution(PentagonalNumber(0), PentagonalNumber(0), 0)])

    print("P_j:", min_solution.P_j)
    print("P_k:", min_solution.P_k)
    print("D:", min_solution.D)


if __name__ == "__main__":
    main()
