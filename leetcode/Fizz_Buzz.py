"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
"""

from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        data = []
        for i in range(1, n+1):
            if (not i%15):
                data.append('FizzBuzz')
            elif (not i%3):
                data.append('Fizz')
            elif (not i%5):
                data.append('Buzz')
            else:
                data.append(str(i))
        return data

if __name__ == "__main__":
    solution = Solution()
    print(solution.fizzBuzz(15))

"""
One line solution:
return [(not int(i)%3) * 'Fizz' + (not int(i)%5) * 'Buzz' or str(i) for i in range(1,n+1)]
"""