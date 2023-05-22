import view.zooView as viewZoo
import streamlit as st

if __name__ == '__main__':
    st.set_page_config(
        page_title = "Zoologico",
        layout = "wide"
    )
    sara = viewZoo.vistaZoo()
    sara.mostrar_menu()