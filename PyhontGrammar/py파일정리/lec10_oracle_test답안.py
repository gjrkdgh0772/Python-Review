# lec10_oracle_test.py

# 
# DDL
# 
# drop table test;
# create table test(
# seq number,
# name varchar2(20),
# pw  number(10));

# 
# Test 테이블 CRUD
# 
import cx_Oracle as cx

# # 다음 두건의 데이터 동시 입력
# def test_insert(list):
#     conn = cx.connect("ai", "0000", "localhost:1521/XE")
#     cur = conn.cursor()
#     sql = "insert into test values(:1,:2,:3)"
#     cur.executemany(sql, list)
#     cur.close()
#     conn.commit()
#     conn.close()
# list = [[1,'aa','111'],
#         [2,'bb','222']
#        ]
# test_insert(list)


# aa 정보 출력 > [1,'aa','111']
# def test_select(name) :
#     conn = cx.connect("ai", "0000", "localhost:1521/XE")
#     cur = conn.cursor()
#     sql = "select * from test where name=:1"
#     cur.execute(sql, [name])
#     for c in cur:
#         print(c)
#     cur.close()
#     conn.close()
# test_select('aa')

#
# # aa 비번 333로 변경
# # bb 비번 444로 변경 > [1,'aa','333']  [2,'bb','444']
#
# def test_update(list):
#     conn = cx.connect("ai", "0000", "localhost:1521/XE")
#     cur = conn.cursor()
#     sql = "update test set pw=:1 where name=:2"
#     cur.executemany(sql, list)
#     cur.close()
#     conn.commit()
#     conn.close()
#
# list = [ ['333', 'aa'],
#           ['444','bb' ]
#         ]
# test_update(list)
#
#
#aa 정보 삭제
def test_delete(name):
    conn = cx.connect("ai", "0000", "localhost:1521/XE")
    cur = conn.cursor()
    sql = "delete from test where name=:1"
    cur.execute(sql, [name])
    cur.close()
    conn.commit()
    conn.close()
test_delete('aa')