"""
    ✅ 오늘의 문제 : 튜플과 딕셔너리로 문자열 길이 출력하기
    3개의 문자열이 담긴 튜플을 선언하고, 딕셔너리를 통해 각각의 문자열의 길이를 저장한뒤 출력해보세요.

    출력 예시
        {'Hello': 5, 'This is Python': 14, 'Bye': 3}
"""

tup = ("hello", "my name is honggildong", "i want to go home")
dic = {}

for i in tup:
    dic[i] = len(i)

print(dic)