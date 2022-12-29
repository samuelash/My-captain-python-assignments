def most_frequent(strng):
    x=dict()
    for i in strng:
        if i not in x:
            x[i]=1
        else:
            x[i]=x[i]+1
    return x

print(most_frequent('mississippi'))


        
        
      
