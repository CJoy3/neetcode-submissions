# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         l, r = 0, 0
#         length = len(s)
#         counts = {}
#         res = 0

#         for c in set(s):
#             counts[c] = 0
#         print(f"--{counts}--")
#         while l != length - 1 and r != length:
#             # print(f"res: {res}")
#             counts[s[r]] += 1
#             windSize = r - l + 1
#             # print(f"window size: {windSize}")
#             # print(f"max count value: {max(counts.values())}")
#             print(counts)
#             if windSize - max(counts.values()) <= k:
#                 res = max(res, windSize)
#                 r += 1
#             else:
#                 r += 1
#                 while not (windSize - max(counts.values()) <= k) and l != length:
#                     counts[s[l]] -= 1
#                     l += 1
#                     windSize = r - l + 1
            
#         return res
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        length = len(s)
        counts = {}
        for c in set(s):
            counts[c] = 0
        res = 0

        for r in range(length):
            counts[s[r]] += 1
            windSize = r - l + 1
            while windSize - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1
                windSize = r - l + 1
            res = max(res, windSize)

        return res
