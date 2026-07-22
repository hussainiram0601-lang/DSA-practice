import bisect
from typing import List


class Solution:

  def maxActiveSectionsAfterTrade(
      self, s: str, queries: List[List[int]]
  ) -> List[int]:
    n = len(s)
    total_ones = s.count('1')

    # 1. Decompose string into contiguous segments
    segments = []
    i = 0
    while i < n:
      j = i
      while j < n and s[j] == s[i]:
        j += 1
      segments.append((s[i], i, j - 1))  # (char, start, end)
      i = j

    m = len(segments)

    # 2. Extract 1-segments
    one_segs = []
    for idx in range(m):
      if segments[idx][0] == '1':
        one_segs.append((segments[idx][1], segments[idx][2], idx))

    num_one_segs = len(one_segs)
    if num_one_segs == 0:
      return [total_ones] * len(queries)

    # 3. Precalculate base gains for fully internal 1-segments
    A = [0] * num_one_segs
    for k in range(num_one_segs):
      seg_idx = one_segs[k][2]
      len_left = (
          segments[seg_idx - 1][2] - segments[seg_idx - 1][1] + 1
          if seg_idx > 0
          else 0
      )
      len_right = (
          segments[seg_idx + 1][2] - segments[seg_idx + 1][1] + 1
          if seg_idx < m - 1
          else 0
      )
      A[k] = len_left + len_right

    # 4. Build Sparse Table for Range Maximum Query (RMQ)
    LOG = num_one_segs.bit_length()
    st = [[0] * num_one_segs for _ in range(LOG)]
    st[0] = A[:]

    for j in range(1, LOG):
      length = 1 << (j - 1)
      for k in range(num_one_segs - (1 << j) + 1):
        st[j][k] = max(st[j - 1][k], st[j - 1][k + length])

    def query_rmq(L: int, R: int) -> int:
      if L > R:
        return 0
      length = R - L + 1
      j = length.bit_length() - 1
      return max(st[j][L], st[j][R - (1 << j) + 1])

    starts = [os[0] for os in one_segs]
    ends = [os[1] for os in one_segs]

    ans = []
    for l, r in queries:
      # Find range of valid 1-segments inside (l, r)
      L_seg = bisect.bisect_right(starts, l)
      R_seg = bisect.bisect_right(ends, r - 1) - 1

      if L_seg > R_seg:
        ans.append(total_ones)
        continue

      # Helper function for boundary 1-segments
      def get_gain(k: int) -> int:
        start_k, end_k, seg_idx = one_segs[k]
        s_l = segments[seg_idx - 1][1]
        gain_left = start_k - max(l, s_l)

        e_r = segments[seg_idx + 1][2]
        gain_right = min(r, e_r) - end_k
        return gain_left + gain_right

      if L_seg == R_seg:
        max_gain = get_gain(L_seg)
      else:
        gain_L = get_gain(L_seg)
        gain_R = get_gain(R_seg)
        max_gain = max(gain_L, gain_R)

        # Query middle fully internal 1-segments
        if L_seg + 1 <= R_seg - 1:
          max_gain = max(max_gain, query_rmq(L_seg + 1, R_seg - 1))

      ans.append(total_ones + max_gain)

    return ans
        