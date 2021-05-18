list1 =[]#표의 위쪽 대입
list2 = []#표의 아래쪽 원래
list3 = []#
cryptosystemname = 0

def jgshgn():
	print('글자를 한글자씩 입력해주세요. 끝나셨으면 "end"라고 입력을 해주세요 ex)한글, ㅎ ㅏ ㄴ ㄱ ㅡ ㄹ')
	inputf = 0
	while inputf == 'end':
		inputf = str(input('> '))
		list3.append(inputf)
	
def jghjbrn():#잡고 하짐 받름니, 암호 파일 만들기
    cryptosystemname = cryptosystemname + '.txt'
    f = open(cryptosystemname, 'a')

    #list1 input
    f.write('list1 > ')
    for i in list1:
        f.write(i, '|')
    f.write('\n')

    #list2 input
    f.write('list2 > ')
    for i in list2:
        f.write(i, '|')
    f.write('\n')
#jghjbrn end
	jgshgn()

def jgmuipkn():#잡고미으프쿠나, 암호 리스트 추가
    cryptosystemname = str(input('만들 암호체계 이름을 저장해주세요.'))
    print("변환될\n")
    print("더 이상 추가할 암호 대응이 없으면 'end'를 입력하세요")
    inputdata = 0
    #end가 입력 될때 까지 계속 입력 받기
    while inputdata == 'end':
        inputdata = str(input('list1 > '))
        list1.append(inputdata)
    print("list1 입력이 끝났습니다")
    
    print("list2는 원래 글자에 해당합니다\n")
    print("더 이상 추가할 암호 대응이 없으면 'end'를 입력하세요")
    inputdata = 0
    #end가 입력 될때 까지 계속 입력 받기
    while inputdata == 'end':
        inputdata = str(input('list1 > '))
        list2.append(inputdata)
    print("list2 입력이 끝났습니다")

    jghjbrn()
