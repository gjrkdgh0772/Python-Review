import cx_Oracle as cx
# seq number,
# name varchar2(20),
# pw  number(10));
# --[1,'aa','111']
# --[2,'bb','222']
# --test_insert(list)
# --test_select(name)
# --aa 정보출력---->
# --test_update
# --aa  비번 333로 변경
# --bb 비번 444로 변경
# --
# --test_delete
# --aa정보삭제

def test_insert_many(test_list):
    sql = """insert into test (seq, name, pw)
            values (:1,:2,:3)"""  # 66,'CCC',10 값

    conn = cx.connect("test", "0000", "127.0.0.1:1521/XE")
    cur = conn.cursor()
    # cur.execute(sql,{"empno":777,"ename":'BBB',"deptno":10})
    cur.executemany(sql, test_list)
    cur.close()
    conn.commit()
    conn.close()

# list = [[1,'aa','111'],[2,'bb','222']]
# test_insert_many(list)
#     -----------------------------------------------
# def test_select(name):
#
#
#
#     conn = cx.connect("test", "0000", "127.0.0.1:1521/XE")
#     cur = conn.cursor()
#     sql = """select * from test where name = :1
#                         """
#     # cur.execute(sql,{"empno":777,"ename":'BBB',"deptno":10})
#     cur.execute(sql, [name])
#     for c in cur:
#
#         print(c) #()튜블 : 수정,삭제 못하게 하기위해서
#     cur.close()
#     conn.commit()
#     conn.close()
#
# test_select('aa')

# ----------------------------------------------------------------------------------
# def test_update(list):
#
#
#     conn = cx.connect("test", "0000", "127.0.0.1:1521/XE")
#     cur = conn.cursor()
#     sql = """update test
#                     set pw = :1
#                     where name = :2
#                     """
#     # cur.execute(sql,{"empno":777,"ename":'BBB',"deptno":10})
#     cur.executemany(sql, list)
#     cur.close()
#     conn.commit()
#     conn.close()
# #
# list = [['333','aa'],['444','bb']]
# test_update(list)


# def test_delete1(name):
#
#     # sql = """ delete from emp where empno in(:1,:2,:3)"""
#
#     conn = cx.connect("test", "0000", "127.0.0.1:1521/XE")
#     cur = conn.cursor()
#     sql = "delete from test where name = :1"
#     cur.execute(sql, [name])
#     cur.close()
#     conn.commit()
#     conn.close()




def test_delete(name):
    conn = cx.connect("test", "0000", "localhost:1521/XE")
    cur = conn.cursor()
    sql = "delete from test where name=:1"
    cur.execute(sql, [name])
    cur.close()
    conn.commit()
    conn.close()
test_delete('aa')