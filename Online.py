import json

from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    # index from
    return render_template("index.html")

@app.route("/contact",methods=['POST','GET'])
def contact():
    # contact form
    return render_template("contact-us.html")

@app.route("/about",methods=['POST','GET'])
def about():
    return render_template("about.html")
@app.route("/mainchart",methods=['POST','GET'])
def mainChart():
    # district wise total crop production
    import DWTCProduction as dwtc1
    return_list=dwtc1.main()
    data = json.dumps(return_list[0])
    labels = json.dumps(return_list[1])
    return render_template('mainchart.html',data1=data,lable=labels)

@app.route("/dcpa",methods=['POST','GET'])
# area and district wise total crop production
def dcpa():
    import districtCropProductionArea as pre
    list=pre.plot()
    # pre.plot()
    # print(list[3])
    # eel.data(list)
    # return render_template("demo.html",name=list)

    data = json.dumps(list[2])
    labels = json.dumps(list[3])
    area = json.dumps(list[1])
    return render_template("ADWCPChart.html", lable=labels,data1=data,data2=area)

@app.route("/sycp",methods=['POST','GET'])
def sycp():
    # specific year crop production shows all crop name
    if request.method=="POST":
        year=request.form.get("year")
        dis=request.form.get("dis")
        district=dis
        import specificYearCropsProduction as spe
        return_list=spe.main(dis,year)
        print(return_list)
        data = json.dumps(return_list[0])
        labels = json.dumps(return_list[1])
        year = return_list[2]
        cropmax = return_list[3]
        maxpro =return_list[4]
        cropmin = return_list[5]
        minpro =return_list[6]

        # bar_no = json.dumps(return_list[2])
        # print("runnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")
        # print(data)
        # print(labels)
        return render_template("SYCPChart.html",data1=data,lable=labels,year=year,cropmax=cropmax,maxpro=maxpro,cropmin=cropmin,minpro=minpro)
        # return render_template("SYCPSelection.html")
    else:
        return render_template("SYCPSelection.html")


@app.route("/cpiy",methods=['POST','GET'])
def cpiy():
    # particular district wise total crop production in each year
    import CPInYear as CPIY
    if request.method=="POST":
        dis=request.form.get("dis")
        return_list=CPIY.main(dis)
        print(return_list)
        data = json.dumps(return_list[0])
        labels = json.dumps(return_list[1])

        districtname=dis
        maxpro=return_list[3]
        year=return_list[4]
        # bar_no = json.dumps(return_list[2])
        print(return_list[1])

        return render_template("CPIYChart.html",data1=data,lable=labels,districtname=districtname,maxpro=maxpro,year=year)
        # return "hello"
    else:
        return render_template("CPIYSelection.html")

# @app.route("/dwtcpr",methods=['POST','GET'])
# def dwtcpr():
#     import DWTCProduction as dwtc
#     return_list=dwtc.main()
#     data = json.dumps(return_list[0])
#     labels = json.dumps(return_list[1])
#     return render_template("DWTCChart.html",data1=data,lable=labels)

@app.route("/popciy",methods=['POST','GET'])
def popciy():
    # Production Of Perticular Crop in Years
    if request.method=="POST":
        dis=request.form.get("dis")
        cropname=request.form.get("croptype")
        import ProductionOfPerticularCropinYears as POPCIY
        return_list=POPCIY.main(dis,cropname)
        print(return_list)
        if return_list[0]=="NONE":
            return render_template("POPCIYSelective.html")
        else:
            data = json.dumps(return_list[0])
            labels = json.dumps(return_list[1])

            maxpro=return_list[2]
            maxyear=return_list[3]
            minpro=return_list[4]
            minyear=return_list[5]
            
            # # bar_no = json.dumps(return_list[2])
            # print(return_list[1])

            return render_template("POPCIYChart.html", data1=data, lable=labels,maxpro=maxpro,maxyear=maxyear,minpro=minpro,minyear=minyear,cropname=cropname)

        # return "hello"
    else:
        return render_template("POPCIYSelective.html")

@app.route('/chart', methods=['GET', 'POST'])
def chart():
    labels1 = ["January","February","March","April","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
    data = json.dumps(values)
    labels = json.dumps(labels1)
    return render_template('chart2.html',data1=data,lable=labels)
    # return "hello"

@app.route('/rec',methods=['GET', 'POST'])
def rec():
    if request.method=="POST":
        dis=request.form.get("dis")
        global dist
        dist = dis
        season=request.form.get("season")
        import rec2 as rec
        return_list=""
        return_list=rec.yearProductionCal(dis,season)
        data = json.dumps(return_list)
        return render_template("recReceiveCrop.html",data1=data ,dis2=dis)
        # return render_template("recReceiveDS.html")
    else:
        return render_template("recReceiveDS.html")

@app.route('/reccrop',methods=['GET', 'POST'])
def reccrop():
    if request.method=="POST":
        crop1=""
        Crop2=""
        crop1=request.form.get("crop1")
        crop2=request.form.get("crop2")
        print(crop1)
        print(crop2)
        import rec2 as rec
        district = dist

        # rec.graph(crop1,crop2)
        return_list=rec.graph(crop1,crop2)
        data_1=""
        data_2=""
        data_1 = json.dumps(return_list[0])
        labels = json.dumps(return_list[2])
        data_2 = json.dumps(return_list[1])
        choice1 = json.dumps(return_list[3])
        choice2 = json.dumps(return_list[4])
        # print(data_1)
        # print(data_2)
        # maxPro = json.dumps(return_list[5])
        # cropMax = json.dumps(return_list[6])
        # minPro = json.dumps(return_list[7])
        # cropMin = json.dumps(return_list[8])

        maxPro = return_list[5]
        cropMax =return_list[6]
        minPro =return_list[7]
        cropMin =return_list[8]

        # print(return_list)
        return render_template("/recChart.html",data1=data_1,lable=labels,data2=data_2,ch1=choice1,ch2=choice2,maxPro1=maxPro,cropMax1=cropMax,minPro1=minPro,cropMin1=cropMin , crop1=crop1,crop2=crop2,dis=district)
    else:
        return render_template("recReceiveDS.html")

if __name__ == "__main__":
    app.run(debug=True)