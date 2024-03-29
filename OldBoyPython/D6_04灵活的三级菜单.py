#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/1/8 0:39
# FileName: D6_04灵活的三级菜单.py
# Description:
#       1. 用户可以一层一层滴进入菜单；
#       2. 用户可以在每一层返回到上一层；
#       3. 用户可以在任意菜单中退出菜单选择
# Question:
# --------------------------------------
menu = {
    '北京': {
        '朝阳': {
            '国贸': {
                '中金': {},
                'CCTV': {},
                '渣打银行': {}
            },
            '望京': {
                '陌陌': {},
                '奔驰': {},
                '360': {}
            },
            '三里屯': {
                'Apple': {},
                '优衣库': {},
                '加拿大鹅': {}
            }
        },
        '海淀': {
            '后厂村': {
                '百度': {},
                '网易': {},
                '新浪': {}
            },
            '中关村': {
                '爱奇艺': {},
                '优酷': {},
                '优信二手车': {}
            },
            '五道口': {
                '北京大学': {},
                '清华大学': {},
                '中国人民大学': {}
            }
        },
        '昌平': {
            '沙河': {
                '沙河地铁站': {},
                '沙河公交站': {},
                '沙河大桥': {}
            },
            '回龙观': {
                '回龙观地铁站': {},
                '回龙观公交站': {},
                '回龙观街道办事处': {}
            },
            '天通苑': {
                '链家': {},
                '我爱我家': {},
                '绿地': {}
            }
        }
    },
    '上海': {
        '浦东区': {
            '陆家嘴': {
                "CICC": {},
                "高盛": {},
                "摩根士丹利": {}
            },
            '外滩': {
                "上海滩": {}
            }
        },
        '闵行区': {

        },
        '静安区': {

        }
    },
    '陕西省': {
        '西安': {
            '长安区': {
                '西安外国语大学': {},
                '西北政法大学': {},
                '西北大学': {}
            },
            '雁塔区': {
                '大雁塔': {},
                '小雁塔': {},
                '小寨': {}
            }
        },
        '渭南': {
            '临渭区': {}
        }
    }
}

while True:
    # 遍历最顶层的省级
    for key in menu:
        print("1_省级菜单：", key)

    # 根据打印情况，让用户选择
    choice = input("1_请选择>>：").strip()
    if choice in menu:
        while True:
            for key2 in menu[choice]:
                print("2_市级菜单：", key2)

            # 继续让用户进行选择
            choice2 = input("2_请选择市>>：").strip()
            if choice2 in menu[choice]:
                while True:
                    for key3 in menu[choice][choice2]:
                        print("3_区级菜单：", key3)

                    # 继续让用户进行选择
                    choice3 = input("3_请选择区>>：").strip()
                    if choice3 in menu[choice][choice2]:
                        while True:
                            for key4 in menu[choice][choice2][choice3]:
                                print("4_具体地点菜单：", key4)
                            # 继续让用户选择具体的地点
                            choice4 = input("4_选择地点>>：").strip()
                            if choice4 in menu[choice][choice2][choice3][choice4]:
                                print("您已经到达最小维度")


