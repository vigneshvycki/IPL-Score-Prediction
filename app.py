from flask import Flask,render_template,request
import pickle
import numpy as np

model=pickle.load(open('forest_model.pkl','rb'))

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_score', methods=['POST'])
def predict_score():
  prediction_array = []
  if request.method=='POST':
      batting_team=request.form['batting-team']
      if batting_team == 'Chennai Super Kings':
            prediction_array = prediction_array + [1,0,0,0,0,0,0,0]
      elif batting_team == 'Delhi Daredevils':
            prediction_array = prediction_array + [0,1,0,0,0,0,0,0]
      elif batting_team == 'Kings XI Punjab':
            prediction_array = prediction_array + [0,0,1,0,0,0,0,0]
      elif batting_team == 'Kolkata Knight Riders':
            prediction_array = prediction_array + [0,0,0,1,0,0,0,0]
      elif batting_team == 'Mumbai Indians':
            prediction_array = prediction_array + [0,0,0,0,1,0,0,0]
      elif batting_team == 'Rajasthan Royals':
            prediction_array = prediction_array + [0,0,0,0,0,1,0,0]
      elif batting_team == 'Royal Challengers Bangalore':
            prediction_array = prediction_array + [0,0,0,0,0,0,1,0]
      elif batting_team == 'Sunrisers Hyderabad':
            prediction_array = prediction_array + [0,0,0,0,0,0,0,1]
      
      bowling_team=request.form['bowling-team']  
      if bowling_team == 'Chennai Super Kings':
            prediction_array = prediction_array + [1,0,0,0,0,0,0,0]
      elif bowling_team == 'Delhi Daredevils':
            prediction_array = prediction_array + [0,1,0,0,0,0,0,0]
      elif bowling_team == 'Kings XI Punjab':
            prediction_array = prediction_array + [0,0,1,0,0,0,0,0]
      elif bowling_team == 'Kolkata Knight Riders':
            prediction_array = prediction_array + [0,0,0,1,0,0,0,0]
      elif bowling_team == 'Mumbai Indians':
            prediction_array = prediction_array + [0,0,0,0,1,0,0,0]
      elif bowling_team == 'Rajasthan Royals':
            prediction_array = prediction_array + [0,0,0,0,0,1,0,0]
      elif bowling_team == 'Royal Challengers Bangalore':
            prediction_array = prediction_array + [0,0,0,0,0,0,1,0]
      elif bowling_team == 'Sunrisers Hyderabad':
            prediction_array = prediction_array + [0,0,0,0,0,0,0,1]
            
      overs=float(request.form['overs'])
      runs=int(request.form['runs'])
      wickets=int(request.form['wickets'])
      runs_in_prev_5=float(request.form['runs_in_prev_5'])
      wickets_in_prev_5=float(request.form['wickets_in_prev_5'])
      prediction_array = prediction_array + [runs, wickets, overs, runs_in_prev_5, wickets_in_prev_5]
      prediction_array = np.array([prediction_array])
      my_prediction = int(model.predict(prediction_array)[0])
      
      return render_template('result.html',my_prediction=my_prediction)
        
if __name__=='__main__':
    app.run(debug=True)