from __future__ import annotations

import streamlit as st 
import sys

from datetime import datetime, timedelta


sys.path.insert(1, './modules')
# print(sys.path.insert(1, '../modules/'))


from dotenv import load_dotenv

load_dotenv()



st.markdown(
    """
    <div class=title>
        <div style=" justify-content: center;">
            <h1 style="text-align: center; margin-top: -50px; color: #007B8A;">PAW AI 🐾</h1>
            <p style="text-align: center;">Guardians of the wild, powered by AI.</p>
        </div>
    </div> 
    """,
    unsafe_allow_html=True,
)

st.image('https://img.freepik.com/premium-vector/wild-animals-fauna-silhouettes-scene_24908-67621.jpg', width=900)


st.markdown(
    """
    <div class=title>
        <div style=" justify-content: center;">
            <h3 style="text-align: center; margin-top: -50px; color: #007B8A;">Join hands in making the world a sanctuary for wildlife.</h3>
        </div>
    </div> 
    """,
    unsafe_allow_html=True,)

st.markdown("""
        **1. Conservation & Habitat Protection**  
        Seeing parks, reserves, forests and sanctuaries on a map helps us understand where animals live, breed or migrate. It shows gaps or corridors that are essential for their survival, so we can protect them from isolation or habitat loss.

        **2. Community Engagement & Ownership**  
        When locals can view wildlife areas, species info, fees and access info easily, it builds awareness and pride. It empowers community members to care, protect, and benefit from conservation and eco-tourism.

        **3. Smarter Planning & Decision-Making**  
        Mapped data helps government, NGOs & tech teams plan patrols, allocate resources, address human-wildlife conflict zones, or realize where land use change is threatening wildlife. It makes responses timely & efficient.

        **4. Boosting Eco-Tourism & Sustainable Livelihoods**  
        Clear info (what species, when open, cost) helps tourists plan visits. Tourism revenue flows to guides, lodges, local businesses. When local communities benefit, they support conservation more.

        **5. Environmental Threat Mitigation**  
        Mapping protected areas near human settlements or threatened forests helps detect and respond to threats: poaching, deforestation, climate-induced habitat changes. Early warning & buffer zones become possible.
        """)


st.image("https://wildlife-conservation.streamlit.app/~/+/media/b6c97c7bba701236664a52fb9d6af7f6db94165f56eb2b5fdf5be61b.png", width=700)

# =============================================================================


import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium

def get_kenya_wildlife_sites():
    """
    Returns a pandas.DataFrame with the list you provided:
    National Parks, Game Reserves, Sanctuaries, Forests
    with metadata where available.
    """
    data = [
        # National Parks
        {"name":"Amboseli National Park", "type":"National Park",
         "lat": -2.6527, "lon": 37.2606,
         "species":"Elephants, Lions, Giraffes, Buffalo, Wildebeest; ~50 mammal spp, 420+ bird spp", 
         "opening_hours":"6:00 AM ‒ 6:00 PM", 
         "entry_fee":"Citizen KES 860 / Non-Resident USD 60", 
         "other_info":"Road access via Kimana, Meshanani, Iremito gates; guides available", 
        },
        {"name":"Lake Nakuru National Park", "type":"National Park",
         "lat": -0.39339, "lon": 36.08586,
         "species":"Black & White Rhinos, ~450 bird species incl flamingos, pelicans, herons; lions, leopards etc", 
         "opening_hours":"Daily, dawn to dusk (~6:00 AM ‒ 6:00 PM)", 
         "entry_fee":"Citizen/Resident KES 860 / Non-Resident USD 60", 
         "other_info":"Multiple gates (Lanet, Main, Nderit); scenic viewpoints like Baboon Cliff", 
        },
        {"name":"Nairobi National Park", "type":"National Park",
         "lat": -1.37333, "lon": 36.85889,
         "species":"[TBD]", "opening_hours":"[TBD]", "entry_fee":"[TBD]", "other_info":"Close to Nairobi city", 
        },
        {"name":"Tsavo East National Park", "type":"National Park",
         "lat": -2.780556, "lon": 38.564167, "species":"[TBD]", "opening_hours":"[TBD]", "entry_fee":"[TBD]", "other_info":"[TBD]"},
        {"name":"Tsavo West National Park", "type":"National Park",
         "lat": -2.88, "lon": 38.06, "species":"[TBD]", "opening_hours":"[TBD]", "entry_fee":"[TBD]", "other_info":"[TBD]"},
        {"name":"Meru National Park", "type":"National Park",
         "lat": 0.0881, "lon": 38.1900, "species":"[TBD]", "opening_hours":"[TBD]", "entry_fee":"[TBD]", "other_info":"[TBD]"},
        {"name":"Mount Kenya National Park", "type":"National Park",
         "lat": 0.1500, "lon": 37.3075, "species":"[TBD]", "opening_hours":"[TBD]", "entry_fee":"[TBD]", "other_info":"[TBD]"},
        {"name":"Hell's Gate National Park", "type":"National Park",
         "lat": -0.878774, "lon": 36.323478, "species":"[TBD]", "opening_hours":"[TBD]", "entry_fee":"[TBD]", "other_info":"[TBD]"},
        {"name":"Mount Elgon National Park", "type":"National Park",
         "lat": 1.143333, "lon": 34.563889, "species":"[TBD]", "opening_hours":"[TBD]", "entry_fee":"[TBD]", "other_info":"[TBD]"},
        {"name":"Lake Turkana National Park", "type":"National Park",
         "lat": 4.0, "lon": 36.1, "species":"[TBD]", "opening_hours":"[TBD]", "entry_fee":"[TBD]", "other_info":"[TBD]"},
        {"name":"Kora National Park", "type":"National Park",
         "lat": 2.25, "lon": 38.9833, "species":"[TBD]", "opening_hours":"[TBD]", "entry_fee":"[TBD]", "other_info":"[TBD]"},
        {"name":"Chyulu Hills National Park", "type":"National Park",
         "lat": -2.5912, "lon": 37.85751, "species":"[TBD]", "opening_hours":"[TBD]", "entry_fee":"[TBD]", "other_info":"[TBD]"},
        # Game Reserves
        {"name":"Maasai Mara National Reserve", "type":"Game Reserve",
         "lat": -1.4061, "lon": 35.0219, "species":"[TBD]", "opening_hours":"[TBD]", "entry_fee":"[TBD]", "other_info":"[TBD]"},
        {"name":"Samburu National Reserve", "type":"Game Reserve",
         "lat": 0.6243, "lon": 37.5361, "species":"[TBD]", "opening_hours":"[TBD]", "entry_fee":"[TBD]", "other_info":"[TBD]"},
        {"name":"Shimba Hills National Reserve", "type":"Game Reserve",
         "lat": -4.234, "lon": 39.323, "species":"[TBD]", "opening_hours":"[TBD]", "entry_fee":"[TBD]", "other_info":"[TBD]"},
        # ... (add the rest similarly)
        # Sanctuaries
        {"name":"Lewa Wildlife Conservancy", "type":"Sanctuary",
         "lat": 0.2431, "lon": 37.2833, "species":"[TBD]", "opening_hours":"[TBD]", "entry_fee":"[TBD]", "other_info":"[TBD]"},
        {"name":"Ol Pejeta", "type":"Sanctuary",
         "lat": -0.028333, "lon": 37.049167, "species":"[TBD]", "opening_hours":"[TBD]", "entry_fee":"[TBD]", "other_info":"[TBD]"},
        # ... others
        # Forests
        {"name":"Kakamega Forest", "type":"Forest",
         "lat": 0.2895, "lon": 34.7529, "species":"[TBD]", "opening_hours":"[TBD]", "entry_fee":"[TBD]", "other_info":"[TBD]"},
        {"name":"Arabuko Sokoke Forest", "type":"Forest",
         "lat": -3.22, "lon": 39.92, "species":"[TBD]", "opening_hours":"[TBD]", "entry_fee":"[TBD]", "other_info":"[TBD]"},
        # etc for the rest
    ]
    return pd.DataFrame(data)

