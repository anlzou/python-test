'''
    结果：error
'''
#统计谷歌浏览器访问历史记录
import os
import sqlite3
import operator
from collections import OrderedDict

def parse(url):
    try:
        parsed_url_components = url.split('//')
        sublevel_split = parsed_url_components[1].split('/',1)
        domian = sublevel_split[0].replace('www.','')
        return domian
    except IndexError:
        print('URL format error!!')

if __name__ == '__main__':
    #指到用户的谷歌浏览器的历史记录
    data_path = r'C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\Default'
    files = os.listdir(data_path)
    history_db = os.path.join(data_path,'history1')

    #查询数据库内容
    conn = sqlite3.connect(history_db)
    cursor = conn.cursor()
    #select_statement_queryall = 'SELECT * FROM urls;'
    select_statement_query = 'SELECT urls.url,urls.visit_count FROM urls,visits WHERE urls.id=visits.url;'
    #select_statement_delete_id = ' DELETE FROM urls;'#清空urls表的所有的数据
    #cursor.execute(select_statement_delete_id)
    #conn.commit
    #cursor.execute(select_statement_queryall)
    cursor.execute(select_statement_query)
    results = cursor.fetchall()
    #for d in results:
        #print("ID: "+str(d[0])+'\t'+"URL: "+str(d[1])+"\t"+"Title: "+str(d[2])+'\t'+"visit_count: "+str(d[3])+'\t'+"typed_count: "+str(d[4])+'\t'+"last_visit_time: "+str(d[5])+'\t'+"hiddlen: "+str(d[6])+'\t')

    sites_count = {}#定义为字典

    for url,count in results:
        #print(url)
        #print(count)
        url = parse(url)
        if url in sites_count:
            sites_count[url] += 1
        else:
            sites_count[url] = 1
    sites_count_sorted = OrderedDict(sorted(sites_count.items(),key=operator.itemgetter(1),reverse=True))
    print(sites_count_sorted)