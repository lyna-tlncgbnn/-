import pandas as pd
import numpy as np
import librosa
import glob
import os
import torch

def extract_mfcc(audio_data,n_mfcc):
    mfccs = librosa.feature.mfcc(audio_data,n_mfcc=n_mfcc,lifter=0) #(n_mfcc,t)
    return np.mean(mfccs.T,axis=0)
def extract_mfcc2D(audio_data,n_mfcc):
    mfccs = librosa.feature.mfcc(audio_data,n_mfcc=n_mfcc,lifter=0)
    return mfccs
def getdata(file):
    filter_size = 30000
    stride = 10000
    audio_data = file.values[:,0]
    data_sum = audio_data.shape[0]
    seg_num = int((data_sum - filter_size)/stride+1)
    data_seg = list()
    for i in range(seg_num):
        first_idx = stride*i
        last_idx = first_idx + filter_size
        data_seg.append(np.array(audio_data[first_idx:last_idx]))
        #extract mfcc feature
    feature = []
    for j in data_seg:
        mfccs_dim = 128
        mfccs = extract_mfcc(j,n_mfcc=mfccs_dim)
        feature.append(mfccs)
    feature = np.array(feature)
    feature = torch.tensor(feature)
    print(feature.shape)
    print("finish")
    return feature

def predict(data,model):
    data = data.float()
    data = data.reshape(1, 1, 13, 128)
    data = torch.cat((data, data), dim=0)
    res,out = model(data)
    out = torch.argmax(out, dim=1)
    if(out[0]==1):
        return res[0],1
    else:
        return res[0],0


    
