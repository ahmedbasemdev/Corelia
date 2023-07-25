import  joblib
import pandas as pd
from utils import  *
param = {
 "Type":"TRANSFER",
    "Delivery_Status":"Shipping canceled",
    "Late_delivery_risk":0,
    "Category_Name":"Sporting Goods",
    "Customer_City":"Caguas",
    "Customer_Segment":"Corporate",
    "Department_Name":"Fitness",
    "Market":"USCA",
    "Order_Country":"Australia",
    "Order_Region":"Oceania",
    "Product_Price":327.750000,
    "Shipping_Mode":"Second Class"
}

data = pd.DataFrame([param])
for col, encoder in joblib.load("utils/encoders.pkl").items():
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

print(prediction)