import pickle
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

def prediction(lst):
    filename ='model/model.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst])
    return pred_value

@app.route('/' ,methods=['GET','POST'])
def index():
   pred=0
   if request.method == 'POST':
       age=request.form['age']
       years_of_exprience=request.form['Years of Experience']
       jobtitle=request.form['Jobtitle']
       gender=request.form['Gender']
       education=request.form['Education Level']
       feature_list  = []
       feature_list.append(int(age))
       feature_list.append(float(years_of_exprience))


       gender_list=["Male","Female"]
       education_list=["Bachelor's","Master's","PhD"]
       job_list=["Data Analyst","Graphic Designer","HR Manager","Sales Associate","Senior Manager","Social Media Manager","Software Engineer","Web Developer"]




       def traverse(lst,value):
           for item in lst:
               if item == value:
                   feature_list.append(1)
               else:
                    feature_list.append(0)

       traverse(gender_list,gender)
       traverse(education_list,education)
       traverse(job_list,jobtitle)
       print(feature_list)


       pred = prediction(feature_list)
       pred =np.round(pred[0],2)

   return render_template('index.html', pred=pred)


if __name__ == '__main__':
    app.run()
