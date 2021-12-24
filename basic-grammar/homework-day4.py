price = 3420

print("물건의 가격은", price, "원입니다.")
print("=> 1000원", price//1000, "장")
print("=> 100원", (price%1000)//100, "개")
print("=> 10원", (price%100)//10, "개")
print("==> 필요한 동전의 개수 :", (price%1000)//100 + (price%100)//10)