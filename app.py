import streamlit as st
from multiapp import MultiApp
from apps import home, heatmap  # import your app modules here

st.set_page_config(layout="wide")

app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Heatmap", heatmap.app)


# The main app
app.run()
