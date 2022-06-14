#모듈 = .py(확장자) 파일 : lec08_class_call.py

from pkg import lec08_class
#    패키지        모듈(.py)
lec08_class.dummy(5)

#--------------------------------------
from pkg.lec08_class import UserClass
#    패키지.모듈(.py)         클래스




#네임스페이스 (영역)== 메모리


uc1 = UserClass("홍길동", 22) #생성자
uc2 = UserClass("나유저", 32) #생성자
print(uc1.__dir__())
print(type(uc1))


uc1.userInfo(22)



UserClass.userPrint( '이')
print(UserClass.__dict__)




# --------------------------------------------
from pkg.lec08_class import MyClass

my = MyClass('나', 20, 'f')


# my.point

my.myfunc()

# print("*********",my._MyClass__point)

my.userInfo(20)  #부모꺼 호출
#패키지.모듈.클래스
#from pkg.book.notebook import my_first_module

#from pkg.book.notebook import my_area  import (변수,메서드)
    # 패키지                    ,모듈(py)




