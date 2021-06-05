import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from io import BytesIO
from mpl_toolkits.mplot3d import Axes3D
import torch
from dataprocess import getdata
from network2 import SoundClassifyNet2D
from dataprocess import predict
def show(csv_data,model):
    '''
    原始数据波形图
    '''
    st.subheader("原始波形图")
    fig , ax = plt.subplots()
    ax.plot(csv_data)
    st.pyplot(fig)
    mfcc_data = getdata(csv_data)
    if mfcc_data:
        st.write("success")
    else:
        st.write("false")
    st.subheader("mfcc")
    mfcc_da = np.array(mfcc_data)
    st.line_chart(mfcc_da.T)
    fig = plt.figure()
    plt.imshow(mfcc_data, cmap=plt.cm.jet, extent=[0, mfcc_data.shape[1], 0, mfcc_data.shape[0]], aspect='auto')
    st.pyplot(fig)
    res,Bool = predict(mfcc_data,model)
    res = res.detach().numpy()
    st.subheader("三维特征图")
    fig = plt.figure(figsize=(8,8))
    ax = fig.gca(projection='3d')
    ax.scatter(res[0],res[1],res[2],c=Bool*10)
    st.pyplot(fig)
    st.header("诊断结果")
    if Bool:
        st.success("正常")
    else:
        st.error("故障")
def get_model():
    model = SoundClassifyNet2D(2)
    checkpoint1 = torch.load('model.pth', map_location=torch.device('cpu'))
    model.load_state_dict({k.replace('module.', ''): v for k, v in checkpoint1.items()})
    return model
def run_app():
    st.sidebar.markdown('### 第一步：选择样例文件或者上传本地文件(csv)')
    choice = st.sidebar.selectbox("选择文件",("样例一","样例二","本地文件"))
    if choice=="本地文件":
        file = st.sidebar.file_uploader("选择本地文件")
    elif choice=="样例一":
        file = pd.read_csv("good.csv",header=None)
    else:
        file = pd.read_csv("bad.csv",header=None)
    st.sidebar.markdown("### 第二步：点击查看结果")
    left,mid,right = st.sidebar.beta_columns(3)
    st.header("马达声音测试")
    st.subheader("使用方法")
    '''
    - 第一步：选择本地文件
    - 第二步：点击诊断查看结果
    '''
    model = get_model()
    model.eval()
    if mid.button("诊断"):
        if choice=="本地文件":
            csv_data = pd.read_csv(file, header=None)
            show(csv_data,model)
        else:
            show(file,model)           
run_app()
