def solution(list):
    unique = []
    for x in list:
        if x not in unique:
            unique.append(x)
    return (unique)

l = [1, 3, 4, 3 ,5]
solution(l)
