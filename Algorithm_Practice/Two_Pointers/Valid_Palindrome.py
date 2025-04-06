class Solution:
    def isPalindrome(self, s: str) -> bool:
        # str为空 return true
        if not s:
            return True

        # 去除空格和标点符号 统一大小写 比较处理完后的str和反转的str
        # 如果一致 则是回文串
        res = ""

        for char in s:
            if char.isalnum():
                res += char.lower()

        if res == res[::-1]:
            return True
        else:
            return False