"""
    ✅ 오늘의 문제 : 클래스 생성하기
    저번 시간에 여러분이 만든 나만의 계산기 클래스를 상속해 새로운 클래스를 만들어보거나,
    달콤한 파이썬 본문에 있는 "완벽한 계산기"를 이용하여 클래스를 새로 만들어보세요!
    (나만의 새로운 클래스를 만들어도 좋습니다.)
    [조건]
     - 클래스의 상속이 있어야합니다.
"""

class Calc():
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

class EngineerCalc(Calc):
    def __init__(self, first, second):
        super().__init__(first, second)
    def pow(self):
        result = self.first ** self.second
        return result
    def sqrt(self):
        result = self.first ** (1/self.second)
        return result
        

calc = EngineerCalc(10, 2)
print("10 + 2 = ", calc.add())
print("10 - 2 = ", calc.sub())
print("10 * 2 = ", calc.mul())
print("10 / 2 = ", calc.div())
print("10 ^ 2 = ", calc.pow())
print("10 ^ (1/2) = ", calc.sqrt())