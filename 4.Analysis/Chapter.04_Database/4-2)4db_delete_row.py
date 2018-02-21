#!/usr/bin/env python3
import sys
import csv
import sqlite3

# CSV 입력 파일의 경로와 파일명
input_file = sys.argv[1]

# 메모리에 sqlite3 데이터베이스를 만든다.
# 다섯 가지 속성을 지닌 Supplier 테이블을 만든다.
con = sqlite3.connect("Supplier_del.db")
con_cursur = con.cursor()
create_table = """CREATE TABLE IF NOT EXISTS Suppliers
(Supplier_Name VARCHAR(20),
Invoice_Number VARCHAR(20),
Part_Number VARCHAR(20),
Cost FLOAT,
Purcharse_Date DATE);"""
con_cursur.execute(create_table)
con.commit()

# CSV 파일을 읽는다.
# 읽은 데이터를 Suppliers 테이블에 삽입한다.
file_reader = csv.reader(open(input_file, 'r'), delimiter = ',')
header = next(file_reader, None)
for row in file_reader :
    data = []
    for column_index in range(len(header)) :
        data.append(row[column_index])
    print(data)
    con_cursur.execute("INSERT INTO Suppliers VALUES(?, ?, ?, ?, ?);", data)
con.commit()
print("")

delete_data = "DELETE FROM Suppliers WHERE Supplier Name = 'Supplier Z'"
con_cursur.execute(delete_data)

# Suppliers 테이블에 질의한다.
output = con_cursur.execute("SELECT * FROM Suppliers")
rows = output.fetchall()
for row in rows :
    output = []
    for column_index in range(len(row)) :
        output.append(str(row[column_index]))
    print(output)

print("Program End.")
