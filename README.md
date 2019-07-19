## About This Repository

**Please follow the restrictions in Apache-2.0 Licence before you refer to this repository.** 

**@Ming Jin** (*mingj2@student.unimelb.edu.au*)

This repository is a simple NLP project for beginners and will be updated occasionally.

Environment: Python3.6

**Pull requests are always welcome!**

To-do list:
1. Sentiment analysis can be done by using LSTM.
2. Crawler can be improved based on some libraries like BeautifulSoup.

## Introduction

这是一个微博评论分析工具，实现功能主要有：
1. 微博评论数据爬取
2. 分词与关键词提取
3. 词云与词频统计
4. 情感分析
5. 主题聚类

正常状态下实现效果在: “ 案例：泰国大象踩踏伤人事件 ”
注意：案例中最后表格需要自己根据LDA结果进行统计

This is a Weibo comments processing toolbox, which has been implemented for:

1. Weibo comments crawler that based on regular expression
2. Tokenization, filtration and key words extraction
3. Words cloud and visualization
4. Sentiment analysis
5. Topic clustering that based on LDA


## Pre-Requirements Checklist

*MySQL is required (e.g., You may use MySQL Workbench)*

1. importlib
2. sys
3. time
4. requests
5. lxml
6. pymysql
7. jieba
8. PIL
10. wordcloud
11. snownlp
12. logging
13. configparser
14. random
15. codecs


## Citing The Code

BibTex reference format:
```
@misc{WeiboAnalyst,
title={Weibo-Analyst: An Open-Source Python Library for Social Media Comments Analysis},
url={https://github.com/KimMeen/Weibo-Analyst},
author={Ming Jin},
year={2018}
}
```
