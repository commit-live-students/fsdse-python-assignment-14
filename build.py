def solution(l):

    unique = []
    for x in l:
        if x not in unique:
            unique.append(x)
    return unique

print solution([1,2,3,3,4,])
#print solution(l)
