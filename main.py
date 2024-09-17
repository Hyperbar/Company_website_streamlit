import streamlit as st
import pandas
import os

# Set the page configuration to use wide layout
st.set_page_config(layout="wide")

st.title("The Best Company")

header_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit,sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
st.write(header_text)

st.markdown("<h2>Our team</h2>", unsafe_allow_html=True)

col_1, empty_col_1, col_2, empty_col_2, col_3 = st.columns([1, 1, 1, 1, 1])

df = pandas.read_csv("data.csv", sep=",")

with col_1:
    # Créer la colonne full_name une seule fois, en dehors de la boucle
    df['full_name'] = df['first name'] + ' ' + df['last name']

    # Itérer seulement sur les 4 premières lignes
    for index, row in df.iloc[:4].iterrows():
        st.subheader(row['full_name'])
        st.write(row["role"])

        image_path = os.path.join("img", row["image"])
        if os.path.exists(image_path):
            st.image(image_path)
        else:
            st.write(f"Image not found: {image_path}")

with col_2:
    # Créer la colonne full_name une seule fois, en dehors de la boucle
    df['full_name'] = df['first name'] + ' ' + df['last name']

    # Itérer seulement sur les 4 premières lignes
    for index, row in df.iloc[4:8].iterrows():
        st.subheader(row['full_name'])
        st.write(row["role"])

        image_path = os.path.join("img", row["image"])
        if os.path.exists(image_path):
            st.image(image_path)
        else:
            st.write(f"Image not found: {image_path}")

with col_3:
    # Créer la colonne full_name une seule fois, en dehors de la boucle
    df['full_name'] = df['first name'] + ' ' + df['last name']

    # Itérer seulement sur les 4 premières lignes
    for index, row in df.iloc[8:].iterrows():
        st.subheader(row['full_name'])
        st.write(row["role"])

        image_path = os.path.join("img", row["image"])
        if os.path.exists(image_path):
            st.image(image_path)
        else:
            st.write(f"Image not found: {image_path}")