from flask import *
import pymysql

db = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "pratikdalvi"
    )

cursor = db.cursor()


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
    
@app.route("/about")
def about():
    name = "Places that you will visit in Pune"
    mylist = ["Shaniwar Wada", "Dagadusheth Halwai Temple", "Sinhgadh Fort", "Aga Khan Palace", "Shinde Chatri", "Saras Bag", "Lal Mahal", "National War Museum", "Rajive Gandhi Zoological Park"]
    return render_template("about.html",username=name,mylist=mylist)

@app.route("/user/<name>")
def user(name):
    return "Hello {}".format(name)

@app.route("/allusers")
def allusers():
    cursor.execute("select * from tour")
    data = cursor.fetchall()
    return render_template("allusers.html",userdata=data)






@app.route("/create",methods=["POST"])
def create():
    uname = request.form.get('uname')
    contact = request.form.get('contact')
    pwd = request.form.get('pwd')
    tr = request.form.get('tr')
    dat = request.form.get('dat')
    pri = request.form.get('pri')
    
    insq ="insert into tour(Username,Contact,Password,Tour,Date,Payment) values ('{}','{}','{}','{}','{}','{}')".format(uname,contact,pwd,tr,dat,pri)
    try:
        cursor.execute(insq)
        db.commit()
        return redirect(url_for("allusers"))
    except:
        db.rollback()
        return "Error in query"


@app.route("/delete")
def delete():
    id = request.args.get('id')
    
    delq = "delete from tour where id={}".format(id)
    try:
        cursor.execute(delq)
        db.commit()
        return redirect(url_for("allusers"))
    except:
        db.rollback()
        return "Error in query"

@app.route("/edit")
def edit():
    id = request.args.get('id')
    
    selq ="select * from tour where id={}".format(id)
    cursor.execute(selq)
    data = cursor.fetchone()
    return render_template("edit.html",row = data)

@app.route("/update",methods=["POST"])
def update():
    uname = request.form.get('uname')
    contact = request.form.get('contact')
    pwd = request.form.get('pwd')
    tr = request.form.get('tr')
    dat = request.form.get('dat')
    pri = request.form.get('pri')
    uid = request.form.get('uid')
    
    updq ="update tour set Username='{}', Contact='{}', Password='{}', Tour='{}', Date='{}', Payment='{}' where id='{}' ".format(uname,contact,pwd,tr,dat,pri,uid)
    try:
        cursor.execute(updq)
        db.commit()
        return redirect(url_for("allusers"))
    except:
        db.rollback()
        return "Error in query"
   
@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/getdata",methods=["POST"])
def getdata():
    id = request.form.get('id')
    
    selq ="select * from tour where id={}".format(id)
    cursor.execute(selq)
    data = cursor.fetchone()
    return render_template("search.html",row = data)

    
if __name__ == '__main__':
    app.run(debug=True)
    



