hexLetters = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
 
def toHex(d):
    if d > 9:
        return (hexLetters[d])
    else:
        return str(d)
 
def hexPrinter(n):
    if n < 16:
        return toHex(n)
    else:
        return ((toHex(n % 16)) + hexPrinter(int(n)//16)) 
 
def bin_to_hex(binary_string):
    decRes = 0
    revBinSt = binary_string[::-1]
    for i in range(len(revBinSt)):  
        decRes += int(revBinSt[i])*(2**i)
    finalHex = str(hexPrinter(int(decRes)))
    return ((finalHex)[::-1])
        
print (bin_to_hex('11010101010011010010'))
print (bin_to_hex('110101010100110101010010101010010'))
print (bin_to_hex('0000011010010'))
print (bin_to_hex('1010'))