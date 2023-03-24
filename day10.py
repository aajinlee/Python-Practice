#숫자 7개를 입력받아 리스트에 저장하고 그 수들의 평균을 구해서 출력하는 프로그램을 만들어 보세요

value = []

for i in range(0, 7) :
    x = int(input("정수를 입력하세요. :"))
    value.append(x)

sum = 0

for i in range(0, 7) : 
    sum = sum + value[i]

print("평균 :", sum/7)