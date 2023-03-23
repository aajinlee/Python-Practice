def addSum(n) :
    sum = 0
    for i in range(1, n+1) :
        sum = sum + i
    print(sum)

num = int(input("정수를 입력하세요 :"))
addSum(num)