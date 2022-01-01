"""
    ✅ 오늘의 문제 : 정수 n까지의 합을 구하는 함수 만들기
    정수 n을 하나 입력받고, 0부터 n까지의 합을 구하는 함수를 만들어 보세요
"""

def Sum(n):
    return n*(n+1)/2

number = int(input("정수를 입력하세요. : "))
print("1부터 %d까지의 총합은 %d입니다"%(number, Sum(number)))