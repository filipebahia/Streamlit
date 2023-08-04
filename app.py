import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

st.title("My first project")

st.title("Making a Button")

result = st.button("Click Here")

st.write(result)

if result:
    st.write(":smile:")

selecao = st.selectbox('Selecione', range(1,5),1)

marcacao = st.checkbox('Marcação')

icon_size = 22

st_button('linkedin', 'https://www.linkedin.com/in/filipebahia/', 'Filipe de M. Peixoto', icon_size)
