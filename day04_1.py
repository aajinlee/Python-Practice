time = int(input("시간(초)을 입력해 주세요. : "))

#1day = 24hr = 1440min = 86400sec 
#1hr = 60min = 3600sec

print(time,"초 =", end=" ")

if time >= 86400 :
    day = time // 86400
    time = time % 8640
    if day > 0 :
        print(day,"일", end=" ")
    
if time >= 3600 :
    hr = time // 3600
    time = time % 3600
    if hr > 0 :
        print(hr,"시간", end=" ")
    
if time >= 60 :
    min = time // 60
    time = time % 60
    if min > 0 :
        print(min, "분", end=" ")
    
if time >= 0 :
    sec = time
    if sec > 0 :
        print(sec, "초", end=" ")
  
  