def plot_wildlife_sites_map(df):
    """
    Plot the given DataFrame of wildlife sites using folium in Streamlit,
    with clusters, different icons/colors per category, tooltips/popups with metadata.
    """
    # Map setup
    kenya_center = (0.0236, 37.9062)
    m = folium.Map(location=kenya_center, zoom_start=6, control_scale=True)
    marker_cluster = MarkerCluster(name="Wildlife Sites").add_to(m)
    
    # Icon/color mapping per type
    type_icon_color = {
        "National Park": ("glyphicon-tree-conifer", "darkgreen"),
        "Game Reserve": ("glyphicon-tower", "olive"),
        "Sanctuary": ("glyphicon-heart", "cadetblue"),
        "Forest": ("glyphicon-leaf", "darkblue"),
    }
    
    for _, row in df.iterrows():
        icon_name, color = type_icon_color.get(row["type"], ("glyphicon-map-marker", "gray"))
        popup_html = f"""
        <b>{row['name']}</b><br/>
        <em>Type:</em> {row['type']}<br/>
        <em>Species:</em> {row.get('species','Information not available')}<br/>
        <em>Opening hours:</em> {row.get('opening_hours','TBD')}<br/>
        <em>Entry fee:</em> {row.get('entry_fee','TBD')}<br/>
        <em>Other info:</em> {row.get('other_info','')}<br/>
        """
        folium.Marker(
            location=(row["lat"], row["lon"]),
            popup=popup_html,
            tooltip=row["name"],
            icon=folium.Icon(color=color, icon=icon_name, prefix="glyphicon")
        ).add_to(marker_cluster)
    
    folium.LayerControl().add_to(m)
    return m

def main():
    # st.set_page_config(layout="wide", page_title="Kenya Wildlife Sites Map")
    # st.title("Kenya Wildlife Sites Map")
    df = get_kenya_wildlife_sites()
    st.sidebar.header("Filter by Type")
    types = ["All"] + sorted(df["type"].unique().tolist())
    typeselect = st.sidebar.selectbox("Select type:", types, index=0)
    
    if typeselect != "All":
        df_filtered = df[df["type"] == typeselect]
    else:
        df_filtered = df
    
    show_table = st.sidebar.checkbox("Show data table", True)
    if show_table:
        st.dataframe(df_filtered)
    
    m = plot_wildlife_sites_map(df_filtered)
    st.subheader("Map of Parks, Reserves, Sanctuaries & Forests in Kenya")
    st_folium(m, width=1200, height=700)

if __name__ == "__main__":
    main()
