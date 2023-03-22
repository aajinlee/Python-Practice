#4의 배수이면서 100으로 나누어떨어지지 않으면 윤년이다
#단, 연도가 400으로 나누어떨어지는 해는 윤년이다.

year = int(input("연도를 입력하세요. :"))

if year % 4 == 0 and year % 100 != 0 :
    print(str(year)+"은 윤년입니다.")

elif year % 400 == 0 :
    print(str(year)+"은 윤년입니다.")

else :
    print(str(year)+"은 윤년이 아닙니다.")
      