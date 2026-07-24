class Solution:

  def uniqueXorTriplets(self, nums: list[int]) -> int:
    S = list(set(nums))

    # All unique XOR values from pairs (a ^ b)
    S2 = {x ^ y for x in S for y in S}

    # All unique XOR values from triplets ( (a ^ b) ^ c )
    S3 = {x ^ y for x in S2 for y in S}

    return len(S3)
        