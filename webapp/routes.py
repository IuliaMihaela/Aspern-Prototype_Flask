from flask import render_template, url_for, redirect, request
from webapp import app
import json
import geopandas
from requests import put, get, post, delete
from script import index_calculation, reproject

@app.route("/", methods=['GET'])
def home():
    return render_template('show_index.html')
    # return render_template('prop_canvas.html')
    # return render_template('dynamic_prop.html')
    # return render_template('updated_plots.html')


@app.route("/dropdown/", methods=['GET'])
def dropdown():
    return render_template('dropdown.html')

@app.route("/prop/", methods=['GET'])
def prop():
    return render_template('show_changed_prop.html')

@app.route("/prop2/", methods=['GET'])
def prop2():
    return render_template('improved_prop.html')

@app.route("/design/", methods=['GET'])
def design():
    return render_template('design.html')

@app.route("/design2/", methods=['GET'])
def design2():
    return render_template('design2.html')

@app.route("/prop3/", methods=['GET'])
def prop3():
    return render_template('improved_prop_engl.html')

@app.route("/design3/", methods=['GET'])
def design3():
    return render_template('design3.html')

@app.route("/design4/", methods=['GET'])
def design4():
    return render_template('design4.html')

@app.route("/design5/", methods=['GET'])
def design5():
    return render_template('design5.html')

########### data ###########
@app.route("/data/prototype_layerWGS84.geojson", methods=['GET'])
def data1():
    with open(r'webapp\data\prototype_layerWGS84.geojson', encoding='utf-8') as f:
        return f.read()

@app.route("/data/final/aspern_blocks_attr.geojson", methods=['GET'])
def data2():
    with open(r'webapp\data\final\aspern_blocks_attr.geojson', encoding='utf-8') as f:
        return f.read()

@app.route("/data/final/aspern_blocks_final.geojson", methods=['GET'])
def data21():
    with open(r'webapp\data\final\aspern_blocks_final.geojson', encoding='utf-8') as f:
        return f.read()

@app.route("/data/final/aspern_realUseBlocks.geojson", methods=['GET'])
def data3():
    with open(r'webapp\data\final\aspern_realUseBlocks.geojson', encoding='utf-8') as f:
        return f.read()

@app.route("/data/final/aspern_landcover_final.geojson", methods=['GET'])
def data31():
    with open(r'webapp\data\final\aspern_landcover_final.geojson', encoding='utf-8') as f:
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




# old data ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/data/changes/final/aspern_blocks_attr.geojson", methods=['GET'])
def data12():
    with open(r'webapp\data\changes\final\aspern_blocks_attr.geojson', encoding='utf-8') as f:
        return f.read()

@app.route("/data/changes/final/aspern_realUseBlocks.geojson", methods=['GET'])
def data13():
    with open(r'webapp\data\changes\final\aspern_realUseBlocks.geojson', encoding='utf-8') as f:
        return f.read()

@app.route("/data/changes/final/aspern_bkmBlocks.geojson", methods=['GET'])
def data14():
    with open(r'webapp\data\changes\final\aspern_bkmBlocks.geojson', encoding='utf-8') as f:
        return f.read()

@app.route("/data/changes/final/aspern_landuse.geojson", methods=['GET'])
def data15():
    with open(r'webapp\data\changes\final\aspern_landuse.geojson', encoding='utf-8') as f:
        return f.read()

@app.route("/data/changes/final/aspern_roads.geojson", methods=['GET'])
def data16():
    with open(r'webapp\data\changes\final\aspern_roads.geojson', encoding='utf-8') as f:
        return f.read()

@app.route("/data/changes/final/aspern_publiclines.geojson", methods=['GET'])
def data17():
    with open(r'webapp\data\changes\final\aspern_publiclines.geojson', encoding='utf-8') as f:
        return f.read()

@app.route("/data/changes/final/aspern_trees_blocks.geojson", methods=['GET'])
def data18():
    with open(r'webapp\data\changes\final\aspern_trees_blocks.geojson', encoding='utf-8') as f:
        return f.read()

@app.route("/data/changes/final/aspern_publicstops.geojson", methods=['GET'])
def data19():
    with open(r'webapp\data\changes\final\aspern_publicstops.geojson', encoding='utf-8') as f:
        return f.read()

@app.route("/data/changes/final/shops.geojson", methods=['GET'])
def data110():
    with open(r'webapp\data\changes\final\shops.geojson', encoding='utf-8') as f:
        return f.read()


# @app.route('/flask/<data>', methods=['POST'])
# def post_calculated_data(data):
#     #steps:
#     # get data from map,
#     # call function for index calculation with the data,
#     # (store the changes and the indices in a file ?),
#     # return the result from the function
#     data = json.loads(data)
#     # print(data)
#     print('flask route')
#     print('request decode type', type((request.data).decode()))
#     dict = json.loads((request.data).decode())
#     df = geopandas.GeoDataFrame.from_features(dict, crs="EPSG:4326")
#     print(type(df), df)
#
#     result = index_calculation(df)
#     print('index result: ', result)
#     return result.to_json()



@app.route('/flask/', methods=['POST'])
def post_calculated_data():
    #steps:
    # get data from map,
    # call function for index calculation with the data,
    # (store the changes and the indices in a file ?),
    # return the result from the function

    print('flask route')
    print('request decode type', type((request.data).decode()))
    dict = json.loads((request.data).decode())

    df = geopandas.GeoDataFrame.from_features(dict, crs="EPSG:4326")
    print(type(df), df)

    df = reproject(df)

    result = index_calculation(df)
    print('index result: ', result)
    return result.to_json()


