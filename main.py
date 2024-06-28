from flask import Flask, request, render_template, jsonify, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from config import app,db
from models import Users, Image, Writer



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
    if "email" in session: 
        return redirect('/homepage')
    if request.method == "POST" : 
        email = request.form["email"]   #Lay email tu form tren web 
        pwd = request.form["password"]  #Lay password tu form tren webf
        found_user = Users.query.filter_by(email = email).first() #Trich xuat tu database, tim nguoi dung, tra ve kq Bool 
        if found_user : 
            email = found_user.email
            password = found_user.pwd #lay mat khau va email tu database 
            if check_password_hash(password, pwd) : #So sanh mat khau ma hoa voi mat khau nguoi dung nhap 
                session["email"] = email
                session["id"] = found_user.id
                return redirect(url_for('homepage')) 
            else : 
                return jsonify({"message":"sai mat khau"}),200
        else : 
            return jsonify({"message":"sai email"}),200
    return render_template("signin.html")
    
            

@app.route("/dangky", methods = ["POST","GET"])
def dangky():
    #User = Users.query.all() json_User = list(map(lambda x : x.to_json(),User)) data = jsonify({"user": json_User})
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
    return render_template('upload.html')

@app.route('/dangbai2', methods = ["GET","POST"])
def dangbai2(): 
    return render_template('C-time.html')

@app.route('/dangbai3', methods = ["GET","POST"])
def dangbai3(): 
    if request.method == "POST": 
        text = request.form["data"]
        newPost = Writer(belong_to=session["id"], article=text)
        try : 
            db.session.add(newPost)
            db.session.commit()
            return redirect(url_for('homepage'))
        except Exception as e :
            return jsonify({"message": str(e)}),400
    return render_template('C-upload.html')

@app.route('/rules', methods = ["GET","POST"])
def rule(): 
    return render_template("rules.html")

@app.route("/AI_huongnghiep")
def AI_huongnghiep(): 
    return render_template("huongnghiep.html")

@app.route("/mbti.html")
def mbti(): 
    return render_template("mbti.html")

@app.route("/mbti1")
def mbti1(): 
    return render_template("MBTI1.html")

@app.route('/1.html', methods=["GET","POST"]) 
def test1(): 
    session["dapan1"] = 0 
    if request.method == "POST": 
        if request.form["a"] == "a": 
            session["dapan1"] = session["dapan1"] + 1 
        return redirect("/2.html")
    return render_template('1.html')
@app.route('/2.html', methods=["POST"]) 
def test2(): 
    if request.method == "POST": 
        if request.form["a"] == "a": 
            session["dapan1"] = session["dapan1"] + 1 
        return redirect("/3.html")
    return render_template('2.html')
@app.route('/3.html', methods=["POST","GET"]) 
def test3(): 
    if request.method == "POST": 
        if request.form["a"] == "a": 
            session["dapan1"] = session["dapan1"] + 1 
        return redirect("/4.html")
    return render_template('3.html')
@app.route('/4.html') 
def test4(): 
    if request.method == "POST": 
        if request.form["a"] == "a": 
            session["dapan1"] = session["dapan1"] + 1 
        return redirect("/5.html")
    return render_template('4.html')
@app.route('/5.html') 
def test5(): 
    if request.method == "POST": 
        if request.form["a"] == "a": 
            session["dapan1"] = session["dapan1"] + 1 
        return redirect("/6.html")
    return render_template('5.html')
@app.route('/6.html') 
def test6(): 
    if request.method == "POST": 
        if request.form["a"] == "a": 
            session["dapan1"] = session["dapan1"] + 1 
        return redirect("/7.html")
    return render_template('6.html')
@app.route('/7.html') 
def test7(): 
    if request.method == "POST": 
        if request.form["a"] == "a": 
            session["dapan1"] = session["dapan1"] + 1 
        return redirect("/8.html")
    return render_template('7.html')
@app.route('/8.html') 
def test8(): 
    if request.method == "POST": 
        if request.form["a"] == "a": 
            session["dapan1"] = session["dapan1"] + 1 
        return redirect("/9.html")
    return render_template('8.html')
@app.route('/9.html') 
def test9():
    if request.method == "POST": 
        if request.form["a"] == "a": 
            session["dapan1"] = session["dapan1"] + 1 
        return redirect("/10.html") 
    return render_template('9.html')
@app.route('/10.html') 
def test10(): 
    if request.method == "POST": 
        if request.form["a"] == "a": 
            session["dapan2"] = session["dapan2"] + 1 
        return redirect("/11.html")
    return render_template('10.html')
@app.route('/11.html') 
def test11(): 
    session["dapan2"] = 0 
    if request.method == "POST": 
        if request.form["a"] == "a": 
            session["dapan2"] = session["dapan2"] + 1 
        return redirect("/12.html")
    return render_template('11.html')
@app.route('/12.html') 
def test12(): 
    if request.method == "POST": 
        if request.form["a"] == "a": 
            session["dapan2"] = session["dapan2"] + 1 
        return redirect("/13.html")
    return render_template('12.html')
@app.route('/13.html') 
def test13(): 
    if request.method == "POST": 
        if request.form["a"] == "a": 
            session["dapan2"] = session["dapan2"] + 1 
        return redirect("/14.html")
    return render_template('13.html')
