a,b,n=map(int,input().split())
sum=d=a
for i in range(n-1):
  sum+=b
  d+=sum
print(d) 
