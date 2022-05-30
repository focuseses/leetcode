# Find the sum of integers between 1 and N (inclusive) that are not multiples of A or B.
# O(log(min(a)))
import sys
import math
def sumFunction():
    n, a, b = input("Enter three values: ").split(",", 3)
    N = int(n)
    A = int(a)
    B = int(b)
    sumAll = (N/2) * ((2 * 1) + (N - 1))
   
    NA =(((N - (N % A)) - A)/A) + 1
    

    sumA = (NA/2) * ((2 * A) + ((NA - 1) * A))
   

    NB = (((N - (N % B)) - B)/B) + 1
    sumB = (NB/2) * ((2 * B) + (NB - 1) * B)
  
# O(log n)
    hi = math.lcm(A, B)
    NC = (((N - (N % hi)) - hi)/hi) + 1
    sumLCM = (NC/2) * ((2 * hi) + (NC - 1) * hi)
    ans = sumAll - sumA - sumB + sumLCM
    print(ans)
sumFunction()
