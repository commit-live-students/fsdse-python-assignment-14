def solution(list):
    list=[1,2,3,4,4,5,5]
    unique = []
    for x in list:
        if x not in unique:
            unique.append(x)
    return (unique)
print solution(list)
