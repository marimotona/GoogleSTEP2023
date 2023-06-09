## wikipedia.py

##### テーマ：最短経路を見つける

##### 考え方：
キューに探索したいノードと、そこまでの経路を入れていく<br>
既に調べたものはSetオブジェクトに保存しておく<br>
全ての可能なノードを調べていく<br>
もし、現在のノードが目的のノードだった場合、そのノードまでの経路を出力する


##### コード解説：
```
for id, title in self.titles.items():
    if title == start:
        start_id = id
    if title == goal:
        goal_id = id
```
スタートとゴールのノードを探してくる<br>
self.titlesディクショナリに保存されているところから探してくる
<br>

```
visited = set()
queue = collections.deque([(start_id, [])])
```
既に探索したノードを記録する、Setオブジェクトを定義する<br>
探索すべきノードを保存するためのキューを定義する


```
while queue:
     (curr_node, path) = queue.popleft()
     if curr_node not in visited:
         visited.add(curr_node)
         path = path + [curr_node]

         if curr_node == goal_id:
             shortest_path =  [self.titles[i] for i in path]
             print('shortest path :')
             for page in shortest_path:
                 print(page)
             return shortest_path
                
         for next_node in self.links[curr_node]:
             if next_node not in visited:
                 queue.append((next_node, path))
        pass
```

キューに探索するべきノードが存在する限りループを回す<br>
キューから、現在のノードと、それまでの経路を取り出す<br><br>

もし取り出したノードが、探索されていなかった場合、<br>
キューをSetオブジェクトに保存する<br>
pathという、経路を保存する変数に、<br>
これまでの経路と、今いる現在のノードまでの経路を足して入れる<br><br>

もし、現在のノードが、目的のノードだった場合<br>
path変数の中に入っている、タイトルをself.titlesディクショナリ内に対応する<br>
ページ名を取得し、新たなリストを作成する<br>
そして、それを表示させる<br><br>

最後に、現在のノードからリンクしているすべてのノードに対してループを回す<br>
そして、もし次のノードが調べられていない場合、<br>
キューに、次のノードと現在のノードまでの経路を追加する<br>

