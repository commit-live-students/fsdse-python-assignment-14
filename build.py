def solution(list):
    unique = []
    for x in list:
        if x not in unique:
            unique.append(x)
    return (unique)

list = [3,4,3,5,4]
solution(list)
