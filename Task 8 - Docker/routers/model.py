from fastapi import APIRouter, Body

from utils import *
from schams import ModelInput
import pandas as pd
import joblib
from utils import cat_cols

model_router = APIRouter()


@model_router.get('/predict')
def get_prediction(params : ModelInput = Body()):

    prediction = prefrom_prediction(params)
    prediction = "Normal" if prediction[0]  == 1 else "Fraud"
    return {"output" : prediction}
