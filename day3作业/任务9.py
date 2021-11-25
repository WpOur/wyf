for i in range(9,0,-1):
    for j in range(i,0,-1):
        print(str(j)+str("*")+str(i)+"="+str(j*i),end="\t")
    print()