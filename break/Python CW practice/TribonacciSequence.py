def tribonacci(signature,n):
    sequence = []
    for i in range(n):
        if i < 3:
            sequence.append(signature[i])
        else:
            sequence.append(sequence[i-1]+sequence[i-2]+sequence[i-3])
            
    return sequence
    
    
    
print (tribonacci([1,1,1],10))