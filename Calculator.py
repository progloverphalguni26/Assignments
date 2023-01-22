import streamlit as st
 
st.title("The Great Calculator")
 
# creates a horizontal line
st.write("---")

# input 1
n1 = st.number_input(label="Enter first number")
 
# input 2
n2 = st.number_input(label="Enter second number")

st.write("Operation")
 
o = st.radio("Select an operation to perform:",
                    ("Add", "Subtract", "Multiply", "Division", "Modulus", "Integer Division", "Power"))

def calc():
    if o=="Add": 
        res=n1+n2
    elif o=="Subtract":
        res=n1-n2
    elif o=="Multiply":
        res=n1*n2
    elif o=="Division":
        if n2==0:
            res="cannot divide by 0"
        else:
            res=n1/n2
    elif o=="Modulus": 
        res=n1%n2
    elif o=="Integer Division":
        res=n1//n2
    elif o=="Power":
        res=n1**n2
    else: 
        res="invalid operator"
    st.success(f"Answer = {res}")

if st.button("Calculate result"):
    calc()