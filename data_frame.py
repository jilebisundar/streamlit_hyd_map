import streamlit as st
import numpy as np
import pandas as pd
from bokeh.plotting import figure



st.balloons()
st.snow()

st.header("displays the random number between 1,-1 with standard_normal_distribution")
st.write("highlights the maximum values in the dataframe with yellow color along with column wise")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))
st.line_chart(dataframe)


#ploting the line chart with and other table
st.header("ploting the  line ")
df_1 = pd.DataFrame({
    'X' : [1,2,3,4,5],
    'Y' : [6,7,2,4,5]
    }
)
st.dataframe(df_1.style.highlight_min())

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]
p = figure(
    title='simple line example',
    x_axis_label='x',
    y_axis_label='y')

p.line(x, y, legend_label='Trend', line_width=2)
st.bokeh_chart(p, use_container_width=True)





st.header("plotting the area chart")


chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.dataframe(chart_data)
st.write("below gives the summary statistics of above dataframe ")
st.dataframe(chart_data.describe())

st.area_chart(chart_data)




st.header("ploting a map with latitude and logitudes ")

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [17.3850, 78.4867],
    columns=['lat', 'lon'])

st.map(map_data,zoom =(9))



