import streamlit as st
import time 
import pandas as pd
import joblib

# Function to preprocess input data
def preprocess_input(data):
    # Add your preprocessing steps here if needed
    return data

models = {
    'Hardik Pandya': joblib.load('HardikPandya.pkl'),
    'Ishan Kishan': joblib.load('IshanKishan.pkl'),
    'KL Rahul': joblib.load('KLRahul.pkl'),
    'Rohit Sharma': joblib.load('RohitSharma.pkl'),
    'Shreyas Iyer': joblib.load('ShreyasIyer.pkl'),
    'Shubman Gill': joblib.load('SubhmanGill.pkl'),
    'Surya Kumar Yadav': joblib.load('SuryaKumar.pkl'),
    'Virat Kohli': joblib.load('ViratKholi.pkl')
}

modelst = {
    'Hardik Pandya': joblib.load('HardikPandya_.pkl'),
    'Ishan Kishan': joblib.load('IshanKishan_.pkl'),
    'KL Rahul': joblib.load('KLRahul_.pkl'),
    'Rohit Sharma': joblib.load('RohitSharma_.pkl'),
    'Shreyas Iyer': joblib.load('ShreyasIyer_.pkl'),
    'Shubman Gill': joblib.load('SubhmanGill_.pkl'),
    'Surya Kumar Yadav': joblib.load('SuryaKumar_.pkl'),
    'Virat Kohli': joblib.load('ViratKholi_.pkl')
}


players = [
    'Hardik Pandya', 'Ishan Kishan', 'KL Rahul', 'Rohit Sharma',
    'Shreyas Iyer', 'Shubman Gill', 'Surya Kumar Yadav', 'Virat Kohli'
]

models_50s = {
    'Hardik Pandya': joblib.load('Hardik Pandya50s.pkl'),
    'Ishan Kishan': joblib.load('Ishan Kishan50s.pkl'),
    'KL Rahul': joblib.load('KL Rahul50s.pkl'),
    'Rohit Sharma': joblib.load('Rohit Sharma50s.pkl'),
    'Shreyas Iyer': joblib.load('Shreyas Iyer50s.pkl'),
    'Shubman Gill': joblib.load('Subhman Gill50s.pkl'),
    'Surya Kumar Yadav': joblib.load('Surya Kumar50s.pkl'),
    'Virat Kohli': joblib.load('Virat Kholi50s.pkl'),
}

models_100s = {
    'Hardik Pandya': joblib.load('Hardik Pandya100s.pkl'),
    'Ishan Kishan': joblib.load('Ishan Kishan100s.pkl'),
    'KL Rahul': joblib.load('KL Rahul100s.pkl'),
    'Rohit Sharma': joblib.load('Rohit Sharma100s.pkl'),
    'Shreyas Iyer': joblib.load('Shreyas Iyer100s.pkl'),
    'Shubman Gill': joblib.load('Subhman Gill100s.pkl'),
    'Surya Kumar Yadav': joblib.load('Surya Kumar100s.pkl'),
    'Virat Kohli': joblib.load('Virat Kholi100s.pkl'),
}

models_4s = {
    'Hardik Pandya': joblib.load('Hardik Pandya4s.pkl'),
    'Ishan Kishan': joblib.load('Ishan Kishan4s.pkl'),
    'KL Rahul': joblib.load('KL Rahul4s.pkl'),
    'Rohit Sharma': joblib.load('Rohit Sharma4s.pkl'),
    'Shreyas Iyer': joblib.load('Shreyas Iyer4s.pkl'),
    'Shubman Gill': joblib.load('Subhman Gill4s.pkl'),
    'Surya Kumar Yadav': joblib.load('Surya Kumar4s.pkl'),
    'Virat Kohli': joblib.load('Virat Kholi4s.pkl'),
}

models_6s = {
    'Hardik Pandya': joblib.load('Hardik Pandya6s.pkl'),
    'Ishan Kishan': joblib.load('Ishan Kishan6s.pkl'),
    'KL Rahul': joblib.load('KL Rahul6s.pkl'),
    'Rohit Sharma': joblib.load('Rohit Sharma6s.pkl'),
    'Shreyas Iyer': joblib.load('Shreyas Iyer6s.pkl'),
    'Shubman Gill': joblib.load('Subhman Gill6s.pkl'),
    'Surya Kumar Yadav': joblib.load('Surya Kumar6s.pkl'),
    'Virat Kohli': joblib.load('Virat Kholi6s.pkl'),
}


Ground_frequency = {'Bengaluru': 10, 'Eden Gardens': 12, 'Mumbai': 16, 'Lucknow': 9, 'Dharamsala': 6, 'Pune': 18, 'Ahmedabad': 17, 'Delhi': 9, 'Chennai': 16, 
     'Rajkot': 9, 'Colombo': 24, 'Pallekele': 8, 'Bridgetown': 9, 'Visakhapatnam': 10, 'Indore': 11, 'Raipur': 4, 'Hyderabad': 8, 'Thiruvananthapuram': 6,
     'Guwahati': 6, 'Mirpur': 8, 'Manchester': 16, 'London': 4, 'The Oval': 5, 'Cuttack': 4, 'Port of Spain': 15, 'Leeds': 4, 'Birmingham': 8, 
     'Southampton': 8, 'Mohali': 8, 'Ranchi': 5, 'Nagpur': 2, 'Wellington': 3, 'Hamilton': 8, 'Mount Maunganui': 7, 'Napier': 2, 'Melbourne': 2, 
     'Adelaide': 2, 'Sydney': 10, 'Chattogram': 4, 'Cape Town': 4, 'Paarl': 6, 'Canberra': 5, 'Auckland': 6, 'Christchurch': 3, 'San Fernando': 4, 'Harare': 7}
    

