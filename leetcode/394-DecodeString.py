class Solution:
    def decodeString(self, s: str) -> str:
        def decodeHelper(s: str, index: int):
            num = full_str = ""
            while index < len(s):
                if str(s[index]).isnumeric():
                    num += s[index]
                elif s[index] == '[':
                    index, new_str = decodeHelper(s, index + 1)
                    for i in range(int(num) if num else 1):
                        full_str += new_str
                    num = ""
                    continue
                elif s[index] == ']':
                    return (index + 1, full_str)
                else:
                    full_str += s[index]
                index += 1
            return (index + 1, full_str)
        return decodeHelper(s, 0)[1]