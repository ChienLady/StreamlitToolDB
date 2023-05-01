import requests
import streamlit as st
from streamlit_extras.let_it_rain import rain
from streamlit_lottie import st_lottie
from streamlit_extras.add_vertical_space import add_vertical_space

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def main():
    ani, wel = st.columns(2)
    with ani:
        st_lottie(load_lottieurl('https://assets3.lottiefiles.com/packages/lf20_xnbikipz.json'), quality='high', key='lottie', height=400)
    with wel:
        st.header(f'Welcom back, **{st.session_state["username"]}!**')
        st.session_state['role'] = st.session_state['config']['accounts'].get(st.session_state['username'], 'reviewer')
        st.subheader(f'Your role: **{st.session_state["role"]}**')
        st.session_state['permissions'] = st.session_state['config']['permissions'][st.session_state["role"]]
        for p in st.session_state['permissions']:
            st.checkbox(p, True, p)
        rain(
            emoji = '🎁',
            font_size = 30,
            falling_speed = 10,
            animation_length = 'infinite',
        )
        add_vertical_space(5)
    st.markdown(
        '''
---
<p align="middle"> Backend: <b> AITeam </b> </p>
<p align="middle"> Copyright © 1994 - 2023 MISA JSC </p>  
        ''',
        unsafe_allow_html=True
    )
