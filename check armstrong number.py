n=int(input("enter the number"))
sum=0
temp=num
while(temp>0):
 digit=temp%10
 sum+=digit**3
 temp//=10
 if(num==sum):
  print("given is armstrong number")
 else:
  print("given is not armstrong number")
