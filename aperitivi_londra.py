import folium
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
from utils import *
from streamlit_folium import st_folium, folium_static



st.title('Introducing A:red[. - ] D:red[.]A:red[.]T:red[.]E')
st.markdown("### :red[A]da's :red[D]inner :red[A]rrangement & :red[T]able :red[E]xperience interactive map")


with st.expander("Aggiungi un nuovo ristorante da provare!"):
    with st.form("my_form"):
       nome = st.text_input('Inserisci il nome')
       url_thumbnail = st.text_input('Inserisci url thumbnail (è l\'immagine che viene visualizzata quando clicchi il segnalino sulla mappa)')
       url_video = st.text_input('Inserisci url video')
       indirizzo = st.text_input('Inserisci l\'indirizzo')
       country_selected = st.selectbox(label='Seleziona il tipo di cucina', options=list(COUNTRY_NAME_TO_CODE_DICT.keys()))
       submitted = st.form_submit_button("Submit")
       if submitted:
           latitude, longitude = restituisci_coordinate_da_indirizzo_approssimativo(indirizzo)
           visited = False
           country_code = COUNTRY_NAME_TO_CODE_DICT[country_selected]
           icon_image = f"https://purecatamphetamine.github.io/country-flag-icons/3x2/{country_code}.svg"
           data_to_be_appended = [nome, url_thumbnail, url_video, indirizzo, latitude, longitude, icon_image, visited]
           df_to_be_appended = pd.DataFrame([data_to_be_appended], columns=pd.read_excel('data/london.xlsx').columns)
           df_new = pd.concat([pd.read_excel('data/london.xlsx'), df_to_be_appended])
           df_new.to_excel('data/london.xlsx', index=False)


df = pd.read_excel('data/london.xlsx')


with st.expander('Per indicare un luogo visitato (cambiando il colore del marker da rosso a grigio) inserisci qui il nome'):
    with st.form('visited_form'):
        st.write("Hai già visitato un posto? Inserisci qui il nome")
        nome = st.text_input('Inserisci il nome del posto che hai già visitato')
        submitted = st.form_submit_button("Submit")
        if submitted:
            df.loc[df['nome'].str.contains(nome), 'visited'] = True
            df.to_excel('data/london.xlsx', index=False)


df = pd.read_excel('data/london.xlsx')

m = folium.Map(location=[51.5373595, -0.1582341], zoom_start=12, tiles='Cartodb Positron')


for index, row in df.iterrows():
    name = row['nome']
    url_thumbnail = row['url_thumbnail']
    url_video = row['url_video']
    address = row['indirizzo']
    latitude, longitude = row['latitude'], row['longitude']
    icon_image = row['icon_image']

    url_thumbnail_encoded = get_image_base64(url_thumbnail)
    html = build_html_popup(name, address, url_video, url_thumbnail_encoded)
    iframe = folium.IFrame(html, width=400, height=350)
    popup = folium.Popup(iframe, max_width=400)
    icon = folium.features.CustomIcon(icon_image=icon_image, icon_size=(42, 42))

    if row['visited'] == True:
        folium.Marker(location=[latitude, longitude], popup=popup,
                      icon=icon).add_to(m)

    elif row['visited'] == False:
        folium.Marker(location=[latitude, longitude], popup=popup,
                      icon=icon).add_to(m)


folium.Marker(location=[51.5122375, -0.076242], popup='Casa!',
                      icon=folium.Icon(color='beige', icon='heart')).add_to(m)


st_data = folium_static(m, width=800, height=800)


with st.expander('Database dei luoghi da provare'):
    st.info(f'Ci sono {df.shape[0]} ristoranti in totale nel database!')
    st.info(f"Finora abbiamo provato {df['visited'].sum()} ristoranti!")
    st.dataframe(df)

