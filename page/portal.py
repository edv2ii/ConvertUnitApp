import streamlit as st
import pandas as pd
import numpy as np

# from calculator import Calculator

def table():
    column = ["Express","Stack", "Result"]
    df = pd.DataFrame(np.random.randn(10, len(column)), columns=("%s" % i for i in column))
    st.table(df)

class page:
    def __init__(self):
        pass

    def home():
        st.title("Calculator Application")
        st.write("This Project is that convert infix to postfix of datastruceture")
        st.header("Contact me")
        st.write(f'<ul><li><a href="https://www.facebook.com/12ize12">Facebook Me</a></li></ul>', unsafe_allow_html=True)
        st.write(f'<ul><li><a href="https://www.github.com/edv2ii">Github</a></li></ul>', unsafe_allow_html=True)
    def infix_convertor():
        st.header("Infix Convertsion")
        
    def infix_to_postfix():
        st.header("Infix To Postfix Conversion")
        st.text_input("Infix To")
        st.text_input("Postfix", value="", )
        table()

    def infix_to_prefix():
        st.header("Infix To Pretfix Conversion")
        st.text_input("Infix To")
        st.text_input("Prefix", value="", )
        table()

    def base_convertor():
        st.header("Base Conversion")
        base = [i for i in range(1,10)]
        st.selectbox(
            'Convert Base to 10',
            ("%s to 10" % i for i in base))

# cal = Calculator().calcBaseTo("1000", base=2, to=10)
# print(cal)
