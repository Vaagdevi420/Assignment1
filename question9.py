n = list(map(int,input().split(",")))
#print(n)
v=[]
if(len(n)>0):
    for i in range(0,len(n)):
        kg = n[i] * 0.453
        v.append(kg)
    print(v)
else:
    print("no students  ")
