def is_power_two(n):
  if n<=0:
    return false
  else:
    return n & (n-1)==0
n=int(input(""))
if is_power_two(n):
  print("yes")
else:
  print("no")
