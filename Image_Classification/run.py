import os
from sklearn.externals import joblib
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import img_to_array  
from flask import Flask, redirect, render_template, url_for, request

app = Flask(__name__) 


@app.route('/')
def home():
    return render_template('home.html')


def path():
    f        = request.files['file']                      # static/upload.
    dir      = os.path.dirname(os.path.abspath(__file__))
    filename = f.filename
    filedir  = '/static/' + filename  
    f.save( dir + '/static/' + filename )
   
    mymodel = joblib.load( r'.\Test.pkl' )
    return  mymodel, filedir    


@app.route('/upload', methods=['GET','POST'] )
def upload():
    if request.method == 'GET':
        return render_template('upload.html') 
    else:
        mymodel, filedir = path()
        now_dir          = os.getcwd()                                 
        # print( mymodel, filedir, filename )                                        # 1. Read Multi-layer Perceptron model etc...                         
        imgData          = image.load_img( now_dir + filedir,  target_size=(98,98) ) # 2. Load saved images 
        test_img         = img_to_array( imgData )/255
        # print( test_img.shape )                                                    # 3. Transform image to ndarray
        if mymodel.predict( test_img.reshape(1,-1) )[0]   == 0.0:
            pred_result = '모자'
        elif mymodel.predict( test_img.reshape(1,-1) )[0] == 1.0:
            pred_result = '바지'
        else:
            pred_result = '신발'
        # print( result )                                                            # 4. Result : 3 class (0, 1, 2) 
        pred_proba = ( mymodel.predict_proba( test_img.reshape(1,-1) ).max().round(4) )*100
        return render_template( 'uploadend.html', pred_result=pred_result, filedir=filedir, pred_proba=pred_proba )


if __name__ == '__main__':  
    app.run(debug=True)