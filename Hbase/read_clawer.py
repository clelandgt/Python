# -*- coding:utf-8 -*-
"""	hbase 测试程序
将云爬虫中爬取的工商数据数据导入到hbase。

"""
import time
import sys
import json
import happybase
__author__ = 'cleland'

reload(sys)
sys.setdefaultencoding("utf-8")

HOST = 'localhost'
BATCH_SIZE = 1024


def connection(host):
    conn = happybase.Connection(host)
    return conn


def load(path):
    with open(path, 'r') as f:
        for line in f:
            yield json.loads(line)


def store_in_hbase(items, conn):
    start_time = time.time()
    error_list = []
    conn.open()
    table = conn.table('clawer')
    batch = table.batch(batch_size=BATCH_SIZE)
    try:
        count = 0
        for item in items:
            _id = item['_id']['$oid']
            batch.put(_id, {'data:content': str(item)})
            count += 1
    except Exception as e:
        print 'Exception: {}'.format(str(e))
        error_list.append(str(e))
    finally:
        batch.send()
        print 'insert {} rows'.format(count)
        print 'spend time: ', time.time() - start_time
        conn.close()

    if len(error_list) == 0:
        return
    for index, error in enumerate(error_list):
        print 'Exception {0}: {1}'.format(index + 1, error)


def main():
    path = 'json_test_data.json'
    conn = connection(HOST)
    items = load(path)
    store_in_hbase(items, conn)


if __name__ == '__main__':
    main()
