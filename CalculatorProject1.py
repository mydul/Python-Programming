

x= input("Enter variables: ").split(" ")

# print(len(x))
size = len(x)

#y = [0 for i in range(size)]

for i in range(0,size):
    #y[i] = x[i]

    if x[i] == '*':
        y = [0 for i in range(size)]
        #print(int(x[i-1])*int(x[i+1]))
        for j in range (i-1):
            y[j]=x[j]
        y[i-1]= int(x[i-1])*int(x[i+1])
        temp = i
        for j in range (i+2,size):
            y[temp]=x[j]
            temp=temp+1
        for k in range (size):
            x[k]=y[k]

for i in range(0,size):
    #y[i] = x[i]

    if x[i] == '+':
        y = [0 for i in range(size)]
        #print(int(x[i-1])+int(x[i+1]))
        for j in range (i-1):
            y[j]=x[j]
        y[i-1]= int(x[i-1])+int(x[i+1])
        temp = i
        for j in range (i+2,size):
            y[temp]=x[j]
            temp=temp+1
        for k in range (size):
            x[k]=y[k]

        
    

print(y)



