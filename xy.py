def printxy(values):
    print("x,y="+str(values))

def printv(a):
    for aa in a:
        printxy(aa)

print("\033c\033[43;30m\n")
aaa=[(0,1),(1,0),(0,0),(1,1)]

printv(aaa)
