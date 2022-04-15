# Enter your code here. Read input from STDIN. Print output to STDOUT

#takes factorial of the integer
def facto(num:int):
    if num==0:
        return int(1)
    else:
        return num*facto(num-1)

#takes input, converts to integer
def takeInput():
    q = int(input())
    n=[]
    m=[]
    for i in range(q):
        x = input()
        x = x.split()
        n.append(int(x[0]))
        m.append(int(x[1]))
    
    return q,n,m

#splits integer to digits, returns list of digits
def splitInt(n:int):
    myStr = str(n)
    split = []
    for i in range(len(myStr)):
        split.append(int(myStr[i]))        
    return split

#takes factorial of each element(digits)
def f_1(split:list):
    factos = []
    for i in range(len(split)):
        factos.append(facto(split[i]))
    return factos

#sums elements(factorials of digits)
def f_2(factos:list):
    facto_sum = sum(factos)    
    return facto_sum

#sums the digits of integer(sum of factorials of digits)
def s_f(facto_sum:int):
    s_f_split = splitInt(facto_sum)
    s_f_summed = sum(s_f_split)
    return s_f_summed

#same as s_f but s_f was wrongly named , sumDigits was way to go
def sumDigits(i:int):
    summed = s_f(i)
    return summed

#searches n witch satisfies g(i) = n
def g(i:int):
    n = 1
    while ((s_f(f_2(f_1(splitInt(n))))) != i):
        n = n + 1    
    return n

#sums the digits of g(i)=n for n
def g_sum(g_n:int):
    summed = sumDigits(g(g_n))
    return summed

#iteration sum
def gross_sum(n:int):
    summed = 0
    for i in range(1,n+1):
        summed = summed + g_sum(i)
    return summed
        
        




q,n,m = takeInput()
for i in range(q):
    print(gross_sum(n[i])%m[i])