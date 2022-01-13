"""
    ✅ 오늘의 문제 : 계산기 클래스 만들기
    여러분만의 계산기 클래스를 만들어서 입력과 출력까지 보여주세요. 정수가 아니여도 괜찮겠죠?
"""

class Calc():
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        return self.first + self.second
    def sub(self):
        return self.first - self.second
    def mul(self):
        return self.first * self.second
    def div(self):
        return self.first / self.second

calc = Calc(10, 2)
print("10 + 2 = ", calc.add())
print("10 - 2 = ", calc.sub())
print("10 * 2 = ", calc.mul())
print("10 / 2 = ", calc.div())