import streamlit as st
import math
import numpy as np
import pandas as pd

try:
    from scipy import stats
    SCIPY_AVAILABLE = True
except:
    SCIPY_AVAILABLE = False


st.set_page_config(
    page_title= 'Aplikasi Uji Hipotesis',
    layout= 'wide',
    page_icon='☁'
)
 st.
