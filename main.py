
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
if len(num1) <= len(num2):
    num1.extend(num2)
    print(num1)
else:
    num2.extend(num1)
    print(num2)

# ******************************
# Make your Code
# ******************************

# print (num3) 
