num = float(input("숫자를 입력해 주세요 :"))
up_num = int(num*10)
up_num = up_num % 10

if up_num < 5 :
    print(num,"을 반올림하면",int(num),"입니다")
else :
    print(num,"을 반올림하면",int(num +0.5),"입니다")
    


