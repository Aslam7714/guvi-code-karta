#javid_aslam
#greater_number_in_same_digit
n=int(input())
l=[]
for i in str(n):
    l.append(int(i))
for j in range(len(l)-1,0,-1):
    if l[j]>l[j-1]:
        break
if j==1:
    print("impossible")
else:
    a=l[j-1]
    l2=l[j:]
    m2=l2[0]
    for i in l2:
        if i>a and i<m2:
            m2=i
    k=l.index(m2)
    l[j-1],l[k]=m2,a
    l1=sorted(l[j:])
    for i in range(j):
        print(l[i],end="")
    for i in l1:
        print(i,end="")
