def solution(list):
    unique = []
    for x in list:
        if x not in unique:
            unique.append(x)
    return (unique)
print solution([1,2,3,4,4,5,5])
