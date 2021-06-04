from flask import Flask, request, render_template

import numpy as np
import pickle

# Create Flask object to run
app = Flask(__name__,template_folder= 'templates' )
def conlist(numbertochange,max):
  
  k = []
  for i in range(1,max+1,1):
    if i == numbertochange:
      k.append(float(1))
    if i != numbertochange:
      k.append(float(0))
  del k[0]
  return k
@app.route('/')
def home():
    return render_template('HOTELBOOKINDEX.html')

@app.route('/predict',methods=['POST'])
def predict():

  try:
    knnIrisModel = pickle.load(open('hotelbook.pkl', 'rb'))
    int_features = [float(x) for x in request.form.values()]
    HOTEL = int(request.form.get('HOTEL TYPE'))
    print(HOTEL)
    COUNTRY = int(request.form.get('COUNTRY'))
    print(COUNTRY)
    MEAL = int(request.form.get('MEAL'))
    print(MEAL)
    DEPOSITE = int(request.form.get('DEPOSIT TYPE'))
    print(DEPOSITE)
    CUSTOMER = int(request.form.get('CUSTOMER TYPE'))
    print(CUSTOMER)
    MONTH = int(request.form.get('MONTH'))
    print(MONTH)
    ASSIGNED = int(request.form.get('ASSIGNED ROOM'))
    print(ASSIGNED)
    ADULT = int(request.form.get('ADULT'))
    print(ADULT)
    CHILDREN = int(request.form.get('CHILDREN'))
    print(CHILDREN)
    ADR = float(request.form.get('ADR'))
    print(ADR)


    FEATURES = []
    FEATURES.extend(conlist(HOTEL,2))
    FEATURES.extend(conlist(COUNTRY,11))
    FEATURES.extend(conlist(MEAL,5))
    FEATURES.extend(conlist(DEPOSITE,3))
    FEATURES.extend(conlist(CUSTOMER,4))
    FEATURES.extend(conlist(MONTH,12))
    FEATURES.append(ASSIGNED)
    FEATURES.append(ADULT)
    FEATURES.append(CHILDREN)
    FEATURES.append(ADR)
    print(FEATURES)


    prediction = knnIrisModel.predict([FEATURES])
    output =prediction[0]
    if output ==0:
      output = "CONFIRMED BOOKING"
    if output ==1:
      output = "NOT CONFIRMED BOOKING"
    return render_template('HOTELBOOKINDEX.html', prediction_text= output)
  except:
    return render_template('HOTELBOOKINDEX.html', prediction_text= 'invalid input')
    
    
if __name__ == "__main__":
	app.run()
