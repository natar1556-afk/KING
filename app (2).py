import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt

print('app.py created with initial imports.')

st.title('Dataset Analysis Application')

# Load the dataset
df = pd.read_csv('mark.csv')
st.subheader('Raw Data (First 5 Rows)')
st.dataframe(df.head())

print('Data loading and initial display added to app.py.')

st.subheader('Interactive Visualizations')

# Get a list of all columns for selection boxes
all_columns = df.columns.tolist()

# Scatter Plot
st.write('### Scatter Plot')
x_col = st.selectbox('Select X-axis for Scatter Plot', all_columns, key='scatter_x')
y_col = st.selectbox('Select Y-axis for Scatter Plot', all_columns, key='scatter_y')

if x_col and y_col:
    fig_scatter = px.scatter(df, x=x_col, y=y_col, title=f'Scatter Plot of {y_col} vs {x_col}')
    st.plotly_chart(fig_scatter)

# Count Plot
st.write('### Count Plot')
count_col = st.selectbox('Select Column for Count Plot', all_columns, key='count_col')

if count_col:
    fig_count = px.histogram(df, x=count_col, title=f'Count Plot of {count_col}')
    st.plotly_chart(fig_count)

# Pie Chart
st.write('### Pie Chart')
pie_col = st.selectbox('Select Column for Pie Chart', all_columns, key='pie_col')

if pie_col:
    pie_data = df[pie_col].value_counts().reset_index()
    pie_data.columns = [pie_col, 'count']
    fig_pie = px.pie(pie_data, names=pie_col, values='count', title=f'Distribution of {pie_col}')
    st.plotly_chart(fig_pie)

print('Interactive visualization widgets and plots added to app.py.')

st.subheader('Summary Report')
if st.button('Generate Summary Report'):
    st.write('### Summary Statistics')
    st.dataframe(df.describe())

print('Summary report functionality added to app.py.')
