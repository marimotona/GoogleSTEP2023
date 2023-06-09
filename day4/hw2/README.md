## wikipedia.py

#### 考え方
1. 全てのノードに初期値として、1.0を渡す<br>
2. 各ノードに分配を行う<br>
　・各ノードに、0.85の割合で振り分けていく<br>
　・残りのノードは全ノードに均等に分配する<br>
3. 各ノードの合計値を更新していく<br>
4. これらを、値が収束するまで繰り返す<br>
5. ページのランクが高い上位10個を出力する

#### コード解説
```
popular = {id: 1.0 for id in self.titles.keys()}
```
全てに初期値1.0を振り分ける

```
share_ratio = 0.85
length = len(self.titles)
```
振り分ける割合の定義

```
for _ in range(100):
  new_popular = {id: (1.0 - share_ratio) / length for id in self.titles.keys()}
  for id, score in popular.items():
      if self.links[id]:
          distribute = share_ratio * score / len(self.links[id])
          for node in self.links[id]:
              new_popular[node] += distribute
      else:
          distribute = score / length
          for node in self.titles.keys():
              new_popular[node] += distribute
   popular = new_popular
   
   top_pages = heapq.nlargest(10, popular.items(), key=lambda x: x[1])
   for id, score in top_pages:
       print(f'ID: {id}, popular: {score}')
   pass
```
(1.0 - share_ratio) / lengthを等しく、それぞれのノードに最初に分配しておく<br><br>

popularの辞書をループし、各ページのidを取得してくる<br><br>

現在のページがリンクを持っている場合、<br>
そのリンク先に、それぞれスコアを分散していく<br><br>

もし、現在のページがリンクを持っていない場合は、<br>
持っているスコアをすべてに分散していく<br><br>
```
popular = new_popular
```
更新した新しいスコアを、保存する

```
top_pages = heapq.nlargest(10, popular.items(), key=lambda x: x[1])
```
popular辞書の中のx[1](score)を比較対象とし、比較を行い<br>
上位10個の要素をtop_pagesリストに格納する<br><br>

最後に、ループを回し、上位10個のページを表示する


