class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Factorize t into prime factors 2, 3, 5, 7
        counts = [0, 0, 0, 0]
        temp_t = t
        for idx, p in enumerate([2, 3, 5, 7]):
            while temp_t % p == 0:
                counts[idx] += 1
                temp_t //= p
        
        if temp_t > 1:
            return "-1"

        def get_factors(d: int):
            if d == 2: return (1, 0, 0, 0)
            if d == 3: return (0, 1, 0, 0)
            if d == 4: return (2, 0, 0, 0)
            if d == 5: return (0, 0, 1, 0)
            if d == 6: return (1, 1, 0, 0)
            if d == 7: return (0, 0, 0, 1)
            if d == 8: return (3, 0, 0, 0)
            if d == 9: return (0, 2, 0, 0)
            return (0, 0, 0, 0)

        def min_digits_needed(c2, c3, c5, c7):
            """Returns min count of digits needed to satisfy factors."""
            c2, c3, c5, c7 = max(0, c2), max(0, c3), max(0, c5), max(0, c7)
            c8, r2 = divmod(c2, 3)
            c9, r3 = divmod(c3, 2)
            c4, r2 = divmod(r2, 2)
            c6 = 0
            if r2 == 1 and r3 == 1:
                c6 = 1
                r2 = r3 = 0
            return c8 + c9 + c5 + c7 + c4 + c6 + r2 + r3

        def make_smallest_suffix(c2, c3, c5, c7, length):
            """Greedily builds lexicographically smallest suffix digit-by-digit."""
            res = []
            cur2, cur3, cur5, cur7 = max(0, c2), max(0, c3), max(0, c5), max(0, c7)
            
            for rem_len in range(length, 0, -1):
                for d in range(1, 10):
                    f2, f3, f5, f7 = get_factors(d)
                    n2, n3 = cur2 - f2, cur3 - f3
                    n5, n7 = cur5 - f5, cur7 - f7
                    
                    if min_digits_needed(n2, n3, n5, n7) <= rem_len - 1:
                        res.append(str(d))
                        cur2, cur3, cur5, cur7 = n2, n3, n5, n7
                        break
            return "".join(res)

        n = len(num)
        first_zero = num.find('0')
        limit = first_zero if first_zero != -1 else n

        prefix_factors = [(0, 0, 0, 0)]
        for i in range(limit):
            d = int(num[i])
            f = get_factors(d)
            prefix_factors.append(tuple(prefix_factors[-1][j] + f[j] for j in range(4)))

        # 1. Check if num itself (without zeros) is valid
        if first_zero == -1:
            p2, p3, p5, p7 = prefix_factors[n]
            if p2 >= counts[0] and p3 >= counts[1] and p5 >= counts[2] and p7 >= counts[3]:
                return num

        # 2. Try replacing num[i] with digit d > num[i]
        for i in range(limit, -1, -1):
            if i >= n:
                continue
            
            p2, p3, p5, p7 = prefix_factors[i]
            rem2, rem3 = counts[0] - p2, counts[1] - p3
            rem5, rem7 = counts[2] - p5, counts[3] - p7

            start_digit = int(num[i]) + 1 if i < limit else 1

            for d in range(start_digit, 10):
                f2, f3, f5, f7 = get_factors(d)
                r2, r3 = rem2 - f2, rem3 - f3
                r5, r7 = rem5 - f5, rem7 - f7
                
                rem_len = n - 1 - i
                if min_digits_needed(r2, r3, r5, r7) <= rem_len:
                    suf = make_smallest_suffix(r2, r3, r5, r7, rem_len)
                    return num[:i] + str(d) + suf

        # 3. If no solution of length n, build smallest string of length > n
        needed_len = min_digits_needed(counts[0], counts[1], counts[2], counts[3])
        target_len = max(n + 1, needed_len)
        return make_smallest_suffix(counts[0], counts[1], counts[2], counts[3], target_len)