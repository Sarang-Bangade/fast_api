from typing import Annotated

from fastapi  import FastAPI, HTTPException, Path, Query
import json
from pydantic import BaseModel
app = FastAPI()

class Patient(BaseModel):

    id: Annotated [str,]
    name :str
    city:str
    age:int
    gender:str
    height:float
    weight:float
    


def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return  data      

@app.get("/")
def hello():
    return{'message':'Hello sarang here from fastApi'}

@app.get('/about')
def about():
    return{'message' : 'Functional api to manage pateient records'}

@app.get('/view')
def view():
    data = load_data()
    return data


@app.get('/patient/{patient_id}')
def view_patient(patient_id : str = Path(...,description = "Id of the patient in the DB")):
    #load all patients
    data = load_data()
    
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code = 404, detail = 'Patient not found')
 

 #use of query parameter : i.e additional data into the http server
@app.get('/sort')
def sort_patients(sort_by : str = Query(...,description ='Sort on the basis of height, weight or bmi'),
order: str = Query('asc', description = 'sort in asc or desc order')): 

    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException (status_code= 400, detail='Invalid order select between asc and desc')
   
    data = load_data()
    sort_order = True if order ==' desc' else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse = sort_order)
    return sorted_data
