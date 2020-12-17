

def get_num(move, input):
    ix=input.split(',')
    i=[]
    for a in ix:
        i.append(int(a))
    m=0
    last=-1
    hist={}
    while m<move:
        if (m%1000000)==0:
            print(m)
        if m<len(i):
            c=i[m]
        else:
            if last in hist:
                c=m-1-hist[last]
            else:
                c=0
        hist[last]=m-1
        last=c
        m+=1       
  
    return c

tests={'1,3,2':1,
'1,2,3':27,
'2,3,1':78,
'3,2,1':438,
'3,1,2':1836}

for test in tests:
    r=get_num(2020, test)
    if r!=tests[test]:
        print(f'{test} failed, {r=}')


print('part 1', get_num(2020, '15,5,1,4,7,0'))

test2={'0,3,6':175594}
for test in test2:
    r=get_num(30000000, test)
    if r!=test2[test]:
        print(f'{test} failed, {r=}')

print('part 2', get_num(30000000, '15,5,1,4,7,0'))