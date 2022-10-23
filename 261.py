import pickle
import numpy as np
import matplotlib.pyplot as plt 
from scipy.signal import find_peaks
import os
import pytest

if os.path.getsize('/Users/utkucicek/Desktop/bme 261/106m.pkl')> 0 :
    with open('/Users/utkucicek/Desktop/bme 261/106m.pkl', 'rb') as file:
        loaded = pickle.load(file)
# print(loaded)

fs = 360
T = 5
time = np.linspace(0, T, fs * T)
signal = loaded[:fs * T]
signal = np.array(signal)
signal = signal / 200
print(signal.shape)
signal.shape

def test_fs_is_int():
    assert type(fs) == int

def test_time_is_not_int():
    assert type(time) != int

def test_signal_not_int():
    assert type(signal) != int