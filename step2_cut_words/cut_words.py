#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 18:51:48 2017
@author: Ming JIN
"""
import jieba
#import string
#import sys
#import os
import pymysql

jieba.load_userdict("SogouLabDic.txt")
jieba.load_userdict("dict_baidu_utf8.txt")
jieba.load_userdict("dict_pangu.txt")
jieba.load_userdict("dict_sougou_utf8.txt")
jieba.load_userdict("dict_tencent_utf8.txt")
jieba.load_userdict("my_dict.txt")

stopwords = {}.fromkeys([ line.rstrip() for line in open('Stopword.txt') ])

def get_data(index_news):
    
    print("连接MySql数据库...")
    
    db = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='请输入自己的密码',db='2017_database',charset='utf8',cursorclass = pymysql.cursors.DictCursor)
 
    cursor = db.cursor()

    sql_1 = "select comment_num from ID" + str(index_news) + " where comment_num=(select max(comment_num) from ID" + str(index_news) + ")"

    cursor.execute(sql_1)
    
    index1 = cursor.fetchall()
    
    index = index1[0]['comment_num']
    
    print("正在解析数据...")
    
    for n in range(1,index):
        
        result = []
   
        sql_2 = "select comment from ID" + str(index_news) + " where comment_num=" + str(n)
        cursor.execute(sql_2)
        result_middle_1 = cursor.fetchall()
        result_middle = result_middle_1[0]['comment']
   
        seg = jieba.cut(result_middle)

        for i in seg:
            
            if i not in stopwords:  
              
                result.append(i)

        fo = open("data_full.dat", "a+")
        #fo = open("/Users/kimmeen/Downloads/P_Weibo/%s"%user_id, "w")

        for j in result:
          
           fo.write(j)
           fo.write(' ')
     
        fo.write('\n')
        fo.close()
        n += 1
    
    db.close()
    print("解析完成!")

if __name__ == '__main__':
    
    total_news = 11
    print("进程开始...")
    for index_news in range(1,total_news):
        
        get_data(index_news)
        
    print("Done!")






