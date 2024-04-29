def kmp_search(s, pattern):
    def build_partial_match_table(pattern):
        '''
        构建部分匹配表：这一步骤是为了记录模式字符串中每个位置前的子字符串的最长相等前缀和后缀的长度。
        比如在模式 "ABCDABD" 中，到第五个字符 "B" 为止的子串 "ABCDAB" 的最长相等前后缀是 "AB"，长度为 2。
        这个信息用于在字符串匹配时，发生不匹配时决定如何移动模式字符串。
        '''
        length = len(pattern)
        table = [0] * length
        j = 0  # 最长相等前后缀的长度

        for i in range(1, length):  # 对于每个i，找到以该字符结尾的子串的最长相等前后缀
            while j > 0 and pattern[i] != pattern[j]:
                j = table[j - 1]  # 不匹配时，回退到前一个最长相等前后缀的长度，一直回退到0为止

            if pattern[i] == pattern[j]:
                j += 1
                table[i] = j  # 以第i个字符结尾的字串的最长相等前后缀，此时j=最长相等前后缀的长度

        return table

    # KMP搜索
    '''
    字符串匹配：在匹配过程中，我们会逐个比较原字符串和模式字符串的字符。
    如果出现不匹配的情况，我们会利用部分匹配表来确定模式字符串应该跳过多少个字符。
    例如，如果在某个位置不匹配，且部分匹配表在这个位置的值是 2，
    那么我们可以安全地跳过模式字符串的前两个字符，因为我们知道它们已经被匹配过了。
    '''
    partial_match_table = build_partial_match_table(pattern)
    print(partial_match_table)
    i = 0  # 主串中的指针
    j = 0  # 子串中的指针

    while i < len(s):
        if s[i] == pattern[j]:  # 字符匹配 指针后移
            i += 1
            j += 1
        elif j > 0:  # 字符失配，根据部分匹配表跳过一些字符
            j = partial_match_table[j - 1]
        else:
            i += 1

        if j == len(pattern):
            return i - j

    return -1  # 如果没有匹配到，返回-1


if __name__ == '__main__':
    # 测试KMP算法
    # s = "ABC ABCDAB ABCDABCDABDE"
    # pattern = "ABCDABD"
    s = "asdfauykbhcjbaksxuhakushxaisuhdaiksnxakisuh"
    pattern = "daiks"
    index = kmp_search(s, pattern)
    print(index)
