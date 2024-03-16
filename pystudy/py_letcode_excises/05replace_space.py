class Solution:
    def replaceSpace(self, s: str) -> str:
        counter = s.count(' ')

        res = list(s)
        # 每碰到一个空格就多拓展两个格子，1 + 2 = 3个位置存’%20‘
        # list()可以把每个字符分割成为一个元素
        res.extend([' '] * counter * 2)
        print(res)

        # 原始字符串的末尾，拓展后的末尾
        left, right = len(s) - 1, len(res) - 1

        while left >= 0:
            if res[left] != ' ':
                res[right] = res[left]
                right -= 1
            else:
                # [right - 2, right), 左闭右开
                res[right - 2: right + 1] = '%20'
                right -= 3
            left -= 1
        return ''.join(res)  # 以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串


if __name__ == '__main__':
    s = Solution()
    print(s.replaceSpace("we are happy."))

"""
相当于对扩充后要占位置的字符串先占位置，然后将结尾一点点往后移，遇到要替换的在后面的指针替换掉

但要替换的字符更少怎么办？？
"""