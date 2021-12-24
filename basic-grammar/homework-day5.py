birth = int(input("생일을 입력해주세요. "))

year = birth//10000
month = (birth%10000)//100
day = birth%100

print("%d년 %d월 %d일"%(year, month, day))