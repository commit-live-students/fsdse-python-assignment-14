def solution(list):
    '''
    Enter your code here
    '''

    unique = []
    for x in list:
        if x not in unique:
            unique.append(x)
    return (unique)

print solution([12,34,565,77,77,77])
