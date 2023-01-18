import json
import geopandas as gpd
import numpy as np

#shannon = gpd.read_file('shan_layer_new.geojson') #for testing the code

def graphs_calc (data, propertyForCalc):
    #data = GeoDataFrame which contains the property for calculation
    #column = property with which the graph should be calculated


    arr = data[propertyForCalc].to_numpy()



    if all(isinstance(e, (int, float)) for e in arr) == True:
        print ("data is numeric")
        dataType = "numerical"
        chartOptions = ["histogram"]
        charts =[]
        for chartType in chartOptions:
            if chartType == "histogram":
                chartValues, chartBinsLabels = np.histogram(arr)
            chartDict= {"chartType" : chartType, "chartValues" : chartValues.tolist(), "chartBinsLabels": chartBinsLabels.tolist() }
            charts.append(chartDict)




    if all(isinstance(e, (int, float)) for e in arr) == False:
        print ("data is categorical")
        dataType = "categorical"
        chartOptions = ["histogram", "pieChart"]
        charts = []
        for chartType in chartOptions:
            chartBinsLabels = np.unique(arr)
            chartBinsLabels = [x for x in chartBinsLabels if x != '']
            chartValues = []
            if chartType == "histogram":
                for type in chartBinsLabels:
                    count = np.count_nonzero(arr == type)
                    chartValues.append(count)

            if chartType == "pieChart":
                countall = len(arr)
                for type in chartBinsLabels:
                    countType = np.count_nonzero(arr == type)
                    countShare = (countType/countall)*100
                    chartValues.append(countShare)



            chartDict = {"chartType": chartType, "chartValues": chartValues,
                     "chartBinsLabels": chartBinsLabels}
            charts.append(chartDict)



    chart = {"dataType": dataType, "chartOptions": chartOptions, "chartData": charts}
    #print (chart)

    json_object = json.dumps(chart, indent=3)

    #print (json_object)


### call the function

#graphs_calc(shannon, 'main_cover') #example for calling the function