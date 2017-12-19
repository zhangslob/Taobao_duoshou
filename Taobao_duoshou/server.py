# -*- coding: UTF-8 -*-
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
from bson import json_util
from bson.objectid import ObjectId
import json
import pymongo

conn = pymongo.MongoClient('localhost', 27017)
db = conn['taobao']
goods_coll = db['search']
cate_coll = db['categories']
app = Flask(__name__)

def toJson(data):
    return json.dumps(
               data,
               default=json_util.default,
               ensure_ascii=False
           )

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        total = goods_coll.count()
        return render_template('index.html', total=total)
    #if request.form['key']:
    #    key = request.form['key']
    #    return redirect(url_for('get_goods', key=key, page=1))


@app.route('/search', methods=['GET'])
@app.route('/search/<item>', methods=['GET'])
def get_goods(item=None):
    if request.method == 'GET':
        page = request.args.get('page', 1, type=int)
        limit = request.args.get('limit', 30, type=int)
        p = (page - 1) * limit
        offset = request.args.get('offset', p, type=int)
        catid = request.args.get('catid', None, type=str)
        jsons = request.args.get('json', 'off')
        keyword = request.args.get('key', '')
        if not keyword:
            keyword = item

        if catid:
            cursor = goods_coll.find({'categories.catid': catid})
        else:
            cursor = goods_coll.find({'title': {'$regex': keyword} })
        #total = cursor.count()
        #flash('已查询到 %d 个结果.'%total)
        results = cursor.skip(offset).limit(limit)
        resultList = []
        for result in results:
            resultList.append(result)

        if jsons == 'off':
            return render_template('search.html', entries=resultList)
        else:
            return toJson(resultList)

if __name__ == '__main__':
    #app.run(host='0.0.0.0')
    app.run(debug=True)
