import numpy as np
import pandas as pd
import streamlit as st
import pickle
# !pip install flask
import joblib


#data = pd.read_pickle('sorted_rules_new2.pkl')
data = joblib.load('sorted_rules_new10.pkl')

#data = pd.read_csv('yeni_08_sorted_rules.csv')

def arl_recommender(rules_df, product_id , rec_count=1):
    sorted_rules = rules_df.sort_values("lift", ascending=False)
    recommendation_list = []
    for i, product in sorted_rules["antecedents"].items():
        for j in list(product):
            if j == product_id:
                recommendation_list.append(list(sorted_rules.iloc[i]["consequents"]))
    recommendation_list = list({item for item_list in recommendation_list for item in item_list})
    return recommendation_list[:rec_count]




def main():
    st.title("Miuulgross Recommender")
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;"> Miuulgross Recommender </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    product = st.text_input("product", "Type Here")
    #rec_count = st.text_input("rec_count", "Type Here")
    #rec_count = rec_count.astype(int)

    # for col in last_test.columns:
    # print(col ,'=', "st.text_input(",'"',col,'"',",1)")
    # product = 'sausage'
    rec_count = 3

    safe_html = """  
    <div style="background-color:#80ff80; padding:10px >
    <h2 style="color:white;text-align:center;"> The customer does not have any payment difficulties</h2>
    </div>
    """
    warn_html = """  
        <div style="background-color:#F4D03F; padding:10px >
        <h2 style="color:white;text-align:center;"> The customer have payment difficulties</h2>
        </div>
      """
    if st.button("Enter client information : "):
        output = arl_recommender(data,product,rec_count)

        st.success('The result is {}'.format(output))

if __name__ == '__main__':
    main()
