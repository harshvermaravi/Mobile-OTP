'''n=0
while(n<=10):
   import random
   print(random.randrange(1000,9999))
   n=n+1

'''
import random
n=random.randrange(1000,9999)
print(n)
a=int(input("Enter your otp:"))
if a==n:
    print("Login Sucess")
else:
    print("log out")
