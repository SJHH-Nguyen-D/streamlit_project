from sklearn.datasets import load_boston
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pprint
import numpy as np
from PIL import Image
import time
np.random.seed(32)
import os

# Loading in data
boston = load_boston()
df = pd.DataFrame(data=boston.data, columns=boston.feature_names)
df['target'] = boston.target



st.title('Streamlit Exploration')
st.markdown('')

st.graphviz_chart("""
digraph D {
  
  # Formatting
  "Time Series Data" [shape=Mdiamond, style=filled];
  "Time Stamps" [style=filled];
  "Temporal" [style=filled];
  "Sequential" [style=filled];
  "Preprocessing" [style=filled];
  "Pandas" [style=filled];
  "Datetime Formatting" [style=filled];
  "Time Shifting" [style=filled];
  node [shape=record]


  "Time Stamps" -> "Time Series Data";
  "Temporal" -> "Time Series Data";
  "Sequential" -> "Time Series Data";
  "Time Series Data" -> Preprocessing;

  Preprocessing -> "Pandas" -> {"Datetime Formatting", "Time Shifting"} -> {"..."};

  "..." -> {"Time Series Data Science Problem Answered"};

}

""")


x = st.slider('x')
st.write(x, 'squared is', x * x)

st.markdown(f"""{boston.DESCR[20:]}""")

st.write("Here's our first attempt at using data to create a table:")
st.write(df.head(20))
st.write("The static version of this dataframe:")

# stylizes a table using styler object to highlight max values
st.table(df.head().style.highlight_max(axis=0))

feature_label = st.selectbox('Filter to:', df.columns)
st.write(f"You've selected: {feature_label}")
st.write(f"Distribution of {feature_label} in Boston")
st.bar_chart(data=df[feature_label], width=0, height=0, use_container_width=True)
df.style.highlight_max(axis=0)

##### side bar items #####

# resize image to have width of 300, and heigh proportional to it
basewidth = 250
url = f'{os.getcwd()}/bb_logo1.png'
image = Image.open(url)
wpercent = (basewidth/float(image.size[0]))
hsize = int((float(image.size[1])*float(wpercent)))
image = image.resize((basewidth,hsize), Image.ANTIALIAS)
st.sidebar.image(image, 
                 use_column_width=True,
                 format='PNG')

st.sidebar.subheader('Chart Playground')
area_chart_show = st.sidebar.checkbox('Show Area Chart')
sf_map_show = st.sidebar.checkbox('Show Map of SF')
start_bar = st.sidebar.checkbox('Run progress bar')
show_line_chart = st.sidebar.checkbox('Show DataFrame and Line Chart')

if area_chart_show:
    st.write('Area Chart')
    chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
    st.area_chart(chart_data)

if sf_map_show:
    st.write('San Francisco Map')
    map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])
    st.map(map_data)


# Create a progress bar
# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)


if start_bar:
    st.write('Starting a long computation...')
    for i in range(100):
    # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.01)

    st.write('...and now we\'re done!')

# Line chart
if show_line_chart:
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)



# You can transition and adjust data by adding transition delay
# Get some data.
data = np.random.randn(10, 2)
# Show the data as a chart.
chart = st.line_chart(data)
# Wait 1 second, so the change is clearer.
time.sleep(3)
# Grab some more data.
data2 = np.random.randn(10, 2)
# Append the new data to the existing chart.
chart.add_rows(data2)

