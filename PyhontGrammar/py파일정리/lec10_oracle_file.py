#module name : lec10_oracle_file.py
#file name : ./lec10_oracle_file.txt
#file,for, excute ,excutemany, cx-oracle-insert
#파일의 내용을 db에 입력
# str ="7521	WARD	SALESMAN	7698	81/02/22	1250	500	30"
# list = str.split()
# print(list)
import cx_Oracle as cx

list = []
with open('./lec10_oracle_file.txt', 'r') as f:
    while True:
        line = f.readline()
        if bool(line) == False:  #더이상 읽을게 없으면 나와라
            break

        line_list = line.split("\t")

        for i, word in enumerate(line_list):
            line_list[i] = word.strip('\n')
            if bool(word) == False:
                 line_list[i] = '0'
        #print(len(line_list)  ,  line_list)
        list.append(line_list)

print(list)


conn = cx.connect("test", "0000", "localhost:1521/XE")
cur = conn.cursor()
sql = """INSERT INTO EMP2 VALUES
   (to_number(:1),:2,:3,to_number(:4),to_date(:5,'yyyy-mm-dd')
   ,to_number(:6),to_number(:7),to_number(:8))
     """
cur.executemany(sql,list)
cur.close()
conn.commit()
conn.close()




# INSERT INTO EMP2 VALUES
# (to_number('7654'),'MARTIN','SALESMAN',to_number('7698'),to_date('1981-04-02','yyyy-mm-dd')
#  , to_number('1250'),to_number('1400'),to_number('30'));
# INSERT INTO EMP2 VALUES
# (to_number(:1),:2,:3,to_number(:4),to_date(:5,'yyyy-mm-dd')
#  , to_number(:6),to_number(:7),to_number(:8))







# db------->파일에다가 입력
# file name : dept 테이블값을 읽어서
# ./lec10_oracle_dept.txt 여기다가 써라