# -*- coding:utf-8 -*-
''' hbase 测试程序
	
	使用happybase导入phones.csv文件到hbase。
	
'''
__author__ = 'cleland'
import time
import csv
import sys
import happybase

reload(sys)
sys.setdefaultencoding("utf-8")


HOST = 'localhost'
BATCH_SIZE = 1024


def connnection(host):
	conn = happybase.Connection(host)
	return conn


def load(path):
	file_handler = open(path, 'r')
	reader = csv.reader(file_handler)
	return reader, file_handler


def store_in_hbase(conn, csv_reader):
	table = conn.table('phones')
	batch = table.batch(batch_size=BATCH_SIZE)
	error_list = []

	try:
		count = 0
		for row in csv_reader:
			batch.put(row[0], {
				'data:phone': row[1],
				'data:province': row[2]
			})
			count += 1
	except Exception as e:
		print str(e)
		error_list.append(str(e))
	finally:
		print 'insert {} rows'.format(count)

	for index, error in enumerate(error_list):
		print 'Exception {0}: {1}'.format(index+1, error)
	

def main():
	start_time = time.time()
	path = 'phones.csv'
	conn = connnection(HOST)
	csv_reader, file_handler =load(path)
	store_in_hbase(conn, csv_reader)
	file_handler.close()
	print 'spend time: {}'.format(time.time()-start_time)


if __name__ == '__main__':
	main()

