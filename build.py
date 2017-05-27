def solution(alist):
    uniquelist = []
    for x in alist:
        if x not in uniquelist:
            uniquelist.append(x)
    return uniquelist
