# 모듈 = .py(확장자) 파일 LEC_08_Class.py


def dummy(num):
    print("dummy() 함수 실행", num)

    dummy(5)
class UserClass:
    # 존재하는 모든것 = 프로그램에 녹일 수 있는 것 = 객체
    # 속성 = 값 = 변수
    # 행위 = 동작 = 함수(메서드)

    def __init__(self,name):
        print(name,"생성자",self)

    username = "aaa"
    userage = 0
# 생성자 매서드 = 초기화
    #메모리 == 인스턴스
#-------self 파라미터가 있는 함수는 반드시 생성자를
#-------만들어서 호출

#-------self 파라미터가 없는 함수는는
#------클래스로 만들어서 호출
    def userInfo(self,age):
        print(f"{age}살 입니다")

    def userPrint(name):
        print(f"{name}님 입니다")

    def userSearch(self,name):
        print(f"{self}주소,{name}")

    def userInsert(self):
        pass


#--------------------------------------------------
class MyClass(UserClass):

    #_MyClass + __point = 1000
    __point = 1000
    def __init__(self, gen):

        super().__init__('나','28')
        self.gen = 'm'

    def myfunc(self):
        print("myfunc()...")


    def myfunc(self, num):
        print("myfunc()...",num)


#네임스페이스란
# 변수가  객체를 바인딩할때 그 둘사이의 관게를 저장하는 공간
# 변수나 메서드는 네임스페이스 안에서 딕셔너리관계로 저장됨
# 인스턴스 생성 주소별로 별도의 스페이스를 유지
# 인스턴스의 네임스페이스 안에서 변수가 보이지않을때
# ---클래스의 네임스페이스에서 찾아서 쓴다
#클래스 정의 : class
#클래스 상속 : import
#메서드 정의 : def
#기본 생성자와 유사 :___init___(self)
