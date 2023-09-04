def main():
    num1=int(input('enter first number: '))
    num2=int(input('enter second number: '))
    
    is_equal(num1,num2)
    
def is_equal(n1,n2):
    if n1==n2:print(f"the num1:{n1} equal num2:{n2}")
    else:print(f"the num1:{n1} not equal num2:{n2}")
    
main()