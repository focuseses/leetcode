# Find the sum of integers between 1 and N (inclusive) that are not multiples of A or B.
import math
def sumFunction(N, A, B):
    sumAll = (N/2) * ((2 * 1) + (N - 1))
    sumNonA = (N/2) * ((2 * A) + (N - 1) * A)
    sumNonB = (N/2) * ((2 * B) + (N - 1) * B)
    lcm = math.lcm(A, B)
    sumLCM = (N/2) * ((2 * lcm) + (N - 1) * lcm)
    return sumAll - sumNonA - sumNonB + sumLCM

