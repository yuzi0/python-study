"""
    ✅ 오늘의 문제 : 짝수이면서 7의 배수는 아닌 수 찾기 / 입력한 숫자들의 합 구하기

    1) 1부터 100까지의 수 중에서 짝수이면서 7의 배수가 아닌 수의 개수를 출력해보세요. 
    (정답은 비밀!)
    2) 0이 입력될 때까지 숫자를 계속 입력 받아 입력 받은 숫자들의 합을 출력하는 프로그램을 만들어보세요
"""

print("Q1")

count = 0
for i in range(1, 101):
    if ((i % 2) == 0) and ((i % 7) != 0):
        count = count + 1

print("> %d개"%count)
print("-----------------------")
print("Q2")

sum = 0
while True:
    num = int(input("숫자를 입력하세요 : "))
    if num == 0:
        break
    sum = sum + num
print("> 총합은 %d입니다"%sum)
