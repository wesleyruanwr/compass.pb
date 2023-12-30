with open('number.txt', 'r') as file:
    num = list(map(int, file.readlines()))
par = lambda x: x % 2 == 0
sePar= filter(par, num)
numOrd = sorted(sePar, reverse=True)
numMai = numOrd[:5]

print(numMai)
print(sum(numMai))
