height = float(input("키를 입력하세요. :"))
weight = float(input("몸무게를 입력하세요. :"))

bmi = weight / (height ** 2)

if bmi < 18.5 :
    print("BMI 지수가", bmi, "이므로 저체중입니다.")

elif bmi >= 23 and bmi < 25 :
    print("BMI 지수가", bmi, "이므로 정상 체중입니다.")
    
elif bmi >= 25 :
    print("BMI 지수가", bmi, "이므로 비만입니다.")

else :
    print("잘못된 입력입니다.") 

