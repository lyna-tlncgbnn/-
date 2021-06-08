import datetime
from io import StringIO
from os import write
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit.elements import checkbox
from streamlit.proto.Checkbox_pb2 import Checkbox
#Draw a title and some text to the app
st.set_page_config(
    page_title="lyna tlncgbnn",
    page_icon=(":shark:"),
    layout='wide',
)
'''
# This is tht document title
This is some_markdown_.
'''
df = pd.DataFrame([1,2,3],columns=["col1"])
df # <-- Draw the dataframe

x = 10
"x=",x
st.text("hello world")
st.markdown("**Hello world**")
st.write("**hello world**")
st.title("Hello")
st.header("lyna")
st.subheader("tlncgbnn")

code = '''int func(int a)
        {
            return a*a
        }
        '''
st.code(code,'c')

'''
- _streamlit.dataframe_`(data=None,width=None,height=None)`
- width,height _**以像素为单位**_
'''

df = pd.DataFrame(
    np.random.randn(50,20),
    columns=('col %d'%i for i in range(20))
)
st.dataframe(df)

#st.dataframe(df.style.highlight_min(axis=1))

'''
- _streamlit.table_`(data=None)`
'''
if st.checkbox("Table data"):
    st.table(df)

st.header("Display charts")

'''
_streamlit.line_char_`(data=None,width=0,height=0,use_container_width=True)`
'''
char_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)
st.line_chart(char_data)

'''
_streamlit.bar_chart_`(同上)`
'''

st.bar_chart(char_data)

'''
###   _streamlit.pyplot_`(fig=None,clear_figure=None,**kwargs)`
'''
arr = np.random.normal(1,1,size=100)
fig,ax = plt.subplots(1,1)
ax.hist(arr,bins=20)
st.pyplot(fig)


'''
_streamlit.graphviz_chart_`(figure_or_dot,use_container_width=False)`
'''

'''
###   _streamlit.map_`(data=None,zoom=None,use_container_width=True)`
'''
df = pd.DataFrame(
     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
     columns=['lat', 'lon'])

st.map(df)

st.header("Display media")
'''
_streamlit.image_`(image,caption=None,**kwargs)`
'''
from PIL import Image
image = Image.open('genie.jpg')
st.image(image,caption="盖聂")
'''
_streamlit.video_\n
_streamlit.audio_
'''

st.header("Display interactive widgets")
'''
_streamlit.button_`(label,key=None,help=None)`
'''
if st.button("wowo",help="点我",key="me"):
    st.write('点我你就对了我')
else:
    st.write("为什么不点我")

'''
_streamlit.checkbox_`(label,value=False,key=None,help=None)`
'''

agree = st.checkbox("选我",help="快选我")
if agree:
    st.write("选我你就对了我")

'''
_streamlit.radio_`(label,options,index=0,format_func=<class'str),key=None,help=None)`
'''
genra = st.radio(
    "what is your favorite movie genre",
    ('Comedy','Drama','Documentary')
)

if genra == 'Comedy':
    st.write("Comedy")
elif genra == 'Drama':
    st.write("Drama")
else:
    st.write('Documentary')

'''
_streamlit.selectbox_`('同上')`
'''

option = st.selectbox(
    "How would you like to be contacted?",
    ('Email','Home phone','Mobile phone')
)

'''
_streamlit.multiselect_`((label, options, default=None, 
format_func=<class 'str'>, key=None, help=None))`
- default ([str] or None) – List of default values.
'''
options = st.multiselect(
    'what are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red']
)
title = st.text_input('Movie title','life of Brian')
st.write('The current movie title is',title)

'''
_streamlit.slider_`(label,min_value=None,max_value=None,value=None,
step=None,format=None,key=None,help=None)`
'''
age = st.slider("How old are you?",0,130,25)
st.write("I am",age,'year old')

value = st.slider(
    'Select a range of values',
    0.0,100.0,(25.0,75.0)
)
st.write('Values:',value)

from datetime import time
appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11,30),time(12,45))
)
st.write("Your are scheduled for:",appointment)

'''
_streamlit.select_slider_`(label,options=[],value=None,
step=None,format=None,key=None,help=None)`
'''
color = st.select_slider(
    'Select a color of the rainbow',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)

start_color, end_color = st.select_slider(
    'Select a range of color wavelength',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    value=('red', 'blue'))
st.write('You selected wavelengths between', start_color, 'and', end_color)

number = st.number_input("Input a number",22,format="%e")
st.write("The current number is:",number)


txt = st.text_area('Text to analyze', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (...)
    ''')
st.write('Sentiment:', txt)

d = st.date_input(
    "When's your birthday",
    datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)

t = st.time_input('Set an alarm for', datetime.time(8, 5))
st.write('Alarm is set for', t)

upload_file = st.file_uploader("choose a file")

t = st.color_picker('Pick A Color','#00f900')
st.write("The current color is",t)

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Emal',"Home phone",'Mobile phone')
)

st.subheader("lay out your app")
'''
_streamlit.form_`(key:str)`
'''

with st.form("my_form"):
    st.write("inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider",slider_val,"chekbox",checkbox_val)
st.write("outside the form")

form = st.form("my_forms")
form.slider("inside")
st.slider('outside the form')

form.form_submit_button("submit")

'''
_streamlit.beta_container_`()`
'''
with st.beta_container():
    st.write("This is inside the container")

    st.bar_chart(np.random.randn(50,3))
st.write("This is outside the container")

container = st.beta_container()
container.write("This is inside the container")
st.write("This is outside the container")
container.write("This is inside too")


'''
###   _streamlit.beta_columns_`(spec)`
'''
col1,col2,col3 = st.beta_columns(3)
with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")
with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

col2.write("A dog")
col1.line_chart(np.random.randn(10,1))

'''
###   _streamlit.bea_expander_`(laber=None,expended=False)`
'''

with st.beta_expander("See explanation",expanded=True):
    st.write("""
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    """)
    st.line_chart({'data':[1,5,2,6,2,1]})

    st.image("https://static.streamlit.io/examples/dice.jpg")

st.subheader("Display code")
'''
_streamlit.echo_`(code_loaction=above or below)`
'''

with st.echo():
    st.write("This code will be printed")

def get_user_name():
    return 'John'

# ------------------------------------------------
# Want people to see this part of the code...

def get_punctuation():
    return '!!!'

greeting = "Hi there, "
user_name = get_user_name()
punctuation = get_punctuation()

st.write(greeting, user_name, punctuation)

# ...up to here
# ------------------------------------------------

foo = 'bar'
st.write('Done!')

def get_user_name():
    return 'John'

with st.echo():
    # Everything inside this block will be both printed to the screen
    # and executed.

    def get_punctuation():
        return '!!!'

    greeting = "Hi there, "
    value = get_user_name()
    punctuation = get_punctuation()

    st.write(greeting, value, punctuation)

# And now we're back to _not_ printing to the screen
foo = 'bar'
st.write('Done!')

st.subheader("Display progerss ans status")
'''
_streamlit.progress_'(value=int or float)'
'''

import time
my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1)

with st.spinner("wait for it..."):
    time.sleep(1)
st.success("Done!")

st.balloons()
st.error("This is an error")
st.warning("This is an warning")
st.info("This is a purely informational message")
st.success("This is an success message")

e = RuntimeError("This is an exception fo type RuntimeError")
st.exception(e)


st.subheader("Placeholders,help,and options")

import time
with st.empty():
    for seconds in range(6):
        st.write(f"{seconds} have passed")
        time.sleep(1)
    st.write("ok")
if st.checkbox("DataFrame"):
    st.help(pd.DataFrame)
