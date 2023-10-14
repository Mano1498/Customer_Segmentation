import streamlit as st
import numpy as np
import joblib
import joblib

print(joblib.__version__)


std = joblib.load('C:/Users/ranja/OneDrive/Documents/Customer Segmentation/std_model.joblib')
lr = joblib.load('C:/Users/ranja/OneDrive/Documents/Customer Segmentation/lr_model.joblib')
ran_obj = joblib.load('C:/Users/ranja/OneDrive/Documents/Customer Segmentation/ran_obj_model.joblib')

def predict_rfm(recency, frequency, monetary):
    
    input_data = np.array([[recency, frequency, monetary]])
    input_data = std.transform(input_data)  

    
    prediction_lr = lr.predict(input_data)
    prediction_ran_obj = ran_obj.predict(input_data)

    return prediction_lr, prediction_ran_obj

def get_enhanced_rfm(lr_prediction, ran_obj_prediction):
   
    mapping = {
        (0, 'Gold'): 'Gold Standard',
        (1, 'Gold'): 'Gold Elite',
        (0, 'Silver'): 'Silver Standard',
        (1, 'Silver'): 'Silver Elite'
    }
    
    
    return mapping.get((lr_prediction, ran_obj_prediction), 'RFM Loyalty')



def main():
    st.title("eRFM Web App")
    st.write("enhanced-RFM For Robust  Clustering")

    # User input for RFM
    recency = st.number_input("Recency", value=0)
    frequency = st.number_input("Frequency", value=0)
    monetary = st.number_input("Monetary ", value=0)

    
    if st.button("Cluster my Customer"):
        lr_prediction, ran_obj_prediction = predict_rfm(recency, frequency, monetary)
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("K-means cluster", lr_prediction)
        with col2:
            st.write("RFM Loyalty", ran_obj_prediction)
        st.write("Enhanced RFM Level: ",get_enhanced_rfm(lr_prediction[0], ran_obj_prediction[0]))
        

if __name__ == '__main__':
    main()




