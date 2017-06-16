def solution(list):
    seen = set()
    unique = []
    for x in list:
        if x not in seen:
            seen.add(x)
            unique.append(x)

    print unique
    return (unique)

solution([1,2,3,1,2,3,4,4,6,2,7,8])
