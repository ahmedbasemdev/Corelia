from fastapi import APIRouter, Body, UploadFile, File

import utils
from schams import ModelInput
import pandas as pd
import joblib
from utils import cat_cols
import pandas as pd

model_router = APIRouter()


@model_router.post("/predict_csv")
async def predict_csvfile(file: UploadFile = File(...)):
    data = pd.read_csv(file.file)[:10]
    data = data.rename(columns=lambda x: x.replace(' ', '_'))
    data = data.drop(['Order_Item_Quantity', 'Unnamed:_0'], axis=1)
    data = data.drop('FraudOrder', axis=1)
    outputs = utils.predcit_file(data)
    return {"outputs of First 10 Rows respectively": str(outputs)}



@model_router.get('/predict')
def get_prediction(params: ModelInput = Body()):
    prediction = utils.prefrom_prediction(params)
    prediction = "Normal" if prediction[0] == 1 else "Fraud"
    return {"output": prediction}
