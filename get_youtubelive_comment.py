# -*- coding: utf-8 -*-
from package1 import get_live_comment3
from package1 import read_json_comment
from package1 import coeuter
# from package1 import *


def fuuso(target_urls, absolute_path):
    for target_url in target_urls:
        get_live_comment3.get_comment(target_url, absolute_path)

def main():
    #
    target_urls = ['https://www.youtube.com/watch?v=ljA6mKiTQuc',
                   'https://www.youtube.com/watch?v=VVQdAdUdowE',
                   ]
    # ファイルを保存する場所
    absolute_path = "D:\comments"

    
    coe = coeuter.Coeuter()
    channel_url = 'https://www.youtube.com/channel/UCXTpFs_3PqI41qX2d9tL2Rw'
    x = 55000
    print(coe.mninj(channel_url,x))# 戻り値は(list)

    # fuuso(target_urls, absolute_path)

    # グラフ表示したいtarget_urlをしたに入れる
    # read_json_comment.show_graph(target_url, file_name, absolute_path)
    target_url = 'https://www.youtube.com/watch?v=ljA6mKiTQuc'
    # read_json_comment.show_graph(target_url, absolute_path)

if __name__ == "__main__":
    main()
    #pip install pyautogui
