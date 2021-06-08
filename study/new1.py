import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import torch
from dataprocess import getdata
from network2 import SoundClassifyNet2D
from dataprocess import predict
from train2D import start      