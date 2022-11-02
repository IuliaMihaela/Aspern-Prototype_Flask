from flask import render_template, url_for, redirect, request
from webapp import app
import json
from requests import put, get, post, delete

@app.route("/", methods=['GET'])
def home():
    return render_template('prop_canvas.html')
    # return render_template('dynamic_prop.html')
    # return render_template('updated_plots.html')


@app.route("/data/prototype_layerWGS84.geojson", methods=['GET'])
def data1():
    with open(r'webapp\data\prototype_layerWGS84.geojson', encoding='utf-8') as f:
        return f.read()

@app.route("/data/final/aspern_blocks_attr.geojson", methods=['GET'])
def data2():
    with open(r'webapp\data\final\aspern_blocks_attr.geojson', encoding='utf-8') as f:
        return f.read()

@app.route("/data/final/aspern_realUseBlocks.geojson", methods=['GET'])
def data3():
    with open(r'webapp\data\final\aspern_realUseBlocks.geojson', encoding='utf-8') as f:
        return f.read()

@app.route("/data/final/aspern_bkmBlocks.geojson", methods=['GET'])
def data4():
    with open(r'webapp\data\final\aspern_bkmBlocks.geojson', encoding='utf-8') as f:
        return f.read()

@app.route("/data/final/aspern_landuse.geojson", methods=['GET'])
def data5():
    with open(r'webapp\data\final\aspern_landuse.geojson', encoding='utf-8') as f:
        return f.read()

@app.route("/data/final/aspern_roads.geojson", methods=['GET'])
def data6():
    with open(r'webapp\data\final\aspern_roads.geojson', encoding='utf-8') as f:
        return f.read()

@app.route("/data/final/aspern_publiclines.geojson", methods=['GET'])
def data7():
    with open(r'webapp\data\final\aspern_publiclines.geojson', encoding='utf-8') as f:
        return f.read()

@app.route("/data/final/aspern_trees_blocks.geojson", methods=['GET'])
def data8():
    with open(r'webapp\data\final\aspern_trees_blocks.geojson', encoding='utf-8') as f:
        return f.read()

@app.route("/data/final/aspern_publicstops.geojson", methods=['GET'])
def data9():
    with open(r'webapp\data\final\aspern_publicstops.geojson', encoding='utf-8') as f:
        return f.read()

@app.route("/data/final/shops.geojson", methods=['GET'])
def data10():
    with open(r'webapp\data\final\shops.geojson', encoding='utf-8') as f:
        return f.read()


# @app.route('/flask', methods=['GET'])
# def get_calculated_data():
#     # r= post('http://localhost:8000/py',
#     #      json={'username': 'felicity', "timestamp": "15-04-2022 19:56", "assets": "1,22,3,4,5,11"})
#     # print(r.content.decode())
#     # return "Flask server..."
#     return {'username': 'felicity', "timestamp": "15-04-2022 19:56", "assets": "1,22,3,4,5,11"}

@app.route('/flask/<data>', methods=['POST'])
def post_calculated_data(data):
    #steps:
    # get data from map,
    # call function for index calculation with the data,
    # (store the changes and the indices in a file ?),
    # return the result from the function
    data = json.loads(data)
    print(data)
    print('request', type((request.data).decode()))
    # return data
    return request.data





