import streamlit as st
from PIL import Image
st.title("calculator app")

def add(a,b):
    c = a + b
    return c

def sub(a,b):
    c = a - b
    return c

def mul(a,b):
    c = a * b
    return c
col1, col2 = st.columns(2)

with col1:

    x = st.number_input("Input Your first Number")
    x = st.number_input("Input Your second Number")

with col2:
    if st.button("Add"):
     st.write(add(x,y))

    if st.button("Subtract"):
     st.write(sub(x,y))

    
    if st.button("Multiply"):
     st.write(mul(x,y))  



   
    