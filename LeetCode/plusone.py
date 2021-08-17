def onePlus(digits,increment):
    if len(digits) == 0 and increment == False:
        return digits
    
    if len(digits) == 0 and increment == True:
        return [1]+digits
    
    if increment == True and digits[-1] <= 8:
        digits[-1] = digits[-1]+1
        return digits
    
    if increment == True and digits[-1] ==9:
        return onePlus(digits[:-1],True)+[0]

        
    if digits[-1] != 9:
        digits[-1] = digits[-1]+1
        return digits
    else:
        return onePlus(digits[:-1],True)+[0]

digits=[8,9,9]
increment=False
print(onePlus(digits,increment))