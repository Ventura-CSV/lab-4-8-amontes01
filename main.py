def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    
    prime_num = int(num ** 0.5) + 1
    for i in range(3, prime_num, 2):
        if num % i == 0:
            return False
    
    return True

def main():
    plist = []
    
    begin = int(input("Enter integer 1: "))
    end = int(input("Enter integer 2: "))
    
    for num in range(begin, end + 1):
        if is_prime(num):
            plist.append(num)
    
    print(plist)
    return plist


if __name__ == '__main__':
    main()
