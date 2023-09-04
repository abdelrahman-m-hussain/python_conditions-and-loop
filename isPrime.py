def main():
    num = int(input('enter the number you want to check: '))
    
    if isPrime(num):print(f'Number {num} is primary number')
    else:print(f'Number {num} is not primary number')
    
def isPrime(n):
    if n==1:return False
    elif n>1:
        for i in range(2,n):
            if n%i==0:
                return False
            else:
                continue
        return True
    
main()