from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('Titanic_survival_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    # Fuel_Type_Diesel=0
    # if request.method == 'POST':
        m=np.zeros(10)
        m[0] = int(request.form['Pclass'])
        m[1]=float(request.form['Age'])
        m[2]=int(request.form['SibSp'])
        # Kms_Driven2=np.log(Kms_Driven)
        m[3]=int(request.form['Parch'])
        m[4]=float(request.form['Fare'])
        Sex=request.form['Sex']
       
        if(Sex=='Female'):
                m[5]=1
                
        if(Sex=='Male'): 
                m[6]=1 
       
        Embarked=str(request.form['Embarked'])
        if(Embarked=='C'):
            m[7]=1
        elif(Embarked=='Q'):
            m[8]=1	
        else:
            m[9]=1
        # Transmission_Mannual=request.form['Transmission_Mannual']
        # if(Transmission_Mannual=='Mannual'):
        #     Transmission_Mannual=1
        # else:
        #     Transmission_Mannual=0
        #prediction=model.predict([m])[0]
        #output=model.predict([m])[0]
        output=model.predict([m])[0]
        Survival=output
    
        if(Survival==0):
            return render_template('index.html',prediction_text="PREDICTION =Person did not Survived")
        else:
        # if(Survival==0):
            return render_template('index.html',prediction_text="PREDICTION=Person Survived")
        
        # return render_template('index.html',prediction_text="Survival of person {}".format(Survival))

if __name__=="__main__":
    app.run(debug=True)

