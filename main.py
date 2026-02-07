from fastapi import FastAPI,Path
import json
app = FastAPI()

def load_data():
    with open('patients.json','r' ) as f:
        data = json.load(f)
    return data    

@app.get("/")
def hello():
    return{'message': 'Patients Management System API'}

@app.get("/about")
def sarang():
    return{'message' : 'API to manage the patient records'}

@app.get('/view')
def view():
    data = load_data()
    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id : str = Path(..., description ="Id of the patient in Db, example - 'P001' ")):

    #load all the patients
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    return {'error': "Patient data not found"}