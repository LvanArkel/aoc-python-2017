a = 1
b = 105700
c = 122700
e = 0
g = 0
h = 0

# 9 - 32: Loop C
while True:
    f = 1 # 9
    d = 2 # 10

    # 11 - 24: Loop B
    while True:
        # 12 - 20: Loop A condensed
        if b % d == 0:
            f = 0
            break
        d += 1 # 21
        if d == b: break # 24

    if f == 0: # 25
        h += 1 # 26
    if b == c: # 29
        break # 30
    b += 17 # 31

print('h=',h)