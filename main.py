from flask import Flask, request, render_template, jsonify, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from config import app,db
from models import Users

@app.route("/homepage", methods = ["GET","POST"])
def homepage(): 
    if 'email' in session : 
        return render_template("homepage.html")
    else : 
        return redirect(url_for('dangnhap'))

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/dangnhap", methods=["GET","POST"])
def dangnhap(): 
    if request.method == "POST" : 
        email = request.form["email"]   #Lay email tu form tren web 
        pwd = request.form["password"]  #Lay password tu form tren web 
        found_user = Users.query.filter_by(email = email).first() #Trich xuat tu database, tim nguoi dung, tra ve kq Bool 
        if found_user : 
            email = found_user.email
            password = found_user.pwd #lay mat khau va email tu database 
            if check_password_hash(password, pwd) : #So sanh mat khau ma hoa voi mat khau nguoi dung nhap 
                session["email"] = email
                return redirect(url_for('homepage')) 
            else : 
                return jsonify({"message":"sai mat khau"}),200
        else : 
            return jsonify({"message":"sai email"}),200
    return render_template("signin.html")
    
            

@app.route("/dangky", methods = ["POST","GET"])
def dangky():
    #User = Users.query.all() json_User = list(map(lambda x : x.to_json(),User)) data = jsonify({"user": json_User})
    if "email" in session: 
        return redirect('/homepage')
    if request.method == "POST" : 
        name = request.form["username"]
        email = request.form["email"]
        pwd = request.form["password"]
        pwd = generate_password_hash(pwd)
        if not email or not pwd : 
            return jsonify({"message": "information can't be null"}),400
        newUser = Users(name = name, email = email, pwd = pwd)
        try : 
            db.session.add(newUser)
            db.session.commit()
            return redirect(url_for('homepage'))
        except Exception as e :
            return jsonify({"message": str(e)}),400
    return render_template("signup.html")

@app.route("/quenmatkhau", methods = ["GET","POST"])
def quenmatkhau(): 
    return render_template("forgetpass.html")

@app.route("/newspaper", methods = ["GET","POST"])
def newspaper(): 
    if "email" in session : 
        return render_template("newspaper.html")
    else : 
        return redirect(url_for('dangnhap'))

@app.route("/club", methods = ["GET","POST"])
def club() : 
    if "email" in session : 
        return render_template("club.html")
    else : 
        return redirect(url_for('dangnhap'))

@app.route("/activities", methods = ["POST","GET"])
def activities(): 
    if "email" in session : 
        return render_template('activities.html')
    else : 
        return redirect(url_for('dangnhap'))

@app.route("/aboutus", methods = ["POST","GET"])
def aboutus(): 
    if "email" in session : 
        return render_template('aboutus.html')
    else : 
        return redirect(url_for('dangnhap'))

@app.route('/dangbai', methods = ["GET","POST"])
def dangbai(): 
    return render_template('C-subjects.html')

@app.route('/test', methods = ["GET","POST"])
def test(): 
    return render_template('test.html')


if __name__ == "__main__": 
    with app.app_context(): 
        db.create_all()
    app.run(debug=True)