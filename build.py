def solution(list):
    '''
    Enter your code here
    '''
    unique = []
    for x in list:
        if x not in unique:
            unique.append(x)
    #print unique
    return (unique)

solution([1,1,2,3])
