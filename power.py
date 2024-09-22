# Program to check if a  number is a power of 2
def power2(number):
    # As the power of 2 we have only one set bit, then n-1 & n will always be zero(0)for any power of 2
    if(number == 0):
        return 0
    if((number & (~(number-1)))== number):
        return 1
    return 0
number = int(input("Enter the number:"))
if(power2(number)):
    print("\n the number is power of two")
else:
    print("\n the number is not a power of two")