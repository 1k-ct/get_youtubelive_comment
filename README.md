# get_youtubelive_comment
# youtubeliveのコメントを取得  


  
* ファイルを保存する場所の設定
  * absolute_path = '絶対パス'  

#### *(1), &nbsp; youtube live のコメメントをjson形式で取得 &nbsp; (1,をインストール)*  
```Python:title
def mian():
    target_urls = ["動画url(https: ~ /watch?v=***********)",] # target_urlsはlist
                   
    fuuso(target_url, absolute_path)     
```
  
#### *(2), &nbsp; (1)を使ってグラフ描画 &nbsp; (2,をインストール)*  
```Python:title
def main():
    target_url = 'グラフで描画したい動画url'  
    read_json_comment.show_graph(target_url, absolute_path)  
````
  
#### *(3), &nbsp; youtubeで目的チャンネルの動画urlを全て取得 &nbsp; (3,をインストール)*  
```Python:title
def main():
    coe = coeuter.Coeuter()  
    channel_url = 'チャンネルのurl'  
    x = 55_000 # xはスクロール値。もし、最後まで動画が取得出来なければ'x'を適宜変更 (動画400個で55,000)
    print(coe.mninj(channel_url, x))
```

> ##### 1  
> pip install requests  
> pip install beautifulsoup4  
> pip install lxml  
  
>##### 2  
>pip install matplotlib  
>pip install japanize-matplotlib  
  
>##### 3  
>pip install pyautogui  
>pip install selenium  
  
_____  
 -  参考にさせて頂いたページ  
     - [Hatena Blog](http://watagassy.hatenablog.com/entry/2018/10/08/132939)  
