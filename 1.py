def convertToTernary(num):
    quotient=num/3
    remainder=num%3
    if quotient==0:
        return""
    else:
        return convertToTernary(int(quotient)+str(int(remainder)))
number=int(input("enter number:"))
print(convertToTernary(number))
