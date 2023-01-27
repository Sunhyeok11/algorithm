a = input()
c=0

while True:
    b = input()
    if b == '문제':
        c +=1
    elif b =='고무오리':
        if c != 0:
            c-=1
        elif c == 0:
            c +=2
    elif b == '고무오리 디버깅 끝':
        break

if c == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')