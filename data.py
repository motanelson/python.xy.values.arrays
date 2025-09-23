def printxyz(values):
    print("x,y="+str(values))

def printv(a):
    for aa in a:
        printxyz(aa)

def build(lena,incx,incy):
    x=0
    y=0
    z=0
    list1=[]
    for n in range(lena):
        l1=[x,y]
        list1=list1+[l1]
        x=x+incx
        y=y+incy
        
    return list1 
def saves(names,list1):
    f1=open(names,"w")
    for n in list1:
        x,y=n
        f1.write(str(x)+", "+str(y)+"\n")
    f1.close()
print("\033c\033[43;30m\n")
aaa=build(80,5,2)
printv(aaa)
saves("data.txt",aaa)