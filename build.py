def solution(i):
    i=[1,1,2,3,4,4,5,5,5]
    unique = []
    for x in i:
        if x not in unique:
            unique.append(x)
    return unique