Against =  ['v Afghanistan', 'v Australia', 'v Bangladesh', 'v England',
        'v Netherlands', 'v New Zealand', 'v Pakistan', 'v South Africa',
        'v Sri Lanka', 'v West Indies']

Weather = ['Cloudy', 'Sunny', 'fog', 'light rain', 'mist']  
input_data = 5 # Dummy
def make_predictions(model, input_features):   # MAIN
    input_df = input_features
    input_df = preprocess_input(input_df)
    prediction = model.predict(input_df)
    return prediction[0]

# Manage the prediction of 4s, 6s, 100s, and 50s throught specific models 
def predict_50s(model_50s, input_features):
    input_df = input_features
    input_df = preprocess_input(input_df)
    prediction = model_50s.predict(input_df)
    return prediction[0]

def predict_100s(model_100s, input_features):
    input_df = input_features
    input_df = preprocess_input(input_df)
    prediction = model_100s.predict(input_df)
    return prediction[0]

def predict_4s(model_4s, input_features):
    input_df = input_features
    input_df = preprocess_input(input_df)
    prediction = model_4s.predict(input_df)
    return prediction[0]

def predict_6s(model_6s, input_features):
    input_df = input_features
    input_df = preprocess_input(input_df)
    prediction = model_6s.predict(input_df)
    return prediction[0]



#---------------------------------------------------------------------------------------------------------
def main():
    st.title('Player Perfromance Prediction 🏏')
    st.header('For Team India ')

    st.text('This system represents a sophisticated blend of machine learning models, \ncarefully designed to enhance prediction accuracy. By leveraging a variety\nof algorithms and optimizing them for diverse input parameters,\nit ensures reliable and precise outcomes for a wide range of scenarios.')
    player_name = st.selectbox('Select Player:', list(models.keys()))
    Normal_inputs = [
    'BF','Consistency Score',   # Mention that the Scores are from 0 to 8 in the APP 
    'Psych Readiness Score']                                   # Ground will be at 3rd Position

    select_against = st.selectbox('Vs:',Against)
    select_ground = st.selectbox('Select Ground:', list(Ground_frequency.keys()))
    select_Weather = st.selectbox('Wether Conditions',Weather)

    against_dict = {team: team == select_against for team in Against} # Boolean for Against 

    weather_dict = {condition: condition == select_Weather for condition in Weather} # Boolean for Weather



    st.sidebar.header('Other Parameters:')

    #

    input_data1 = {}
    for feature in Normal_inputs:
        if feature == 'BF':
            input_data1[feature] = st.sidebar.number_input(feature +' (Balls Faced)', value=0)
            st.sidebar.write('Scores are between 0 - 8')


        else:
            input_data1[feature] = st.sidebar.number_input(feature, value=0) 

    



    # Make prediction
    if st.button('Predict Runs'):
            with st.spinner(text='In progress'):
                time.sleep(3)
                st.success('Done')
            
                prediction_data = pd.DataFrame({
                'BF': [input_data1['BF']],
                **against_dict,
                'Ground_Frequency': [Ground_frequency[select_ground]],
                **weather_dict,
                'Consistency_Score': [input_data1['Consistency Score']],
                'Psych_Readiness_Score': [input_data1['Psych Readiness Score']]
            })
                


                # For 50s
                models_50ss = models_50s[player_name]
                s50 =predict_50s(models_50ss ,prediction_data)


                # for 100s
                models_100ss = models_100s[player_name]
                s100 =predict_100s(models_100ss ,prediction_data)
                
                s100 = round(s100)
                st.write("Number of 100s:" ,s100)

                # Specific Inputs for 6s and 4s
                prediction_data_specific = pd.DataFrame({
                'BF': [input_data1['BF']],
                '100s':[s100],
                '50s': [s50],
                **against_dict,
                'Ground_Frequency': [Ground_frequency[select_ground]],
                **weather_dict,
                'Consistency_Score': [input_data1['Consistency Score']],
                'Psych_Readiness_Score': [input_data1['Psych Readiness Score']]
            })
                # for 6s
                models_6ss = models_6s[player_name]
                s6 =predict_6s(models_6ss ,prediction_data_specific)
                st.write("Number of 6s:" ,s6)

                s100 = round(s100)
                s6 = round(s6)
                # for 4s
                models_4ss = models_4s[player_name]
                s4 =predict_4s(models_4ss ,prediction_data_specific)
                st.write("Number of 4s:" ,s4)
                s4 = round(s4)

                # Jugad



                # Final input
                prediction_data_final=pd.DataFrame({
                    'BF': [input_data1['BF']],
                    '4s': [s4],
                    '6s': [s6],
                    **against_dict,
                    'Ground_Frequency': [Ground_frequency[select_ground]],
                    **weather_dict,
                    '50s': [s50],
                    '100s': [s100],
                    '0s':[0]
                }) 

                




                model = modelst[player_name]
                prediction = make_predictions(model,prediction_data_final )
                prediction = round(prediction)

                st.write('Considering all the paramenters')
                st.write(player_name,'is can score:',prediction,'Runs')
                

    
if __name__ == '__main__':
    main()
