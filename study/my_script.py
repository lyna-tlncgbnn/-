import streamlit as st
import numpy as np
import pandas as pd

st.subheader("Data")
dataframe = np.random.randn(10,20)
st.dataframe(dataframe)

dataframe = pd.DataFrame(
    np.random.randn(10,20),
    columns=('col %d'% i for i in range(20))
)
st.dataframe(dataframe.style.highlight_max(axis=0))

x = st.slider("x")
st.write(x,'squaered is ',x*x)