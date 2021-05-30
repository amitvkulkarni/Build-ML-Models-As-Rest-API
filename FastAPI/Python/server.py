from fastapi import FastAPI, Request
from typing import Dict
from pydantic import BaseModel
import uvicorn
import numpy as np
import pickle
import pandas as pd
import json

app = FastAPI()



@app.get("/")
async def root():
    return {"message": "Hello World"}

# Load the model
# model = pickle.load(open('../Models/KNN_model.pkl','rb'))
model = pickle.load(open('../Models/KNN_model.pkl','rb'))

@app.post('/predict')
def pred(body: dict):
    """[summary]

    Args:
        body (dict): [The pred methos takes Response as input which is in the Json format and returns the predicted value from the saved model.]

    Returns:
        [Json]: [The pred function returns the predicted value]
    """
    # Get the data from the POST request.
    data = body   
    varList = []
    for val in data.values():
	    varList.append(val)

    # Make prediction from the saved model
    prediction = model.predict([varList])
    
    # Extract the value
    output = prediction[0]

    #return the output in the json format
    return {'The prediction is ': output}
   

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    """[The API will run on the localhost on port 8000]    
    """
    uvicorn.run(app, host='127.0.0.1', port=8000)


    """[There are two ways to run the API
    1. python server.py (Typical way to execute the file, doesnot auto reload the changes.)
    2. uvicorn server:app --reload  (uvicorn auto reloads the localhost everytime there are any changes to code)
    ]
    """