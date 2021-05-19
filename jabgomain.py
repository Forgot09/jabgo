
list1 =[]#표의 위쪽 대입
list2 = []#표의 아래쪽 원래
list3 = []#입력한 글자의 원 글자
'''
함수 밖에서 선언한 변수라도 함수 안에서 참조하면 또 다른 지역 변수가 생긴다 ㅠㅠ
'''

def jgmuipkn():#잡고미으프쿠나, 암호 리스트 추가
    csn = str(input('만들 암호체계 이름을 입력해주세요: '))
    print("더 이상 추가할 암호 대응이 없으면 'end'를 입력하세요")
    inputdata = 0
    #end가 입력 될때 까지 계속 입력 받기
    while inputdata != 'end':
        inputdata = str(input('list1 > '))
        list1.append(inputdata)
        if inputdata == 'end':
            continue
    print("list1 입력이 끝났습니다")
    
    print("list2는 원래 글자에 해당합니다\n")
    print("더 이상 추가할 암호 대응이 없으면 'end'를 입력하세요")
    inputdata = 0
    #end가 입력 될때 까지 계속 입력 받기
    while inputdata != 'end':
        inputdata = str(input('list2 > '))
        list2.append(inputdata)
        if inputdata == 'end':
            continue
    print("list2 입력이 끝났습니다")
    csn = csn + '.txt'
    f = open(csn, 'a')

    #list1 input
    f.write('list1 > ')
    for i in list1:
        f.write(i)
        f.write(' | ')
    f.write('\n')

    #list2 input
    f.write('list2 > ')
    for i in list2:
        f.write(i)
        f.write(' | ')
    f.write('\n')

    f.close()

def jgshgn():
    whilef = 0
    print('글자를 한글자씩 입력해주세요. 끝나셨으면 "end"라고 입력을 해주세요 ex)한글, ㅎ ㅏ ㄴ ㄱ ㅡ ㄹ')
    inputf = 0
    while inputf != 'end':
        inputf = str(input("input chars > "))
        list3.append(inputf)
        if inputf == 'end':
            continue
    for i in list3:
        char = i
        for y in list2:
            whilef += 1
            if char == y:
                whileff = whilef
        print(list1[whileff - 1])

'''
=======================================================================
'''
orf = 0
print('프로그램을 종료하시고 싶으시면 "end"를 입력해 주세요')
print('1은 암호 만들기\n2는 변환기입니다')
while orf != 'end':
    inputf = str(input('main > '))
    if inputf == 'help':
        print('1은 암호 만들기\n2는 변환기입니다')
    elif inputf == '1':
        jgmuipkn()
    elif inputf =='2':
        jgshgn()
    else:
        print(inputf, '는 명령어에 없습니다 help를 참고해주세요')
        print('1은 암호 만들기\n2는 변환기입니다')
    if inputf == 'end':
            print('종료')
            break