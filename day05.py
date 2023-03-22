name = input("닉네임을 입력하세요 :")
print("당신의 닉네임은",name,"입니다")
a = input("숫자 1을 입력하세요 :")
print(a)
print(type(a)) # input으로 입력받은 모든 것은 문자열로 저장된다.
print(int(3.6))
print(float(3))
#입력받은 문자열을 정수형(int)로 강제 변환 하여 type을 출력했을 때 int로 나온다.
a = int(input("숫자 1을 입력하세요 :"))
print(a)
print(type(a))
my_age = 23
print("내 나이는" + str(my_age) + "이고 파이썬 공부 5일차야!") # +를 사용하면 int형과 str형을 같이 사용할 수 없는데 int형을 str로 강제 형 변환을 시켜주면 된다.
my_age2 = input("당신의 나이를 입력하세요 :")
print("당신의 나이는" + my_age2 +"입니다") # input으로 받은 변수는 str형이기 때문에 +로도 출력된다. 