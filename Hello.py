import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


st.write("Here's another attempt at using toy_dataset to create a graph:")
df = pd.read_csv("https://raw.githubusercontent.com/fallenpetal1/DATA200/main/foo/bar/toy_dataset.csv")
fig, x = plt.subplots()
gen_med = df.groupby(['City','Gender'])['Income'].mean().reset_index(name='count')
plt.bar(gen_med['City'], gen_med['count'])
plt.xlabel("Average Income Per City")
plt.ylabel("Average Income")
plt.title("City")
plt.xticks(rotation=45,horizontalalignment='right' )
st.pyplot(fig)

