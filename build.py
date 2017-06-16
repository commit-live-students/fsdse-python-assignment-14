def solution(list):
    l = [3,4,3,5,4]
    n= []
    for i in l:
          if i not in n:
              n.append(i)
    print (n) 
    unique = []
    for x in list:
        if x not in unique:
            unique.append(x)
    return (unique)
