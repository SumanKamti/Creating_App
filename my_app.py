import streamlit as st

st.write("Hello World: Getting Adam, Hello Brother!!")
st.title("Display Title use st.title()")

st.write("To write text use st.write()")

st.header("I am header to write header use st.header()")
st.subheader("I am subheader to write subheader use st.subheader()")

st.text("Hey I am simple text to write simple text use st.text()")

st.markdown("[Streamlit](http://streamlit.io/)")
st.markdown("[Streamlit Cheatsheet](https://cheat-sheet.streamlit.app/)")

st.success("Success!")
st.info("Information")
st.warning("This is a Warning")
st.error("This is an error")

from PIL import Image
img = Image.open("smj.jpg")
st.image(img, width=100, caption="Satyamev Jayate")

video_file = open("vid.mp4","rb")
video_bytes = video_file.read()
st.video(video_bytes)

st.video("https://youtu.be/khL1Gkp6vnM?si=68dUbg58atgFyaoK")

audio = open("song.mp3","rb")
audio_bytes = audio.read()
st.audio(audio_bytes, format="audio/mp3")

st.button("Play")

st.header("Button Widgets")
if st.button("Play1"):
    st.text("Hello World")
    
if st.button("Play2"):
    st.text("Enjoy Music")
    st.video("https://youtu.be/hNBDtBfv6wE?si=0SKzQ7WMU9PAN_Cd")
    
if st.checkbox("Checkbox"):
    st.text("CheckBox Selected")
    
if st.checkbox("Checkbox2"):
    st.text("Checkbox selected")
    st.video("https://youtu.be/hNBDtBfv6wE?si=0SKzQ7WMU9PAN_Cd")
    
radio_but = st.sidebar.radio("Your Selection", ["Male","Female"])
if radio_but == "Male":
    st.info("You Are Male")
else:
    st.info("You Are Female")
    
city = st.sidebar.selectbox("Your City", ["Daman","Diu","Valsad"])
if city == "Daman":
    st.info("I Love Daman")
elif city == "Diu":
    st.info("I Love Diu")
else:
    st.info("I Love Valsad")  
    
occupation = st.sidebar.multiselect("Your Occupation", ["Programmer", "Data Scientist",                                         "ITConsultant", "DSA"])
    
age = st.sidebar.number_input("Input a number")    
    
message = st.text_area("About NIELIT","WRITE SOMETHINGS----")
message = st.text_area("Address","WRITE SOMETHINGS----")    
    
select_val= st.sidebar.slider("Select a value", 1,10)
select_val= st.sidebar.slider("Select a value",10.0,20.0 ,0.5)
if st.sidebar.button("Balloons"):
    st.balloons()
    
#----------Pandas DataFrame------------#    
import streamlit as st
import pandas as pd

auto_data = pd.read_csv("auto.csv")
st.dataframe(auto_data.head())

st.table(auto_data.head(10))

st.area_chart(auto_data[["mpg","cylinders"]])
st.area_chart(auto_data[["mpg","cylinders"]].head(20))

st.bar_chart(auto_data[["mpg","cylinders"]])
st.bar_chart(auto_data[["mpg","cylinders"]].head(20))

st.line_chart(auto_data[["mpg","cylinders"]])
st.line_chart(auto_data[["mpg","cylinders"]].head(20))

import datetime
import time

today = st.date_input("Today is",datetime.datetime.now())
hour = st.time_input("The time is",datetime.time(12,00))

st.code("Import pandas as pd")
st.code("print(Welcome to NIELIT Daman)")

import pandas as pd 
import numpy as np

st.title("Area")
df = pd.DataFrame(np.random.randn(40,4),columns=["C1","C2","C3","C4"])             
st.bar_chart(df)

st.title("Line Chart")
df = pd.DataFrame(np.random.randn(40,4),columns=["C1","C2","C3","C4"])
st.line_chart(df)

st.title("Area Chart")
df = pd.DataFrame(np.random.randn(40,4),columns=["C1","C2","C3","C4"])
st.area_chart(df)













































