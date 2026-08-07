class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1,len_s2 = len(s1),len(s2)
        count = [0] * 26

        for ch in s1:
            count[ord(ch) - ord('a')] += 1

        left = 0
        remaining_s1_ch = len_s1

        for right in range(len_s2):
            s2_ch_ind = ord(s2[right]) - ord('a')
            if count[s2_ch_ind] > 0:
                remaining_s1_ch -= 1
            count[s2_ch_ind] -= 1

            if right - left + 1 > len_s1:
                outgoing_s2_ch = ord(s2[left]) - ord('a')
                count[outgoing_s2_ch] += 1

                if count[outgoing_s2_ch] > 0:
                    remaining_s1_ch += 1
                left+=1

            if remaining_s1_ch == 0:
                return True
        return False




