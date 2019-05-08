#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/5/8 12:01
# FileName: 05_Interface_testcase.py
# Description: 以百度翻译的查询接口为例
# Question: 
# --------------------------------------

import requests
import unittest
import random
import hashlib
import urllib
import json

word = input('请输入你要翻译的词语：')

class BaiduTranslate(unittest.TestCase):

    def setUp(self) -> None:
        # url = 'http://fanyi.baidu.com/v2transapi'
        self.q = word
        self.fromLang = 'en'
        self.toLang = 'zh'

        my_url = '/api/trans/vip/translate'
        self.appid = '20190508000295298'
        self.secretKey = 'SpZnEM6HliTHK1Mlp96I'
        self.salt = random.randint(32768, 65536)
        self.sign = self.appid + self.q + str(self.salt) + self.secretKey

        m1 = hashlib.md5()
        m1.update(self.sign.encode('utf-8'))
        self.sign = m1.hexdigest()
        self.my_url = my_url + '?appid=' + self.appid + '&q=' + urllib.request.quote(self.q) + '&from=' + \
                      self.fromLang + \
                      '&to=' + self.toLang + '&salt=' + str(self.salt) + '&sign=' + self.sign

    def test_translate(self):
        # 百度翻译的示例文档中用的是 urllib 库，建议使用第三方库 requests 方便点
        r = requests.request('post', url='http://api.fanyi.baidu.com' + self.my_url)
        print('\nr_text_type: ', type(r.text))
        print('r_text: ', r.text)
        r_json = json.loads(r.text)
        print('r_json_type: ', type(r_json))
        print('r_json: ', r_json)
        # 截取翻译结果
        translate_result = r_json["trans_result"]
        print('translate_result_type: ', type(translate_result))

        for i in translate_result:
            # print('translate_result: ', type(i))
            print('translate_result: ', i['dst'])

    def tearDown(self) -> None:
        print("测试固件销毁......")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(BaiduTranslate)
    with open('BaiduTranslate_TestReporter.html', 'a') as f:
        runner = unittest.TextTestRunner(verbosity=2, stream=f)
        runner.run(suite)