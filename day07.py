# 1- 100까지의 짝수들 중 7의 배수가 아닌 수가 몇 개인지 출력

sum = 0

for i in range(2,102,2) :
    if i % 7 == 0:
        sum = sum + 1
        
sum = 50 - sum
print(sum)

