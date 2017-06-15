def solution(list):
    unique = []
    for x in list:
        if x not in unique:
            unique.append(x)
    return (unique)

l = [1, 2, 3, 2, 1, 5, 6, 5, 5, 5]
solution(l)
