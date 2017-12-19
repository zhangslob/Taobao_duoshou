# 淘宝剁手吧

该项目使用 [Scrapy](https://github.com/scrapy/scrapy/) 抓取 taobao 商品信息，并存入 [MongoDB](https://github.com/mongodb/mongo) 数据库。

Web 端使用 [Flask](https://github.com/pallets/flask/) + [Bootstrap](https://github.com/twbs/bootstrap/) 构建聚合搜索商品信息的简单应用。

## Use



运行 Scrapy 爬取商品信息。
```bash
$ cd scrapy
$ scrapy crawl taobao
```

获取信息后，运行 Web Server 进行测试。
```bash
$ python server.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!

```

