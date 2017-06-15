def solution(list):
    unique = []
    seen = set()
    for x in list:
        if x not in seen:
            seen.add(x)
    for y in seen:
        unique.append(y)
    return unique

l = [1, 3, 4, 3 ,5]
solution(l)
