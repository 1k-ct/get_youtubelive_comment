import json

import matplotlib.pyplot as plt
import japanize_matplotlib


def show_graph(target_url, absolute_path):#グラフを表示する
    file_name = target_url.split('=')[1]
    json_open = open("{}/{}.json".format(absolute_path, file_name), "r", encoding="utf-8_sig")
    json_load = json.load(json_open)
    # ユーザー1人のコメント(辞書)
    user_comment_counter = {}
    for k in json_load:
        user_comment_counter["{}".format(k)] = len(json_load["{}".format(k)])
    # ソート
    user_comment_counter_sorted = sorted(user_comment_counter.items(), key=lambda x:x[1], reverse=True)
    
    user_name = [i[0] for i in user_comment_counter_sorted]
    comment_count_list = [i[1] for i in user_comment_counter_sorted]

    height2 = comment_count_list
    left2 = [x for x in range(0,len(json_load))]
    
    height1 = comment_count_list[0:10]
    left1 = [x for x in range(0,10)] 

    labels = user_name[0:10]
    plt.subplot(2,1,1)
    plt.barh(left1, height1, tick_label=labels)

    plt.title("一人がコメントした回数")

    plt.subplot(2,1,2)
    plt.scatter(height2, left2, marker='.')

    plt.xlabel("コメント数")
    plt.ylabel("順位,人数({})".format(len(json_load)))

    plt.grid()
    plt.show()
