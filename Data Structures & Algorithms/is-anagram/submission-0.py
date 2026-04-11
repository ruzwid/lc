class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ascii_value_of_a = ord('a') # 97
        zeroes_list = [0] * 26

        for i in s:
            ascii_value = ord(str(i))
            index = ascii_value - 97
            zeroes_list[index] = zeroes_list[index] + 1
        
        for j in t:
            ascii_value = ord(str(j))
            index = ascii_value - 97
            zeroes_list[index] = zeroes_list[index] - 1
        
        for n in zeroes_list:
            if n != 0:
                return False

        return True


