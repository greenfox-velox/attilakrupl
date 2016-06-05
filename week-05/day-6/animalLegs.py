def animals(heads, legs):
    cows = ( legs - 2 * heads ) / 2 
    chicks = heads - cows
    tupler = (chicks, cows)    
    if heads < 0 or legs < 0 or legs % 2 != 0 or type(legs) != int or type(heads) != int or heads > legs / 2:
        return "No solutions"
    else:
        return tupler
    
    
print (animals(-370.0, 424.0))
