"""
    ✅ 오늘의 문제 : 입력받은 수의 평균 구하기
    7개의 수를 입력받고 그 수들의 평균을 구하는 프로그램을 작성해보세요. 
    ❗ 리스트를 사용해주세요
"""

def aver(numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum/len(numbers)

numbers = []
for _ in range(7):
    numbers.append(int(input("정수를 입력하세요. : ")))

print("평균은 %d입니다"%(aver(numbers)))