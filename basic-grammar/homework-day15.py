"""
    ✅ 오늘의 문제 : 최댓값의 위치를 구하기
    크기(길이)가 6 이상인 리스트를 값과 함께 선언하고 최댓값이 어디에 위치하는지 출력하세요.
    [필수조건]
    - 매개변수가 있는 함수를 사용하세요.
"""

def getMaxIndex(nums):
    max = nums[0]
    maxIdx = 0 
    for i in range(len(nums)):
        if max < nums[i]:
            max = nums[i]
            maxIdx = i
    return maxIdx

nums = [11, 13, 9, 15, 4, 1, -10]
idx = getMaxIndex(nums)

print("nums :", nums)
print("Max num:", nums[idx])
print("Max num index :", idx)