@app.route('/14.html') 
def test14(): 
    if request.method == "POST": 
        if request.form["a"] == "a": 
            session["dapan2"] = session["dapan2"] + 1 
        return redirect("/15.html")
    return render_template('14.html')
@app.route('/15.html') 
def test15(): 
    if request.method == "POST": 
        if request.form["a"] == "a": 
            session["dapan2"] = session["dapan2"] + 1 
        return redirect("/16.html")
    return render_template('15.html')
@app.route('/16.html') 
def test16(): 
    if request.method == "POST": 
        if request.form["a"] == "a": 
            session["dapan2"] = session["dapan2"] + 1 
        return redirect("/17.html")
    return render_template('16.html')
@app.route('/17.html') 
def test17(): 
    if request.method == "POST": 
        if request.form["a"] == "a": 
            session["dapan2"] = session["dapan2"] + 1 
        return redirect("/18.html")
    return render_template('17.html')
@app.route('/18.html') 
def test18(): 
    if request.method == "POST": 
        if request.form["a"] == "a": 
            session["dapan2"] = session["dapan2"] + 1 
        return redirect("/19.html")
    return render_template('18.html')
@app.route('/19.html') 
def test19(): 
    if request.method == "POST": 
        if request.form["a"] == "a": 
            session["dapan3"] = session["dapan3"] + 1 
        return redirect("/20.html")
    return render_template('19.html')
@app.route('/20.html') 
def test20(): 
    return render_template('20.html')
@app.route('/21.html') 
def test21(): 
    return render_template('21.html')
@app.route('/22.html') 
def test22(): 
    return render_template('22.html')
@app.route('/23.html') 
def test23(): 
    return render_template('23.html')
@app.route('/24.html') 
def test24(): 
    return render_template('24.html')
@app.route('/25.html') 
def test25(): 
    return render_template('25.html')
@app.route('/26.html') 
def test26(): 
    return render_template('26.html')
@app.route('/27.html') 
def test27(): 
    return render_template('27.html')
@app.route('/28.html') 
def test28(): 
    return render_template('28.html')
@app.route('/29.html') 
def test29(): 
    return render_template('29.html')
@app.route('/30.html') 
def test30(): 
    return render_template('30.html')
@app.route('/31.html') 
def test31(): 
    return render_template('31.html')
@app.route('/32.html') 
def test32(): 
    return render_template('32.html')
@app.route('/33.html') 
def test33(): 
    return render_template('33.html')
@app.route('/34.html') 
def test34(): 
    return render_template('34.html')
@app.route('/35.html') 
def test35(): 
    return render_template('35.html')
@app.route('/36.html') 
def test36(): 
    return render_template('36.html')
@app.route('/37.html') 
def test37(): 
    return render_template('37.html')
@app.route('/38.html') 
def test38(): 
    return render_template('38.html')
@app.route('/39.html') 
def test39(): 
    return render_template('39.html')
@app.route('/40.html') 
def test40(): 
    return render_template('40.html')
@app.route('/41.html') 
def test41(): 
    return render_template('41.html')
@app.route('/42.html') 
def test42(): 
    return render_template('42.html')
@app.route('/43.html') 
def test43(): 
    return render_template('43.html')
@app.route('/44.html') 
def test44(): 
    return render_template('44.html')
@app.route('/45.html') 
def test45(): 
    return render_template('45.html')
@app.route('/46.html') 
def test46(): 
    return render_template('46.html')
@app.route('/47.html') 
def test47(): 
    return render_template('47.html')
@app.route('/48.html') 
def test48(): 
    return render_template('48.html')
@app.route('/49.html') 
def test49(): 
    return render_template('49.html')
@app.route('/50.html') 
def test50(): 
    return render_template('50.html')
@app.route('/51.html') 
def test51(): 
    return render_template('51.html')
@app.route('/52.html') 
def test52(): 
 return render_template('52.html')
@app.route('/53.html') 
def test53(): 
 return render_template('53.html')
@app.route('/54.html') 
def test54(): 
 return render_template('54.html')
@app.route('/55.html') 
def test55(): 
 return render_template('55.html')
@app.route('/56.html') 
def test56(): 
 return render_template('56.html')
@app.route('/57.html') 
def test57(): 
 return render_template('57.html')
@app.route('/58.html') 
def test58(): 
 return render_template('58.html')
@app.route('/59.html') 
def test59(): 
 return render_template('59.html')
@app.route('/60.html') 
def test60(): 
 return render_template('60.html')
@app.route('/61.html') 
def test61(): 
 return render_template('61.html')
@app.route('/62.html') 
def test62(): 
 return render_template('62.html')
@app.route('/63.html') 
def test63(): 
 return render_template('63.html')
@app.route('/64.html') 
def test64(): 
 return render_template('64.html')
@app.route('/65.html') 
def test65(): 
 return render_template('65.html')
@app.route('/66.html') 
def test66(): 
 return render_template('66.html')
@app.route('/67.html') 
def test67(): 
 return render_template('67.html')
@app.route('/68.html') 
def test68(): 
 return render_template('68.html')
@app.route('/69.html') 
def test69(): 
 return render_template('69.html')
@app.route('/70.html') 
def test70(): 
 return render_template('70.html')
if __name__ == "__main__": 
    with app.app_context(): 
        db.create_all()
    app.run(debug=True)