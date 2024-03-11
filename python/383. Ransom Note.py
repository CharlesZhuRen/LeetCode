class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 为magazine创建一个哈希表, key=字母，value=数量
        alpha = dict()
        for c in magazine:
            if c in alpha.keys():
                alpha[c] += 1
            else:
                alpha[c] = 1  # 若第一次遍历到这个字符，初始值设为1

        for c in ransomNote:
            if c not in alpha.keys() or alpha[c] == 0:
                return False
            else:
                alpha[c] -= 1

        return True
