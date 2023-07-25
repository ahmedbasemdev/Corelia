from fastapi import APIRouter,Body
from schams import  ModelInput
import  pandas as pd
import joblib
from utils import cat_cols
model_router = APIRouter()


@model_router.get('/predict')
def get_prediction(param :ModelInput=Body() ):

    data = pd.DataFrame([param])
    for col, encoder in joblib.load("../utils/encoders.pkl").items():
        data[col] = encoder.transform(data[col])

    hot_encoder = joblib.load('../utils/hot_encoder.joblib')
    encoded_data = pd.DataFrame(hot_encoder.transform(data[cat_cols]))
    encoded_data.columns = hot_encoder.get_feature_names(cat_cols)
    data = pd.concat([data, encoded_data], axis=1)

    data = data.drop(cat_cols, axis=1)

    scaler = joblib.load("../utils/scaler.joblib")
    data = scaler.transform(data)

    model = joblib.load("../utils/oneSVM.joblib")

    prediction = model.predict(data)


    return {"Prediction is " : prediction }

