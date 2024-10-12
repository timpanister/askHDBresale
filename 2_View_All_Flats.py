import streamlit as st
import pandas as pd
import pydeck as pdk

# Load DataFrame from CSV
df = pd.read_csv('./data/hdb_2024.csv')

st.title("Dataset 2024")

# Group by 'Postal', 'Latitude', 'Longitude', 'flat_type', and 'town' and count the number of rows
grouped_df = df.groupby(['postal_code', 'latitude', 'longitude', 'flat_type', 'town']).size().reset_index(name='count')

# Create a selectbox for town with an "All" option
towns = ['All'] + sorted(df['town'].unique().tolist())
selected_town = st.selectbox("Select town", towns)

# Create a selectbox for flat type with an "All" option
flat_types = ['All'] + sorted(df['flat_type'].unique().tolist())
selected_flat_type = st.selectbox("Select flat type", flat_types)

# Filter the grouped DataFrame based on the selected town and flat type
if selected_town == 'All' and selected_flat_type == 'All':
    filtered_grouped_df = grouped_df
elif selected_town == 'All':
    filtered_grouped_df = grouped_df[grouped_df['flat_type'] == selected_flat_type]
elif selected_flat_type == 'All':
    filtered_grouped_df = grouped_df[grouped_df['town'] == selected_town]
else:
    filtered_grouped_df = grouped_df[(grouped_df['town'] == selected_town) & (grouped_df['flat_type'] == selected_flat_type)]


# Define the view state
view_state = pdk.ViewState(
    latitude=filtered_grouped_df['latitude'].mean(),
    longitude=filtered_grouped_df['longitude'].mean(),
    zoom=11,
    pitch=50,
    controller=True
)

# Define the HexagonLayer
hexagon_layer = pdk.Layer(
    'HexagonLayer',
    data=filtered_grouped_df,
    get_position=["longitude", "latitude"],
    radius=30,
    elevation_scale=2,
    elevation_range=[0, 1000],
    pickable=True,
    auto_highlight=True,
    extruded=True,
)


# Render the map with both layers
st.title("Map visualization of HDB Resale transaction volumes")

chart= pdk.Deck(
        map_style=None,
        initial_view_state=view_state,
        layers=[hexagon_layer],
        tooltip ={"text": "{}, {count},{flat_type},{town}"},
)        

event = st.pydeck_chart(chart, on_select="rerun", selection_mode="multi-object")

event.selection