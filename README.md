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

#### 完整内容请来我的博客 [scrapy学习实例（四）采集淘宝数据并展示](https://zhangslob.github.io/2017/12/19/scrapy%E5%AD%A6%E4%B9%A0%E5%AE%9E%E4%BE%8B%EF%BC%88%E5%9B%9B%EF%BC%89%E9%87%87%E9%9B%86%E6%B7%98%E5%AE%9D%E6%95%B0%E6%8D%AE%E5%B9%B6%E5%B1%95%E7%A4%BA/)
