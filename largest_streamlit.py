import streamlit as st
import pandas as pd

#pip install streamlit

def main():
    
    
    st.title('Find the Largest Number!')

    st.header('Please enter 3 numbers to find the largest among them!!')
    
    num1 = st.number_input("Enter first number")
    num2= st.number_input("Enter second number")
    num3= st.number_input("Enter third number")


    if st.button('Find Largest'):
        
        if (num1 >= num2) and (num1 >= num3):
            largest = num1
        elif (num2 >= num1) and (num2 >= num3):
            largest = num2
        else:
            largest = num3
        
        st.write("The largest number among the three is : ",largest)


streamlit.run largest_streamlit.py
