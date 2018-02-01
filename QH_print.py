#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2018 XXX. All Rights Reserved.
# Author:  joanwelol@gmail.com
# QH_print.py 2018/1/25 22:20
# desc:
import json
from prettytable import PrettyTable

table = PrettyTable(['答案选项', '结果总数', '词频计数'])
table.align['答案选项'] = 'l'


# 打印表格
def print_table(value):
    value = json.loads(value)
    title = value['title']
    letters = ['1.', '2.', '3.']
    recommend = value['recommend']
    result = value['result']
    summary = value['search_infos'][0]['summary']
    for i in value['answers']:
        if i in summary:
            # 打印绿色高亮字体    '\033[0;32m' +  + '\033[0m'
            summary = summary.replace(i, '\033[0;32m' + i + '\033[0m')
    print('\b' * 24, end='', flush=True)  # 删除前面打印字符
    print(title)
    print(table)
    if value['recommend'] == '啊呀，这题汪仔还在想':
        print('推荐答案:', '-->' + result + '<--')
    else:
        print('推荐答案:', '-->' + recommend + '<--')
    print('参考:', summary)
    print('\n')
