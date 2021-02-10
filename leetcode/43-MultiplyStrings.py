class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if not num1:
            return num2
        if not num2:
            return num1
        
        if num1 == '0'*len(num1) or num2 == '0'*len(num2):
            return '0'
        
        ans = []
        
        for idx in range(len(num2) - 1, -1, -1):
            num_part = self.multi_single(num2[idx], num1)
            zero_part = '0'*(len(num2) - idx - 1)
            ans = self.add(ans, num_part + zero_part)
        
        return ans[0]
    
    def multi_single(self, char, num):
        if char == '0':
            return '0'
        
        c_n = ord(char) - ord('0')
        prev = 0
        ans = []
        for idx in range(len(num) - 1, -1, -1):
            n_n = ord(num[idx]) - ord('0')
            res = c_n * n_n + prev
            prev = res // 10
            r_char = chr(res % 10 + ord('0'))
            ans.append(r_char)

        if prev != 0:
            ans.append(chr(prev + ord('0')))
        ans.reverse()
        return ''.join(ans)
    
    
    def add(self, ans, num_b):
        if len(ans) == 0:
            ans.append(num_b)
            return ans
        
        num_a = ans[0]
        max_len = max(len(num_a), len(num_b))
        num_a = '0' * (max_len - len(num_a)) + num_a
        num_b = '0' * (max_len - len(num_b)) + num_b
        
        prev = 0
        ans = []
        for idx in range(max_len - 1, -1, -1):
            n_a = ord(num_a[idx]) - ord('0')
            n_b = ord(num_b[idx]) - ord('0')
            res = n_a + n_b + prev
            
            prev = res // 10
            r_char = chr(res % 10 + ord('0'))
            ans.append(r_char)
        
        if prev != 0:
            ans.append(chr(prev + ord('0')))
        ans.reverse()
        return [''.join(ans)]