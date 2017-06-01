def solution(list):
    '''
    Enter your code here
    '''
    unique = []
    for x in list:
        if x not in unique:
            unique.append(x)
    return (unique)

output = solution([1,2,3,4,2,3])
print output
