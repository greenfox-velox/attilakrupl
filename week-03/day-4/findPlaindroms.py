word = "indulag0r0galudni kosarasokkosarasok"
palindrom_list = []   
for i in range(len(word)):  
    for j in range(len(word)-1,i+1,-1): 
        bit = word[i:j+1]
        bit_rev = bit[::-1]
        if bit == bit_rev:
            palindrom_list.append(bit)
        else:
            pass
print (palindrom_list)