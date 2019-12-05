#step -1 # Importing flask module in the project is mandatory 
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
#Step -2 Flask constructor takes the name of  
# current module (__name__) as argument.app = Flask(__name__)

app = Flask(__name__)

#Step -3 Load Trained  Model
model = pickle.load(open('Cluster.pkl', 'rb'))


# Step -4 The route() function of the Flask class is a decorator,  
# which tells the application which URL should call  
# the associated function


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    c  = [np.array(int_features)]
    
    o = model.predict(c)
    if o == 4:
        Category = 'Sensible Clients'
    elif o == 3:
        Category = 'Careless Client'
    elif o == 2:
        Category = 'Target Client'
    elif o == 1:
        Category = 'Standard Client'
    else:
        Category = 'Careful Client'

    res=Category

   

    return render_template('index.html', prediction_text='The client belongs to {} Category'.format(Category))

# main driver function
 # run() method of Flask class runs the application  
    # on the local development server.
if __name__ == "__main__":
    app.run(debug=True)

