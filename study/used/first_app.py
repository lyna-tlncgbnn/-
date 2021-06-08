import numpy as np
import pandas as pd
import streamlit as st

st.title("My first app")
st.write("Here is out first attempt at using data to create a table:")
'''
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 5],
    'second column': [10, 20, 30, 40]
}))
'''
df = pd.DataFrame({'first column': [1, 2, 3, 5],'second column': [10, 20, 30, 40]})
df

char_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)

st.line_chart(char_data)
st.line_chart(df)
data = np.random.randn(100)
st.line_chart(data)

if st.checkbox('show dataframe'):
    char_data = pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])
    char_data
    st.line_chart(char_data)

option = st.selectbox('Which number do you like best',df['first column'])
"You selected:",option,100
option = st.sidebar.selectbox("which number do you like best?",df['first column'])
'Your selected',option

left_column,right_column = st.beta_columns(2)
pressed = left_column.button("Press me?")
if pressed:
    right_column.write("Woohoo!")

expander = st.beta_expander("FAQ")
expander.write("Here you colud put in some really,really long explantions...")
ta = right_column.button("Press")

import time
'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'