# lec10_module_oracle.py

# API = 패키지 package--- 라이브러리
# import cx_Oracle as cx
#
# conn = cx.connect("ai","0000","127.0.0.1:1521/XE")
# # print(conn)
# if bool(conn):
#     print("연결성공")
# else:
#     print("연결실패")
#
#
# cur = conn.cursor()
# cur.execute("select * from emp")
#
#
# for c in cur:
#
#     print(c) #()튜블 : 수정,삭제 못하게 하기위해서
#
# cur.close()
# conn.close()

#-----------------------------------------------

#
# conn = cx.connect("ai","0000","127.0.0.1:1521/XE")
# # print(conn)
# if bool(conn):
#     print("연결성공")
# else:
#     print("연결실패")
#
#
# cur = conn.cursor()
# cur.execute("select * from emp where ename='KING'")
#
#
# for c in cur:
#
#     print(c) #()튜블 : 수정,삭제 못하게 하기위해서
#
# cur.close()
# conn.close()
#--------------------------------------------------------
import cx_Oracle as cx

class E :

    def my_select(ename=None):
        conn = cx.connect("test", "0000", "127.0.0.1:1521/XE")
        # print(conn)
        if bool(conn):
            print("연결성공")
        else:
            print("연결실패")

        cur = conn.cursor()
        if bool(ename) :
            sql = f"select * from emp where ename='{ename}'"
        else:
            sql = "select * from emp"
        cur.execute(sql)

        for c in cur:
            print(c)  # ()튜블 : 수정,삭제 못하게 하기위해서

        cur.close()
        conn.close()

#---------------------------------호출--------------------
# my_select('KING')
# my_select()




    def my_insert(empno, ename=None, deptno = None):

        sql = """insert into emp (empno, ename, deptno)
                values (:empno,:ename,:deptno)"""

        conn = cx.connect("test", "0000", "127.0.0.1:1521/XE")
        cur = conn.cursor()
        cur.execute(sql,[empno,ename,deptno])
        cur.close()
        conn.commit()
        conn.close()

        #현업가면 커넥션 풀이 있어서 갖다가 쓰고 반납하면 됨 나중에 언급


    def my_insert2(empno, ename=None, deptno = None):

        sql = """insert into emp (empno, ename, deptno)
                values (:empno,:ename,:deptno)"""

        conn = cx.connect("test", "0000", "127.0.0.1:1521/XE")
        cur = conn.cursor()
        # cur.execute(sql,{"empno":777,"ename":'BBB',"deptno":10})
        cur.execute(sql, {"empno": empno, "ename": ename, "deptno":deptno})
        cur.close()
        conn.commit()
        conn.close()
# ----------------- 인서트3, 인서트 매니 강추 none --와도그만 안와도그만
    def my_insert3(empno, ename=None, deptno = None):

        sql = """insert into emp (empno, ename, deptno)
                values (:1,:2,:3)"""

        conn = cx.connect("test", "0000", "127.0.0.1:1521/XE")
        cur = conn.cursor()
        # cur.execute(sql,{"empno":777,"ename":'BBB',"deptno":10})
        cur.execute(sql, [empno, ename, deptno])
        cur.close()
        conn.commit()
        conn.close()



    def my_insert_many(emp_list):

        sql = """insert into emp (empno, ename, deptno)
                values (:1,:2,:3)"""   #66,'CCC',10 값

        conn = cx.connect("test", "0000", "127.0.0.1:1521/XE")
        cur = conn.cursor()
        # cur.execute(sql,{"empno":777,"ename":'BBB',"deptno":10})
        cur.executemany(sql, emp_list)
        cur.close()
        conn.commit()
        conn.close()

 # ------------------------------------------------------
 # -- 사원번호 7902인 사원의 급여를 +1000 인상, 부서는 40번으로 발령

    def my_update(deptno, empno):

        sql = """update emp
                    set sal = sal + 1000, deptno = :1
                    where empno = :2
                    """

        conn = cx.connect("test", "0000", "127.0.0.1:1521/XE")
        cur = conn.cursor()

        cur.execute(sql, [deptno, empno])

        cur.close()
        conn.commit()
        conn.close()


    def my_update2(list):

        sql = """update emp
                    set sal = sal + 1000, deptno = :1
                    where empno = :2
                    """

        conn = cx.connect("test", "0000", "127.0.0.1:1521/XE")
        cur = conn.cursor()

        cur.execute(sql, list)

        cur.close()
        conn.commit()
        conn.close()

# ------------------------비추
    def my_update3(list):
        sql = """ update emp
                           set sal = sal + 1000, deptno = :1
                           where empno = :2
                           """

        conn = cx.connect("test", "0000", "127.0.0.1:1521/XE")
        cur = conn.cursor()

        cur.execute(sql, [list[0],list[1]])

        cur.close()
        conn.commit()
        conn.close()

# -------------------------------
# --10번 부서사람들 삭제
# --7698 7499 7844 사번 삭제

    def my_delete(deptno,empno):
        sql = """ delete emp where deptno = :1 or 
            empno in :2 """

        conn = cx.connect("test", "0000", "127.0.0.1:1521/XE")
        cur = conn.cursor()

        cur.execute(sql, [deptno, empno])

        cur.close()
        conn.commit()
        conn.close()

# ------------------------------------------------


    def my_delete1(deptno):
        sql = """ delete from emp where deptno = :1 """
        # sql = """ delete from emp where empno in(:1,:2,:3)"""

        conn = cx.connect("test", "0000", "127.0.0.1:1521/XE")
        cur = conn.cursor()

        cur.execute(sql, [deptno])

        cur.close()
        conn.commit()
        conn.close()

    def my_delete2(empno1,empno2,empno3):
        # sql = """ delete from emp where deptno = :1 """
        sql = """ delete from emp where empno in(:1,:2,:3)"""

        conn = cx.connect("test", "0000", "127.0.0.1:1521/XE")
        cur = conn.cursor()

        cur.execute(sql, [empno1,empno2,empno3])

        cur.close()
        conn.commit()
        conn.close()

# ---------------------------------------------------------
    def my_delete3(list):
        # sql = """ delete from emp where deptno = :1 """
        sql = """ delete from emp where empno = :1 """

        conn = cx.connect("test", "0000", "127.0.0.1:1521/XE")
        cur = conn.cursor()

        cur.executemany(sql, list)

        cur.close()
        conn.commit()
        conn.close()


# ----------------------------------------
    def 함수이름(self):
        # sql = """ delete from emp where deptno = :1 """
        sql = """ delete from emp where empno = :1 """

        conn = cx.connect("test", "0000", "127.0.0.1:1521/XE")
        cur = conn.cursor()

        cur.executemany(sql, list)

        cur.close()
        conn.commit()
        conn.close()