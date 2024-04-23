from flask import Flask, request, render_template, jsonify, redirect, url_for, session
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
        email = request.form["email"]
        pwd = request.form["password"]
        found_user = Users.query.filter_by(email = email).first()
        if found_user : 
            email = found_user.email
            password = found_user.pwd
            if password == pwd : 
                session["email"] = email
                return redirect(url_for('homepage'))
            else : 
                return jsonify({"message":"sai mat khau"}),200
        else : 
            return jsonify({"message":"sai email"}),200
    '''User = Users.query.all()
    json_User = list(map(lambda x : x.to_json(),User))
    data = jsonify({"user": json_User})
    email = request.json.get("email")
    pwd = request.json.get("pwd")
    if not email or not pwd : 
        return jsonify({"message": "information can't be null"}),400
    User = Users.query.all()
    json_User = list(map(lambda x : x.to_json(),User))
    data = jsonify({"user": json_User})'''
    return render_template("signin.html")
    
            

@app.route("/dangky", methods = ["POST","GET"])
def dangky():
    '''User = Users.query.all()
    json_User = list(map(lambda x : x.to_json(),User))
    data = jsonify({"user": json_User})'''
    if "useremail" in session: 
        return redirect('/')
    if request.method == "POST" : 
        name = request.form["username"]
        email = request.form["email"]
        pwd = request.form["password"]
        if not email or not pwd : 
            return jsonify({"message": "information can't be null"}),400
        newUser = Users(name = name, email = email, pwd = pwd)
        try : 
            db.session.add(newUser)
            db.session.commit()
        except Exception as e :
            return jsonify({"message": str(e)}),400
    return render_template("signup.html")

@app.route("/quenmatkhau", methods = ["GET","POST"])
def quenmatkhau(): 
    '''if request.method == "POST": 
        email = request.form["email"]
        found_user = Users.query.filter_by(email = email).first()
        if found_user : '''

    return render_template("forgetpass.html")

@app.route("/newspaper", methods = ["GET","POST"])
def newspaper(): 
    if "email" in session : 
        return render_template("newspaper.html")
    else : 
        redirect(url_for('dangnhap'))

@app.route("/club", methods = ["GET","POST"])
def club() : 
    if "email" in session : 
        return render_template("club.html")
    else : 
        redirect(url_for('dangnhap'))

@app.route("/activities", methods = ["POST","GET"])
def activities(): 
    if "email" in session : 
        return render_template('activities.html')
    else : 
        redirect(url_for('dangnhap'))

@app.route("/aboutus", methods = ["POST","GET"])
def aboutus(): 
    if "email" in session : 
        return render_template('aboutus.html')
    else : 
        redirect(url_for('dangnhap'))

if __name__ == "__main__": 
    with app.app_context(): 
        db.create_all()
    app.run(debug=True)