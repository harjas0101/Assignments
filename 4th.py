number = int(input("Enter a Number :"))
temp = number
add_sum = 0
while temp!=0:
    k = temp%10
    add_sum +=k*k*k
    temp = temp//10
if add_sum==number:
    print('Given number is a three-digit Armstrong Number')
else:
    print('Given number is not an Armstrong Number')
