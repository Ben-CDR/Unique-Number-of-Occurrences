def uniqueOccurrences(self, arr):
    dic = {}
    for i in arr:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    seen = []
    for i in dic.values():
        if i in seen:
            return False
        seen.append(i)
    return True