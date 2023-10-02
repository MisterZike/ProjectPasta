import streamlit as st
from src.application.app_logic import dish_lookup

'Project Pasta'

dish_input = st.text_input('Search Recipe', placeholder='Type name of dish here...')
st.write('You selected: ', dish_input)

option_for_unit = st.selectbox(
    'Choose your preferred unit of measurement',
    ('Imperial', 'Metric'))

st.write('You selected:', option_for_unit)

st.button('Search', on_click=dish_lookup(dish_name=dish_input, unit_of_measure=option_for_unit, serving_size=4))
#dish_lookup()