lower = int(input("Enter a starting number:"))
upper = int(input("Enter a ending number:"))

for i in range(lower,upper+1):
    if i>1:
        for j in range(2,i):
            if(i%j) ==0:
                break
        else:
            print(i)