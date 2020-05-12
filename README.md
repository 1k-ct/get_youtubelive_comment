# get_youtubelive_comment
# youtubeliveのコメントを取得  

##### 1  
pip install requests  
pip install beautifulsoup4  
pip install lxml  
  
##### 2  
pip install matplotlib  
pip install japanize-matplotlib  
  
##### 3  
pip install pyautogui  
  
absolute_path = '絶対パス'  

#### *(1),youtube live のコメメントをjson形式で取得(1,をインストール)*  
- target_urls = ["動画url(https: ~ /watch?v=)",]    
- fuuso(target_url, absolute_path)   
#target_urlsはlist  
  
#### *(2),(1)を使ってグラフ描画(2,をインストール)*  
- target_url = 'グラフで描画したい動画url'  
- read_json_comment.show_graph(target_url, absolute_path)  
  
#### *(3),youtubeで目的チャンネルの動画urlを全て取得(3,をインストール)*  
- coe = coeuter.Coeuter()  
- channel_url = 'チャンネルのurl'  
- x = 55_000(動画400個で55,000。もし、最後まで動画が取得出来なければ'x'を適宜変更)  
- print(coe.mninj(channel_url, x))  
  
______  
- 参考にさせて頂いたページ
　　- [Hatene Blog] (http://watagassy.hatenablog.com/entry/2018/10/08/132939)
