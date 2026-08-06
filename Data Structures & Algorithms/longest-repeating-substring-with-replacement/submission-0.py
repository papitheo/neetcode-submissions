class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = {}
        left_ptr = 0
        max_char = 0
        res = 0

        for right_ptr in range(len(s)):
            c = s[right_ptr]
            char_count[c] = char_count.get(c,0) + 1
            max_char = max(max_char,char_count[c])

            while (right_ptr - left_ptr + 1) - max_char > k:
                left_char = s[left_ptr]
                char_count[left_char] -= 1
                left_ptr+=1
            res = max(res, right_ptr - left_ptr + 1)

        return res


