from fastapi import FastAPI
from joblib import load
import numpy as np
from fastapi.responses import JSONResponse
from pydantic import BaseModel
#defining FastAPI
app = FastAPI()
#loading saved model
model = load('model_rf.joblib')

@app.get("/")
async def root():
   return {"message": "Hello World"}
#defining class for input variables
class Traffic(BaseModel):
    category:str
    type:str
    year:str
    month:str

#calling model and returning prediction
@app.post("/predict/")
def predict(features:Traffic):
    a=[]
    features=features.dict()
    data = list(features.values())
    if data[0]=="Alkoholunfälle":
        a.append(0)
    if data[0]=="Fluchtunfälle":
        a.append(1)
    if data[0]=="Verkehrsunfälle":
        a.append(2)
    if data[1]=="mit Personenschäden":
        a.append(0)
    if data[1]=="insgesamt":
        a.append(1)
    if data[1]=="Verletzte und Getötete":
        a.append(2)
    a.append((data[2]))
    a.append((data[3]))
    prediction = model.predict([a])
    print(prediction)
    return JSONResponse({
        'prediction': str(prediction),
        })


#main
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    # params = [{"category": "Alkoholunfälle", "type": "insgesamt", "year": "2021", "month": "01"}]
    # res= requests.post(f"http://127.0.0.1:8000/predict/",json=params)
    # print("Output: ",res)
