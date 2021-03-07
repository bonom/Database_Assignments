#!/usr/bin/env python3

# MAT: 201487

size_tuple = 10**6

import psycopg2
import psycopg2.extras

from math import isclose
import psycopg2
import time
import string
import random
import sys
import io
import csv

# Random string generator, parametro size gestisce la grandezza della stringa
def string_random(size):
	return ''.join(random.sample(string.ascii_uppercase+string.digits,size))

# Stampa ordinata e sequenziale dei Times Required per ogni step
def step_print(a,b,x):
	b = b - a
	b = b * (10**9)
	print("Step "+str(x)+" needs "+ str(int(round(b))) + " ns")

# Stampa ordinata in formato CSV per la stampa su stderr
def result_print(result_rows,column):
	if column == 1:
		for result_row in result_rows:
			print(result_row[0],file=sys.stderr)
	else:
		for result_row in result_rows:
			print(str(result_row[0])+","+str(result_row[1]),file=sys.stderr)

conn = psycopg2.connect("dbname=db_024 user=db_024 host=sci-didattica.unitn.it password=provapassword")
cur = conn.cursor()
conn.autocommit = True
try:

	# Liste di salvataggio dei tempi di inizio / fine sviluppo dei tempi da stampare
	take = []
	final = []

	# ------ Step 1 ------

	take.append(time.time())
	cur.execute("DROP TABLE IF EXISTS Professor CASCADE;")
	cur.execute("DROP TABLE IF EXISTS Course CASCADE;")
	conn.commit()
	final.append(time.time())

	step_print(take[0],final[0],1)

	# ------ Step 2 ------

	take.append(time.time())
	cur.execute("CREATE TABLE Professor (id INTEGER PRIMARY KEY NOT NULL,name CHAR(50) NOT NULL,address CHAR(50) NOT NULL,age INTEGER NOT NULL,height REAL NOT NULL);")
	cur.execute("CREATE TABLE Course (cid CHAR(25) PRIMARY KEY NOT NULL,title CHAR(50) NOT NULL,area CHAR(30) NOT NULL,instructor INTEGER NOT NULL REFERENCES professor);")
	conn.commit()
	final.append(time.time())

	step_print(take[1],final[1],2)

	# ------ Step 3 ------

	take.append(time.time())

	height = 0.0
	data = []
	number = []

	for x in range((size_tuple)-1):
		height = height + 0.001
		if isclose(height,185,abs_tol=1e-3):
			height = height + 0.01
		number.append((x+1,height))

	random.shuffle(number)

	data.append((1,2,3,4,5))

	for x in range(len(number)):
		data.append( (number[x][0], string_random(8), string_random(10), random.randint(18,80), str(number[x][1])) )

	number.append(size_tuple)
	data.append((number[len(number)-1], string_random(8), string_random(10), random.randint(18,80), 185.0))

	string_buffer = io.StringIO()
	writer = csv.writer(string_buffer, delimiter = ';', quoting = csv.QUOTE_MINIMAL)

	writer.writerows(data)
	string_buffer.seek(0)

	statement = "COPY {table} FROM STDIN DELIMITER '"'{deli}'"' {file_type} HEADER;".format(table = 'Professor',from_file = string_buffer,deli = ';', file_type = 'csv')
	cur.copy_expert(statement, string_buffer)

	final.append(time.time())

	step_print(take[2],final[2],3)

	# ------ Step 4 ------

	take.append(time.time())

	data = []
	course = set()

	data.append((1,2,3,4))

	while len(course)!=size_tuple:
		course.add(string_random(10))

	courses = []
	for t in course:
		courses.append(t)

	for x in range(len(courses)-1):
		data.append( (courses[x], string_random(5), string_random(5), number[random.randint(0,size_tuple-2)][0]) )
		if x+1 % 200000 == 0:
			string_buffer = io.StringIO()
			writer = csv.writer(string_buffer, delimiter = ';', quoting = csv.QUOTE_MINIMAL)

			writer.writerows(data)
			string_buffer.seek(0)

			statement = "COPY {table} FROM STDIN DELIMITER '"'{deli}'"' {file_type} HEADER;".format(table = 'Course',from_file = string_buffer,deli = ';', file_type = 'csv')
			cur.copy_expert(statement, string_buffer)

			data = []
			data.append((1,2,3,4))

	if(len(data) > 1):
		string_buffer = io.StringIO()
		writer = csv.writer(string_buffer, delimiter = ';', quoting = csv.QUOTE_MINIMAL)

		writer.writerows(data)
		string_buffer.seek(0)

		statement = "COPY {table} FROM STDIN DELIMITER '"'{deli}'"' {file_type} HEADER;".format(table = 'Course',from_file = string_buffer,deli = ';', file_type = 'csv')
		cur.copy_expert(statement, string_buffer)

	final.append(time.time())

	step_print(take[3],final[3],4)

	# ------ Step 5 ------

	take.append(time.time())
	cur.execute("SELECT id FROM professor;")
	results = cur.fetchall()
	result_print(results,1)
	final.append(time.time())

	step_print(take[4],final[4],5)

	# ------ Step 6 ------

	take.append(time.time())
	cur.execute("UPDATE professor SET height = 200.0 WHERE height = 185.0;")
	final.append(time.time())

	step_print(take[5],final[5],6)

	# ------ Step 7 ------

	take.append(time.time())
	cur.execute("SELECT id,address FROM professor WHERE height = 200.0;")
	results = cur.fetchall()
	result_print(results,2)
	final.append(time.time())

	step_print(take[6],final[6],7)

	# ------ Step 8 ------

	take.append(time.time())
	cur.execute("CREATE INDEX height_btree ON professor USING btree (height);")
	final.append(time.time())

	step_print(take[7],final[7],8)

	# ------ Step 9 ------

	take.append(time.time())
	cur.execute("SELECT id FROM professor;")
	results = cur.fetchall()
	result_print(results,1)
	final.append(time.time())

	step_print(take[8],final[8],9)

	# ------ Step 10 ------

	take.append(time.time())
	cur.execute("UPDATE professor SET height = 210.0 WHERE height = 200.0;")
	final.append(time.time())

	step_print(take[9],final[9],10)

	# ------ Step 11 ------

	take.append(time.time())
	cur.execute("SELECT id,address FROM professor WHERE height = 210.0;")
	results = cur.fetchall()
	result_print(results,2)
	final.append(time.time())

	step_print(take[10],final[10],11)

finally:
	cur.close()
	conn.close()