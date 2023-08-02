cat_cols = ['Type', 'Delivery_Status', 'Customer_Segment', 'Market', 'Shipping_Mode']

import  pandas as pd

import joblib


def prefrom_prediction(params):
    params = params.dict()
    data = pd.DataFrame(params, index=[0])

    try:
        for col, encoder in joblib.load("utils/encoders.joblib").items():
            data[col] = encoder.transform(data[col])
    except:
        return "fucck"
    hot_encoder = joblib.load('utils/hot_encoder.joblib')
    encoded_data = pd.DataFrame(hot_encoder.transform(data[cat_cols]))
    encoded_data.columns = hot_encoder.get_feature_names(cat_cols)
    data = pd.concat([data, encoded_data], axis=1)

    data = data.drop(cat_cols, axis=1)

    scaler = joblib.load("utils/scaler.joblib")
    data = scaler.transform(data)

    model = joblib.load("utils/oneSVM.joblib")

    prediction = model.predict(data)

    return prediction


def predcit_file(data):


    for col, encoder in joblib.load("utils/encoders.joblib").items():
        data[col] = encoder.transform(data[col])

    hot_encoder = joblib.load('utils/hot_encoder.joblib')
    encoded_data = pd.DataFrame(hot_encoder.transform(data[cat_cols]))
    encoded_data.columns = hot_encoder.get_feature_names(cat_cols)
    data = pd.concat([data, encoded_data], axis=1)

    data = data.drop(cat_cols, axis=1)

    scaler = joblib.load("utils/scaler.joblib")
    data = scaler.transform(data)

    model = joblib.load("utils/oneSVM.joblib")

    prediction = model.predict(data)

    return prediction