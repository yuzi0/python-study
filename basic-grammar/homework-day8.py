"""
    ✅ 오늘의 문제 : BMI 결과보기

    키와 몸무게를 입력받아 BMI지수가 25 ~는 '비만입니다.', BMI 지수가 23 ~ 25는 '과체중입니다.', BMI 지수가 18.5 ~ 23는 '정상체중입니다.', BMI 지수가 18.5 미만일 경우에는 '저체중입니다.'를 출력해주는 프로그램을 작성하시오.
    - BMI 지수는 몸무게(kg) / {키(m) * 키(m)} 로 계산한다.
"""

length = int(input("키를 입력하세요. : "))
weight = int(input("몸무게를 입력하세요. : "))

bmi = weight / (length/100 * length/100)
print("당신의 BMI는", bmi, "이며", end = " ")

if bmi < 18.5:
    print("저체중입니다.")
elif bmi < 23:
    print("정상체중입니다.")
elif bmi < 25:
    print("과체중입니다.")
else:
    print("비만입니다.")