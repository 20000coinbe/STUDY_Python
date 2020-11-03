# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
#   - sep : 단어와 단어사이를 무엇으로 연결시킬지 ex) '', '@', '-'
#   - end : 끝문장을 무엇으로 연결시킨지
#   - file :
#   - flush : 참값이면 스트림이 강제로 플러시

print("Hellow python");
print('Hellow python');
print('''Hellow python''');
print("""Hellow prython""");
print("Hellow", "python", "','로 문장을 이을 경우 공백이 자동으로 생성");
print("--------------------")
print("Hellow"+"python", "'+'로 단어를 연결시킬 경우 자동 띄어쓰기 안됨"); 

# sep옵션
print("--------------------")
print('P', 'Y', 'T', 'H', "O", "N", sep=''); # PYTHON
print('kim1234', 'gmail.com', sep = '@'); # kim1234@gmail.com

# end옵션
print("--------------------")
print("Hellow ", end=''); # end옵션은 다음 문장을 해당 문자열로 연결시켜준다 
print("python"); # Hellow python

# 중요 format() 이용 중괄호{}와 같이 사용된다
print("--------------------")
print('You & Me');
print('{} & {}'.format('You', 'Me'));
print('{a} & {b}'.format(a='You', b='ME')); # 명시적으로 사용할 수 있으니 꼭알아두자
print("%s & %s %d" % ('You', 'Me', 2)); # %s : 문자열, %d : 정수, %f : 실수
print("--------------------")
# 정수를 4자리로 표기, 실수를 정수4자리, 소수점은 2자리 표기 안맞으면 공백 또는 버려버린다
print("% 심화버전(C언어 때와 유사) :", "%4d과 %3.2f" % (123, 123.45));



# Escape 문자 : \ (역슬래쉬 뒤의 문자 1개는 반드시 출력된다)
print("'you'");
print('\'you\'');
print("""'you'""");
print('작은따움표에서 작은따움표 하나 쓰기 : he\'s a warrior');
print("줄바꿈 2번 \n");
print("print()자체 + 이스케이프문자('\\n')");









