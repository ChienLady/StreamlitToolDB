import streamlit as st
def draw_style():
    st.set_page_config(page_title = 'DBtool',
                       page_icon = '🔥',
                       layout = 'wide',
                       menu_items = {
                          'Get help': 'https://www.facebook.com/chienlady/',
                          'Report a Bug': 'https://www.facebook.com/chienlady/',
                          'About': 'Trang web có mục đích riêng rư.'
                       })

    style = '''
        <style>
            header {visibility: visible;}
            footer {visibility: hidden;}
        </style>
    '''
    st.markdown(style, unsafe_allow_html = True)
draw_style()
from streamlit_option_menu import option_menu

from app.components import (
    login,
    home,
    data_iteractive
)

def init():
    st.session_state.pages = {
        'Home': home.main,
        'Documents': data_iteractive.main
    }

def load_page(page_name):
    st.session_state.pages[page_name]()

def main():
    init()
    # draw_style()
    login.main()
    if st.session_state.get('authentication_status', False):
        # Icons: https://icons.getbootstrap.com/
        page = option_menu(None, ['Home', 'Documents', 'Log Messages', 'Settings'],
                        icons=['house', 'device-hdd-fill', 'clock-history', 'gear'],
                        menu_icon='cast', default_index=0, orientation='horizontal')
        load_page(page)
        

if __name__ == '__main__':
    main()

