"""hap, i = 0, 0

while True :
    hap += i
    i = i + 1
    if hap >= 1000 :
        break
print("1~100의 합계를 최초로 1000이 넘게 하는 숫자 : %d" %i)

i, dan = 0, 0
dan = int(input("단을 입력하세요 : "))
for i in range(1, 10, 1) :
    print("%d X %d = %2d" % (dan, i, dan * i))"""

"""import operator
traindic, trainlist = {}, []
traindic = {'Thomas' : '토마스', 'Edward' : '에드워드', 'henry' : '헨리', 'Gothen' : '고든', 'James' : '제임스'}
trainlist = sorted(traindic.items(), key = operator.itemgetter(1))
print(trainlist)"""


song = """ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"""
alphabet = dict()
for c in song :
    if c.isalpha() == False:
        continue
    c = c.lower()
    if c not in alphabet:
        alphabet[c] = 1
    else:
        alphabet[c] += 1
print(alphabet)
