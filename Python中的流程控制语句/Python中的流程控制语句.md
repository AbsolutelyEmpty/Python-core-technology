### Python中的流程控制语句

##### if语句
```python
print("Please input your score:")
score = int(input())
if score >= 90 and score <= 100:
    print("Your level is A.")
elif score >= 80:
    print("Your level is B.")
elif score >= 60:
    print("Your level is C.")
else:
    print("Your level is D.")
```
##### for语句
```python
# 输出乘法口诀表
for i in range(1,10):
    for j in range(1,10):
        if j<=i:
            print(j,"*",i,"=",i*j,end = "\t")
    print()
```
这里提到了`range()`函数,简单的介绍下
```markdown
range(start,end,step)  
顺序输出[start,end)区间内的数据； 
step表示按照指定的幅度增加；
range()表现的像列表，但其实并不是，可以使用list(range(element))，从迭代对象中创建列表；
```
##### break,continue语句，以及循环中的else语句  
官方文档在这里举例一个输出10以内质数的例子：
```python
# 质数定义为在大于1的自然数中，除了1和它本身以外不再有其他因数。
for i in range(2,10):
    for j in range(2,i):
        if i%j == 0:
            print(i,"=",j,"*",i//j)
            break
    else:
        print(i,"is a prime number")
```
输出的结果如下：
```python
>>> 
============== RESTART: C:/Python3/Python37/testPrimeNumber.py ==============
2 is a prime number
3 is a prime number
4 = 2 * 2
5 is a prime number
6 = 2 * 3
7 is a prime number
8 = 2 * 4
9 = 3 * 3
>>> 
```
> 

虽然上述的代码正确输出了10以内的质数，但不是质数的数字并没有列举完所有情况的因数分解，所以有下面的优化：
```python
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
```
输出结果如下：
```python
2 is a prime number
3 is a prime number
4 = 2 * 2
5 is a prime number
6 = 2 * 3
6 = 3 * 2
7 is a prime number
8 = 2 * 4
8 = 4 * 2
9 = 3 * 3 
```
这里做下总结：  
**break**  
用于跳出最近的 for 或 while 循环。  
**continue**  
继续循环中的下次迭代。  
**else**  
这里的else并不是if的，而是for的；  
表示循环没有找到一个符合条件的因素时执行else子句。  
##### while语句  
```python
while True:
    print("Please input your username:")
    userName = input()
    print("Please input your password:")
    password = input()
    if userName == "admin" and password == "123456":
        print("Welcome!",userName)
        break
    else:
        print("Please try entering your username and password again!")
```
其实while循环和for循环可以相互转换。
##### pass语句
- pass 语句什么也不做。
```python
>>> while True:
	pass
```
- 创建最小的类
```python
>>> class MyEmptyClass:
         pass

        
>>> 
```
- pass 的另一个可以使用的场合是在你编写新的代码时作为一个函数或条件子句体的占位符，允许你保持在更抽象的层次上进行思考。 pass 会被静默地忽略:  
```python
>>> def initlog(*args):
     pass   # Remember to implement this!

>>> 
```

