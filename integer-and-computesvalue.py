# 10. Write a Python program that accepts an integer (n) and
 #computes the value of n+nn+nnn.
# Sample value of n is 5
 #Expected Result : 615

n=int(input("Enter an intrger:"))
nn=str(n)+str(n)
nnn=str(n)+str(n)+str(n)
result=n+int(nn)+int(nnn)
print("The result is:",result)
