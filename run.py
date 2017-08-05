#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author: liyinwei
@E-mail: coridc@foxmail.com
@Time: 2017/8/1 19:40
@Description: export xuexi.xxxx.com qa
"""

import json

"""
input.json @see browser F12, a json format string from:
https://xuexi.xxxx.com/app/module/report?mod_id=15952&tkh_id=275446&isMobile=false
"""
file = open('input.json', 'rb')

data = json.load(file)

body = data["hashMap"]["student"][0]["test"][0]["body"][0]
questions = body["question"]

result = []

for q in questions:
    # 1. 题目标题
    title = q["body"][0]["html"][0]["text"]

    # 2. 题目选项对象集合
    obj_options = q["body"][0]["interaction"][0]["option"]
    # 题目选项集合
    options = {}
    for o in obj_options:
        options[o["id"]] = o["html"][0]["text"]

    # 3. 题目答案对象集合
    obj_outcomes = q["outcome"][0]["feedback"]
    outcomes = []
    for o in obj_outcomes:
        if o.get("score") is not None:
            outcomes.append(options[o["condition"]])

    qa = {"question": title, "answer": outcomes}
    result.append(qa)

# 导出答案
with open("output.json", 'w', encoding='utf8') as f:
    f.write(json.dumps(result, ensure_ascii=False))

if __name__ == '__main__':
    pass
