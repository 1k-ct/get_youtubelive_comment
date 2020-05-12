import os
import sys
import json

import requests
from bs4 import BeautifulSoup
from collections import defaultdict


comment_list = []
comment_time_dic = {}
user_name_and_comment = defaultdict(list)
def get_comment(target_url, absolute_path):
    
    comment_data = []
    dict_str = ''
    next_url = ''
    session = requests.Session()
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

    
    user_name_and_comment = defaultdict(list)
    # 動画ページにrequestsを実行，htmlソースを入手し，live_chat_replayの先頭urlを入手
    try:
        html = requests.get(target_url)
    except Exception as e:
        print(e)
        sys.exit()

    soup = BeautifulSoup(html.text, 'html.parser')

    for iframe in soup.find_all('iframe'):
        if 'live_chat_replay' in iframe['src']:
            next_url = iframe['src']

    while True:
        html = session.get(next_url, headers=headers)
        soup = BeautifulSoup(html.text, 'lxml')

        # 次に飛ぶurlのデータがある部分をfind_allで探してsplitで整形
        for scrp in soup.find_all('script'):
            if 'window["ytInitialData"]' in scrp.text:
                dict_str = scrp.text.split(' = ', 1)[1]

        # javascript表記を整形，falseとtrueの表記を直す
        dict_str = dict_str.replace('false', 'False')
        dict_str = dict_str.replace('true', 'True')

        # 辞書形式と認識するとかんたんにデータを取得できるが，末尾に邪魔なのがあるので消しておく（「空白2つ + \n + ;」を消す）
        dict_str = dict_str.rstrip('  \n;')
        # 辞書形式に変換
        try:
            dics = eval(dict_str)
            
        except Exception:
            with open('error_dict_str.txt', 'w') as f:
                f.write(dict_str)
            with open('error_soup.txt', 'w') as f:
                f.write(str(soup))
            print('コメントの変換に失敗しました')
            print(sys.exc_info()[0])
            sys.exit()

        # 'https://www.youtube.com/live_chat_replay?continuation=' + continue_url が次のlive_chat_replayのurl
        # 次のurlが取得できなければ終了
        try:
            continue_url = dics['continuationContents']['liveChatContinuation'][
                'continuations'][0]['liveChatReplayContinuationData']['continuation']
        except Exception:
            break
        next_url = 'https://www.youtube.com/live_chat_replay?continuation=' + continue_url

        # dics['continuationContents']['liveChatContinuation']['actions']がコメントデータのリスト．先頭はノイズデータなので[1:]で保存

       
        for samp in dics['continuationContents']['liveChatContinuation']['actions'][1:]:
            d = {}

            try:
                samp = samp['replayChatItemAction']['actions'][0]['addChatItemAction']['item']
                chat_type = list(samp.keys())[0]
                if 'liveChatTextMessageRenderer' == chat_type:
                    # 通常チャットの処理
                    if 'simpleText' in samp['liveChatTextMessageRenderer']['message']:
                        d['message'] = samp['liveChatTextMessageRenderer']['message']['simpleText']
                        
                    else:
                        d['message'] = ''
                        for elem in samp['liveChatTextMessageRenderer']['message']['runs']:
                            if 'text' in elem:
                                d['message'] += elem['text']
                                
                            else:
                                d['message'] += elem['emoji']['shortcuts'][0]
                                
                    # t = samp['liveChatTextMessageRenderer']['timestampText']['simpleText']
                    
                    d['id'] = samp['liveChatTextMessageRenderer']['authorExternalChannelId']
                    
                elif 'liveChatPaidMessageRenderer' == chat_type:
                    # スパチャの処理
                    if 'simpleText' in samp['liveChatPaidMessageRenderer']['message']:
                        d['message'] = samp['liveChatPaidMessageRenderer']['message']['simpleText']
                        
                    else:
                        d['message'] = ''
                        for elem in samp['liveChatPaidMessageRenderer']['message']['runs']:
                            if 'text' in elem:
                                d['message'] += elem['text']
                                
                            else:
                                d['message'] += elem['emoji']['shortcuts'][0]
                    
                    # コメントした時間           
                    # t = samp['liveChatPaidMessageRenderer']['timestampText']['simpleText']
                    #d['timestamp'] = convert_time(t)
                    d['id'] = samp['liveChatPaidMessageRenderer']['authorExternalChannelId']
                    
                elif 'liveChatPaidStickerRenderer' == chat_type:
                    # コメントなしスパチャ
                    continue
                
                elif 'liveChatLegacyPaidMessageRenderer' == chat_type:
                    # 新規メンバーメッセージ
                    continue
                
                elif 'liveChatPlaceholderItemRenderer' == chat_type:
                    #print('分類なしのもの')
                    continue
                
                else:
                    #print('知らないチャットの種類' + chat_type)
                    continue
                
                user_name = samp['liveChatTextMessageRenderer']['authorName']['simpleText']
                comment_time = samp['liveChatTextMessageRenderer']['timestampText']['simpleText']
                some_comment = d['message']


                comment_list.append(some_comment)
                user_name_and_comment['{}'.format(user_name)].append(some_comment)

                comment_time_dic['{}'.format(some_comment)] = comment_time
                
                #print(comment_list)
                
                #ここ重要
               
            except Exception:
                continue
            
      
    #print(user_name_and_comment)
    file_name = target_url.split('=')[1]
    print('コメント数: {}'.format(len(comment_list)))
    with open("{}/{}.json".format(absolute_path, file_name), "w", encoding="utf-8_sig") as f:
        json.dump(user_name_and_comment, f, ensure_ascii=False, indent=4)
    
    return comment_data
