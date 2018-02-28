#!/usr/bin/env python3
import sys
import csv
import MySQLdb

# CSV 파일 입력 경로
input_file = sys.argv[1]

# MySQL 데이터베이스에 접속한다.
con = MySQLdb.connect(host = "localhost", port = 3306, db = "my_suppliers", user = "root", passwd = "1234")
c = con.cursor()

# CSV 파일을 읽고 특정 행을 갱신한다.
file_reader = csv.reader(open(input_file, 'r', newline=''), delimiter = ',')
header = next(file_reader)
for row in file_reader :
    data = []
    for column_index in range(len(header)) :
        data.append(str(row[column_index]).strip())
    print(data)
    c.execute("""UPDATE Suppliers SET Cost=%s, WHERE Supplier_Name=%s;""", data)
con.commit()

# Suppliers 테이블에 질의한다.
c.execute("SELECT * FROM Suppliers")
rows = c.fetchall()
for row in rows :
    output = []
    for column_index in range(len(row)) :
        output.append(row[column_index])
    print(output)

print("Program End.")
