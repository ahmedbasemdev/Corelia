from pydantic import BaseModel


class ModelInput(BaseModel):
    Type:str
    Delivery_Status:str
    Late_delivery_risk:int
    Category_Name:str
    Customer_City:str
    Customer_Segment:str
    Department_Name:str
    Market:str
    Order_Country:str
    Order_Region:str
    Product_Price:float
    Shipping_Mode:str

