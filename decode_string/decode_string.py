class Solution:

    def decodeString(self, s: str) -> str:
        curr, nums, strs = [], [], []
        n = 0
        for char in s:
            if char.isdigit():
                n = n * 10 + ord(char) - ord('0')
            elif char == '[':
                nums.append(n)
                n = 0
                strs.append(curr)
                curr = []
            elif char == ']':
                strs[-1].extend(curr * nums.pop())
                curr = strs.pop()
            else:
                curr.append(char)
        return print("".join(strs[-1]) if strs else "".join(curr))

s = "3[a]2[bc]"
# return "aaabcbc".
s = "3[a2[c]]" 
# return "accaccacc".
s = "2[abc]3[cd]ef"
# return "abcabccdcdcdef".

s_instance = Solution()
s_instance.decodeString(s)