import pickle
import streamlit as st
import pandas as pd

from PIL import Image
width = st.slider('What is the width in pixels?', 400, 700, 700)

image = Image.open('phones.jpg')

st.image(image, caption='Smart Phones',width=width)


def recommendTV(product,n):
    index = phones[phones['caracteristique'] == product].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    L=[]
    for i in distances[1:n+1]:
        L.append([phones.iloc[i[0]].caracteristique, phones.iloc[i[0]].price, phones.iloc[i[0]].rating,i[1]])
    st.write(pd.DataFrame(L, columns=["Caracteristique", "Price", "Rating", "CosineSimilarity"]))
    #     L.append([phones.iloc[i[0]].caracteristique, phones.iloc[i[0]].price, phones.iloc[i[0]].rating, phones.iloc[i[0]].marque, i[1]])
    # st.write(pd.DataFrame(L, columns=["Caracteristique", "Price", "Rating", "Marque", "CosineSimilarity"]))

phones = pickle.load(open('phone_list.pkl','rb'))
similarity = pickle.load(open('similarity_phone.pkl','rb'))

phone_list = phones['caracteristique'].values

st.header('Phone Recommender System')

selected_makeup = st.selectbox(
    "Select a Phone",
    phone_list
)

int_val = st.number_input('Number of Phones for recommendation', min_value=1, step=1)

if st.button('Show Recommendation'):
    recommendTV(selected_makeup,int_val)
