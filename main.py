import streamlit as st
from src.application.app_logic import dish_lookup
import time

# This should be the user interface

def button_press(dish_input, option_for_unit, serving):
    st.session_state['recipe'] = dish_lookup(dish_input,option_for_unit, serving)
    # st.header(st.session_state['recipe'])


if 'recipe' not in st.session_state:
    st.session_state['recipe'] = ''

#
# class ViewOne:
#     def __init__(self):
#         st.header("VIEW 1")
#         st.write("This is view 1")
#
#
# class ViewTwo:
#     def __init__(self):
#         st.header("VIEW 2")
#         st.write("This is view 2")
#
#
# class StreamLit:
#     def __init__(self, view_one, view_two):
#         self.a = view_one
#         self.b = view_two
#         i = str
#         if 'n' not in st.session_state:
#             st.session_state['n'] = 1
#     def print_view_1(self):
#         st.header("VIEW 1")
#         st.write("This is view 1")
#
#     def print_view_2(self):
#         st.header("VIEW 2")
#         st.write("This is view 2")
#
#     def toggle(self):
#         def toggle_view():
#             st.session_state['n'] += 1
#
#         st.button('Toggle', on_click=toggle_view)
#         while True:
#             if st.session_state['n'] % 2 == 0:
#                 return self.print_view_1()
#
#             else:
#                 return self.print_view_2()
#
#
# if __name__ == "__main__":
#     interface = StreamLit()
#
#     interface.toggle()

st.header('Project Pasta')

dish_input = st.text_input('Search Recipe', placeholder='Type name of dish here...')
st.write('You selected: ', dish_input)

option_for_unit = st.selectbox(
    'Choose your preferred unit of measurement',
    ('Imperial', 'Metric'))
st.write('You selected:', option_for_unit)

serving_size = st.slider('Choose your serving size', min_value=1, max_value=8, value=2)
st.button('Search', on_click=button_press, args=[dish_input, option_for_unit, serving_size])

display = st.empty()
display.write(st.session_state['recipe'])
