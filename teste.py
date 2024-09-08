import pandas as pd
import plotly.express as px
import streamlit as st
import requests
import folium
from streamlit_folium import st_folium
import json


brazil_data = open('brazil_geo_json.json', 'r')
#brazil_data = json.load(f)
m = folium.Map(location=(-8.36, -38.02), zoom_start=5, control_scale=True)
state_geo = json.load(brazil_data)
print(state_geo['name'])