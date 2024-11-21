from flask import Flask, render_template,request,redirect,session
import datetime

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.model_selection import train_test_split

from DBConnection import Db

app = Flask(__name__)
app.secret_key="abc"


@app.route('/',methods=['get','post'])
def login():
    if request.method=="POST":
        u=request.form['textfield']
        p=request.form['textfield2']
        db=Db()
        res=db.selectOne("select * from login where username='"+u+"' and password='"+p+"'")
        if res is not None:
            if res['usertype']=="admin":
                session['lg']='lin'
                return redirect('/admin_home')
            elif res['usertype']=="clinic":
                session['lg'] = 'lin'
                session['lid']=res['login_id']
                return redirect('/clinichome')
            else:
                return '''<script>alert("INVALID USER");window.location="/"</script>'''
        else:
            return '''<script>alert("USER NOT FOUND");window.location="/"</script>'''
    return render_template("login.html")
@app.route('/logout')
def logout():
    session.clear()
    session['lg']=""
    return redirect('/')
@app.route('/view_clinic')
def view_clinic():
    if session['lg']=="lin":

        db=Db()
        a=db.select("select * from clinic")
        return render_template("Admin/view_clinic.html",data=a)
    else:
        return redirect('/')

@app.route('/view_feedback')
def view_feedback():
    if session['lg'] == "lin":
        db=Db()
        b=db.select("select * from feedback,clinic where feedback.clinic_id=clinic.login_id")
        return render_template("Admin/view_feedback.html",data=b)
    else:
        return redirect('/')

@app.route('/clinic',methods=['get','post'])
def clinic():
    if request.method=="POST":
        name=request.form['textfield']
        phone=request.form['textfield2']
        email=request.form['textfield3']
        place=request.form['textfield4']
        post=request.form['textfield5']
        pin=request.form['textfield6']
        license=request.form['textfield7']
        password=request.form['textfield9']
        cp=request.form['cp']
        db=Db()
        if password==cp:
            res=db.insert("insert into login VALUES ('','"+email+"','"+password+"','clinic')")
            db.insert("insert into clinic VALUES ('"+str(res)+"','"+name+"','"+phone+"','"+email+"','"+place+"','"+post+"','"+pin+"','"+license+"')")
            return '''<script>alert("successfully");window.location="/"</script>'''
        else:
            return '''<script>alert("password mismatch!!");window.location="/clinic"</script>'''

    else:
        return render_template("Clinic/clinic_register.html")

@app.route('/Feedback',methods=['get','post'])
def Feedback():
    if session['lg'] == "lin":
        db=Db()
        if request.method=='POST':
            feedback =request.form['textarea']
            db.insert("insert into feedback values('','"+str(session['lid'])+"','"+feedback+"',curdate())")
            return "ok"
        else:
            return render_template("Clinic/Feedback.html")
    else:
            return redirect('/')

