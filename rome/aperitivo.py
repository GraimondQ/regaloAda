import streamlit as st
import pydeck as pdk
from utils import formatta_terrazze, restituisci_terrazze, restituisci_ristoranti, restituisci_hotspots


st.title('Introducing A:red[.]PER:red[.]I:red[.]TI:red[.]VO')
st.markdown("### :red[A]da's :red[PER]sonal :red[I]ncredibly :red[TI]dy :red[VO]ucher generating tool")


st.divider()


st.markdown(
"""
A.PER.I.TI.VO è stato concepito per offrire una risposta di livello alle necessità di Ada di esplorare Roma,
La mappa interattiva, realizzata con tecniche _cutting edge_ di web scraping riporta
- in **:violet[viola]**: i _rooftops_ più belli di Roma e relativa breve descrizione
- in **:green[verde]**: i migliori 100 ristoranti della Capitale
- in cilindri **:orange[gialli]**: luoghi storici di interesse per agevolare l'orientamento nella fruzione del sito 

La scelta dei _rooftops_ è stata condotta a mano con cura, effettuando uno scraping manuale delle migliori risorse per selezionare le 20 migliori location da visitare.
\\
A seguire, la selezione dei 100 migliori ristoranti è il risultato dell'analisi di un dataset contenente più di 50.000 esercizi commerciali, valutati secondo recensioni da TripAdvisor e Google.
""")


terrazze_layer = restituisci_terrazze()
ristoranti_layer = restituisci_ristoranti()
hotspots_layer = restituisci_hotspots()


# Set the initial viewport
view_state = pdk.ViewState(
    latitude=formatta_terrazze()['lat'].mean(),
    longitude=formatta_terrazze()['lon'].mean(),
    zoom=10,
    min_zoom=5,
    max_zoom=15,
    pitch=40.5,
    bearing=-27.36,
)

# Create the deck.gl map
r = pdk.Deck(
    layers=[terrazze_layer, ristoranti_layer, hotspots_layer],
    initial_view_state=view_state,
    tooltip={"html": "{description_cleaned}"},
)


# Render the deck.gl map in the Streamlit app
st.pydeck_chart(r)
