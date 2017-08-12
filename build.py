def solution(a_list):
    a_list = list(set(a_list))
    unique = []
    for x in a_list:
        if x not in unique:
            unique.append(x)
    return (unique)