@app.route('/Image',methods=['get','post'])
def Image():
    if session['lg'] == "lin":
         if request.method == "POST":
            image=request.files['fileField']
            date=datetime.datetime.now().strftime("%y%m%d-%H%M%S")
            image.save(r"C:\Users\HP\PycharmProjects\leukemia project\static\pic\\"+date+'.jpg')
            ss="/static/pic/"+date+'.jpg'

            image_path = r"C:\Users\HP\PycharmProjects\leukemia project\static\pic\\"+date+".jpg"
            from PIL import Image

            img = Image.open(image_path).convert('LA')
            img.save('D:\\greyscale.png')

            import cv2
            import numpy as np

            im_gray = cv2.imread('D:\\greyscale.png', cv2.IMREAD_GRAYSCALE)
            (thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            cv2.imwrite('C:\\Users\\HP\\PycharmProjects\\leukemia project\\static\\binary.png', im_bw)

            img = cv2.imread('C:\\Users\\HP\\PycharmProjects\\leukemia project\\static\\binary.png', 0)
            kernel = np.ones((5, 5), np.uint8)

            opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
            cv2.imwrite('D:\\opening.png', opening)
            close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

            cv2.imwrite('D:\\close.png', close)

            # finding erosion
            import cv2
            import numpy as np

            des = cv2.bitwise_not(close)
            contour, hier = cv2.findContours(des, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

            for cnt in contour:
                cv2.drawContours(des, [cnt], 0, 255, -1)

            gray = cv2.bitwise_not(des)
            cv2.imwrite('D:\\fill.png', gray)

            # import mahotas as mt
            #
            # textures = mt.features.haralick(gray)
            # ht_mean = textures.mean(axis=0)
            #
            # angular_second_moment=ht_mean[0]
            # constrast=ht_mean[1]
            # correlation=ht_mean[2]
            # entropy=ht_mean[8]
            properties = ['ASM', 'contrast', 'correlation', 'energy']
            headerlist = properties
            headerlist.append('Label')

            import numpy as np
            from skimage import io, color, img_as_ubyte
            from skimage.feature import greycomatrix, greycoprops

            rgbImg = io.imread('D:\\fill.png')
            grayImg = img_as_ubyte(rgbImg)

            distances = [1, 2, 3]
            angles = [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4]

            glcm = greycomatrix(grayImg,
                                distances=distances,
                                angles=angles,
                                symmetric=True,
                                normed=True)

            feats = np.hstack([greycoprops(glcm, 'ASM').ravel() for prop in properties])
            feats1 = np.hstack([greycoprops(glcm, 'contrast').ravel() for prop in properties])
            feats2 = np.hstack([greycoprops(glcm, 'correlation').ravel() for prop in properties])
            feats3 = np.hstack([greycoprops(glcm, 'energy').ravel() for prop in properties])

            k = np.mean(feats)
            l = np.mean(feats1)
            m = np.mean(feats2)
            n = np.mean(feats3)

            ar = []
            ar.append(k)
            ar.append(l)
            ar.append(m)
            ar.append(n)
            print("AAA  ", ar)
            arr=[]
            tesst_val=np.array([ar])
            import pandas as pd
            a=pd.read_csv("C:\\Users\\HP\\PycharmProjects\\leukemia project\\static\\features.csv")
            attributes=a.values[:,:4]
            labels=a.values[:,4]
            rf=RandomForestClassifier(n_estimators=100)
            rf.fit(attributes,labels)
            pred=rf.predict(tesst_val)
            lst=pred.tolist()
            x_train, x_test, y_train, y_test=train_test_split(attributes, labels, test_size=0.2)
            clf=RandomForestClassifier(n_estimators=100, random_state=0)
            clf.fit(x_train, y_train)
            y_pred=clf.predict(x_test)
            acc=accuracy_score(y_test, y_pred)
            print(lst[0])
            stat=""
            if lst[0]==1.0:
                stat="Diseased"
            if lst[0]==0.0:
                stat="Non Diseased"
            if lst[0] == 2.0:
                stat="Invalid Input"
            print(stat)
            db=Db()
            db.insert("insert into image values('','"+str(session['lid'])+"','"+ss+"',curdate(), '"+stat+"')")
            return  render_template("Clinic/Image.html", data=stat, acc=round(acc*100, 2))
         else:
            return render_template("Clinic/Image.html")
    else:
            return redirect('/')

@app.route('/view_profile',methods=['get','post'])
def view_profile():
    if session['lg'] == "lin":
        if request.method=="POST":
            name=request.form['textfield']
            phone=request.form['textfield2']
            email=request.form['textfield3']
            place=request.form['textfield4']
            post=request.form['textfield5']
            pin=request.form['textfield6']
            licenses=request.form['textfield7']
            db=Db()
            db.update("update clinic set clinic_name='"+name+"',phone='"+phone+"',email='"+email+"',place='"+place+"',post='"+post+"',pincode='"+pin+"',license='"+licenses+"' where clinic.login_id='"+str(session['lid'])+"'")
            return "ok"
        else:
            db=Db()
            pr=db.selectOne("select * from clinic where clinic.login_id='"+str(session['lid'])+"'")
            return render_template("Clinic/view profile.html",data=pr)
    else:
            return redirect('/')

@app.route('/view_image', methods=['get', 'post'])
def view_image():
    if session['lg'] == "lin":
        db=Db()
        im=db.select("select * from image where image.clinic_id='"+str(session['lid'])+"'")
        return render_template("Clinic/view image.html",data=im)

    else:
        return redirect('/')

@app.route('/admin_home')
def admin_home():
    if session['lg'] == "lin":
        return render_template("Admin/Admin Home.html")
    else:
            return redirect('/')

@app.route('/clinichome')
def clinichome():
    if session['lg'] == "lin":
        db=Db()
        return render_template("Clinic/clinic_index.html")
    else:
            return redirect('/')
if __name__ == '__main__':
    app.run(port=4000)
