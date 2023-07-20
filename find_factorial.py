def find_factorial(number):
    if number==1:
        return 1
    return find_factorial(number-1)*number

number=int(input("Enter the Number : "))
print(find_factorial(number))