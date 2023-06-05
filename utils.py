import pydeck as pdk
import pathlib
import pandas as pd


def formatta_terrazze():
    filepath = r'./terrazze_regalo_ada.xlsx'
    in_path = pathlib.Path(filepath)
    df = pd.read_excel(in_path)
    df.description = df.description.str.replace('. ', '. <br>', regex=False)
    df['description_cleaned'] = '<h2>' + df.nome + '</h2>' + ' ' + df.description
    terrazze = df.fillna('nothing')
    return terrazze


def formatta_hotspots():
    filepath = r'./top_100_hotspots.xlsx'
    in_path = pathlib.Path(filepath)
    df = pd.read_excel(in_path)
    df['description_cleaned'] = '<h4>' + df.description_cleaned + '</h4>'
    hotspots = df.fillna('nothing')
    return hotspots


def formatta_ristoranti():
    filepath = r'./top_100_restaurants.xlsx'
    in_path = pathlib.Path(filepath)
    df = pd.read_excel(in_path)
    df['description_cleaned'] = '<h4>' + df.description_cleaned + '</h4>'
    hotspots = df.fillna('nothing')
    return hotspots


def restituisci_terrazze():
    df = formatta_terrazze()

    # Define a layer to display on a map
    layer = pdk.Layer(
        "ScatterplotLayer",
        df,
        pickable=True,
        opacity=1,
        stroked=True,
        filled=True,
        radius_scale=9,
        radius_min_pixels=10,
        radius_max_pixels=100,
        line_width_min_pixels=1,
        get_position=["lon", "lat"],
        get_radius=10,  # Radius is given in meters
        get_fill_color=[180, 0, 200, 140],  # Set an RGBA value for fill
        get_line_color=[255, 255, 255],
    )
    return layer


def restituisci_ristoranti():
    df = formatta_ristoranti()

    # Define a layer to display on a map
    layer = pdk.Layer(
        "ScatterplotLayer",
        df,
        pickable=True,
        opacity=1,
        stroked=True,
        filled=True,
        radius_scale=5,
        radius_min_pixels=5,
        radius_max_pixels=100,
        line_width_min_pixels=1,
        get_position=["lon", "lat"],
        get_radius=5,  # Radius is given in meters
        get_fill_color=[124, 252, 0, 140],  # Set an RGBA value for fill
        get_line_color=[255, 255, 255],
    )
    return layer


def restituisci_hotspots():
    df = formatta_hotspots()
    # Define a layer to display on a map
    layer = pdk.Layer(
    "ColumnLayer",
    df,
    pickable=True,
    extruded=True,
    radius=45,  # Radius is given in meters
    elevation_scale=50,
    get_position=["lon", "lat"],
    get_elevation="value",  # Use 'value' field for the column height
    get_fill_color=[246, 190, 0, 140],  # Set an RGBA value for fill
    )
    return layer







