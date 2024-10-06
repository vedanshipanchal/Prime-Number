num = 123456

numstr = str(num)

left = int(numstr[len(numstr)//2-1])
right = int(numstr[len(numstr)//2])

multiply = left*right

print("The val is:",multiply)
