#寻找一个给定的元素在指定列表中的第一个索引值
def find1(S, val):
    n = len(S)
    j = 0
    while j < n:
        if S[j] == val：
            return j
        j += 1
    return -1
