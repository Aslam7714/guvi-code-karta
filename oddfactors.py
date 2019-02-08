num=int(input(""))
aaa=""
for i in range(1,num+1):
  if num%i==0 and i%2!=0:
    aaa=aaa+str(i)+" "
    i=i+1
print(aaa.strip())
