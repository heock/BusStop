x = int(input("가방의 금액은 얼마입니까?>>>"))
y = int(input("시계의 금액은 얼마입니까?>>>"))
total = x + y
if total >= 100000:
    print(total * 0.7)
elif total >=50000:
    print(total * 0.8)
else:
    print(total * 0.9)