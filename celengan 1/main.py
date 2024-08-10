from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)

Data = ["I","G","S"]
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/biodata')
def biodata():
    if 'namas' in request.args.keys() and 'umurs' in request.args.keys():
        nama = request.args['namas']
        umur = request.args['umurs']
        kelas = request.args.get('kelass')
        return render_template("biodata.html", nama = nama, umur=umur,kelas=kelas)
    else:
        return render_template("home.html")
    
@app.route('/blog')
def blog():
    DayCoding = ["kamis","jumat","sabtu"]
    # for day in DayCoding:
    #     print(day)

    day = datetime.now().day
    month = datetime.now().month

    return render_template("blog.html", DayCoding = DayCoding, Datas = Data, day = day, month = month)



if __name__ == "__main__":
    app.run(debug=True)