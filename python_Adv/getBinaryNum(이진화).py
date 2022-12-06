def getBinaryNum2(n, lists):
    a = n // 2
    b = n % 2
    lists.append(b)
    if a == 0:
        lists.sort(reverse=True)
        return lists 
    else:
        return getBinaryNum2(a, lists)
