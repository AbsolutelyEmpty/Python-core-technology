# 质数定义为在大于1的自然数中，除了1和它本身以外不再有其他因数。
for i in range(2,10):
    isPrime = True
    for j in range(2,i):
        if i%j == 0:
            print(i,"=",j,"*",i//j)
            isPrime = False
            continue
    else:
        if isPrime:
            print(i,"is a prime number")
        
