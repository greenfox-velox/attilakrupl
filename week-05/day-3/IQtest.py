def iq_test(numbers):
    new = numbers.split()
    even = {}
    evenc = 0
    odd = {}
    oddc = 0
    for i in range(len(new)):
        if int(new[i]) % 2 == 0:
            even[evenc] = i
            evenc += 1
        else:
            odd[oddc] = i
            oddc +=1
    
    if len(even) < len(odd):
        return even.get(0)+1
    else:
        return odd.get(0)+1
       
print (iq_test("2 4 7 8 10"))
print (iq_test("1 2 2"))