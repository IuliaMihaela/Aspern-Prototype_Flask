
'''
import json

# Opening JSON file
f = open('shan_layer_new.geojson')

# returns JSON object as a dictionary
data = json.loads(f.read())
'''


def graphs (graphType, dataType, inputData, propertyForCalc):
    #graphType = type of graph ('histogram' or 'pieChart')
    #dataType = define if the data is "numerical" or "categorical"
    #inputData = json object
    #propertyForCalc = colum needed for graph

    if graphType == 'histogram':
        if dataType == 'numerical':
            values_hist=[]
            for feature in inputData['features']:
                values_hist.append(float(feature['properties'][propertyForCalc]))

            return values_hist

        if dataType == 'categorical':
            strings_hist = []
            for feature in inputData['features']:
                strings_hist.append(feature['properties'][propertyForCalc])

            return strings_hist


    if graphType == 'pieChart':
        if dataType == 'categorical':
            strings_pie=[]
            for feature in inputData['features']:
                strings_pie.append(feature['properties'][propertyForCalc])
            lables = list(dict.fromkeys(strings_pie))
            values_pie=[]
            for type in lables:
                count= strings_pie.count(type)
                values_pie.append (count)
            #print (values_pie)
            #print (lables)

            return values_pie, lables



'''

### calling the function

result= graphs('pieChart', 'categorical', data, 'zoning')

'''