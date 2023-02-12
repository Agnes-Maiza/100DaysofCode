#complex calculator
x=input("Enter the first value ")
y=input("Enter the second value ")
p=input("Enter an operator.(eg +,-,*,/,%) ")
if p == '+':
    result= int (x)+int (y)
    print(x,p,y,"=",result)
elif p == '-':
    result= int (x)-int (y)
    print(x,p,y,"=",result)
elif p == '*':
    result= int (x)*int (y)
    print(x,p,y,"=",result)
elif p == '/':
    result= int (x)/int (y)
    print(x,p,y,"=",result)
elif p == '%':
    
    result= int (x)%int (y)
    print(x,p,y,"=",result)
else :
    print("Invalid operator")