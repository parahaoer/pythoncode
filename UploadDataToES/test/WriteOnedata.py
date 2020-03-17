from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

action ={
              "id": "1111122222",
              "serial":"版本",
              #以下tags.content是错误的写法
              #"tags.content" :"标签2",
              #"tags.dominant_color_name": "域名的颜色黄色",
              #正确的写法如下：
              "tags":{"content":"标签3","dominant_color_name": "域名的颜色黄色"},
              #按照字典的格式写入，如果用上面的那种写法，会直接写成一个tags.content字段。
              #而不是在tags中content添加数据，这点需要注意
              "tags.skill":"分类信息",
              "hasTag":"123",
              "status":"11"
                }
es.index(index="index_test",body = action, id = 2)



