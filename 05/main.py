#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

from dbconn import db_cursor


def write_grade(stu_no, cou_no, grade):
    """填写学生stu_no添加课程编号为cou_no的成绩"""

    with db_cursor() as cur : # 取得操作数据的游标，记为cur

        s = 'SELECT sn, name FROM student WHERE no=%(stu_no)s'
        cur.execute(s, dict(stu_no=stu_no))
        stu = cur.fetchone() # 仅读取第一行的数据，有两列(sn, name)
                             # 如果没有一行数据返回，则返回的是None
        if stu is None : 
            print('找不到学生(%s)' % stu_no)
            return

        s = 'SELECT sn, name FROM course WHERE no=%(cou_no)s'
        cur.execute(s, dict(cou_no=cou_no))
        cou = cur.fetchone() # 仅读取第一行的数据
        if cou is None :
            print('找不到课程(%s)' % cou_no)
            return

        s = """
        UPDATE course_grade SET
           grade = %(grade)s
        WHERE stu_sn = %(stu_sn)s AND cou_sn= %(cou_sn)s
        """
        cur.execute(s, dict(stu_sn=stu[0],
                    cou_sn=cou[0],
                    grade=grade))
        if cur.rowcount == 0:
            # rowcount, 最近一次执行SQL语句后所涉及的行数
            # 如果学生和课程都找到，则至少更新一条，
            # 反之，没找到可更新的，因此需要插入一条新的
            s = """
            INSERT INTO course_grade (stu_sn, cou_sn, grade)
                VALUES (%(stu_sn)s, %(cou_sn)s, %(grade)s)
            """
            cur.execute(s, dict(stu_sn=stu[0],
                                cou_sn=cou[0],
                                grade=grade))
            print('添加%s的%s成绩%.2f' % (stu[1], cou[1], grade))
        else:
            print('更新%s的%s成绩%.2f' % (stu[1], cou[1], grade))
            

def list_grades(stu_no):

    with db_cursor() as cur : 

        s = 'SELECT sn, name FROM student WHERE no=%(stu_no)s'
        cur.execute(s, dict(stu_no=stu_no))
        stu = cur.fetchone() 
        if stu is None : 
            print('找不到学生(%s)' % stu_no)
            

        s ='SELECT grade,cou_sn FROM course_grade WHERE stu_sn = %(stu_sn)s ORDER BY cou_sn'
        cur.execute(s,dict(stu_sn=stu[0]))
        for row in cur.fetchall():
            cou_sn=int(row[1])
            grade=row[0]
            print('{0}的序号为{1}的成绩是{2}'.format(stu[1],cou_sn,grade))
    

def delete_grades(stu_no, cou_no):
    

    with db_cursor() as cur :

        s = 'SELECT sn, name FROM student WHERE no=%(stu_no)s'
        cur.execute(s, dict(stu_no=stu_no))
        stu = cur.fetchone() 
        if stu is None : 
            print('找不到学生(%s)' % stu_no)
            return

        s = 'SELECT sn, name FROM course WHERE no=%(cou_no)s'
        cur.execute(s, dict(cou_no=cou_no))
        cou = cur.fetchone() 
        if cou is None :
            print('找不到课程(%s)' % cou_no)
            return

        s = """
        UPDATE course_grade SET
           grade = null
        WHERE stu_sn=%(stu_sn)s AND cou_sn= %(cou_sn)s
        """
        cur.execute(s,dict(stu_sn=stu[0],
                    cou_sn=cou[0]))
        print('已删除{0}的{1}的成绩'.format(stu[1],cou[1]))


  
if __name__ == '__main__':

    write_grade('S004', 'C01', 88.5)
    write_grade('S004', 'C02', 76.0)
    write_grade('S004', 'C03', 68.0)

    print('[1]' + '==' * 20)
    list_grades('S004')

    print('[2]' + '==' * 20)
    delete_grades('S004', 'C02')
    delete_grades('S004', 'C10')

    print('[3]' + '==' * 20)
    list_grades('S004')



    
