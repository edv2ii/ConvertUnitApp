import streamlit as st
from page.portal import page
from bs4 import BeautifulSoup


class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_data(self):
        # โค้ดสำหรับโหลดข้อมูล
        pass

class Predictor:
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = self.load_model()

    def load_model(self):
        # โค้ดสำหรับโหลดโมเดล
        pass

    def predict(self, data):
        # โค้ดสำหรับทำนายข้อมูล
        pass

class Css:
    def __init__(self, pathfile=None) -> None:
        self.pathfile = pathfile
    
    # def openCss(self, label=None, tag=None, className=None, src=None, href=None):
    #     # The given HTML string
    #     if tag == "a":
    #         st.write(f"<{tag} class='{className}', href='{href}'>{label}</{tag}>", unsafe_allow_html=True)
    #     elif tag == "img": 
    #         st.write(f"<{tag} class='{className}, src='{src}'>{label}</{tag}>", unsafe_allow_html=True)
    #     else: 
    #         st.write(f"<{tag} class='{className}'>{label}</{tag}>", unsafe_allow_html=True)


    #     # if tag == "a"
        #     st.write(f"<{tag} class='{className}'>{label}</{tag}>", unsafe_allow_html=True)
        with open(f"{self.pathfile}") as f:
            st.write(f"<style>{f.read()}</style>", unsafe_allow_html=True)

class App:
    def __init__(self):
        pass

    def navigateTo(self, path):
        st.session_state["current_page"] = path
    
    def Route(*label):
        st.sidebar.title("Navigation")
        st.sidebar.button("Home", on_click=App().navigateTo, args=('home',))
        st.sidebar.button("Infix Convertion", on_click=App().navigateTo, args=('infix_convertor',))
        st.sidebar.button("Base Convertion", on_click=App().navigateTo, args=('base_convertor',))
        

        
        
        if st.session_state['current_page'] == 'home':
            page.home()
        elif st.session_state['current_page'] == 'infix_convertor':
            st.button("Infix To Postfix", on_click=App().navigateTo, args=('infix_to_postfix',))
            st.button("Infix To Prefix", on_click=App().navigateTo, args=('infix_to_prefix',))
            page.infix_convertor()
        elif st.session_state['current_page'] == 'infix_to_postfix':
            st.button("Infix To Postfix", on_click=App().navigateTo, args=('infix_to_postfix',))
            st.button("Infix To Prefix", on_click=App().navigateTo, args=('infix_to_prefix',))
            page.infix_to_postfix()
        elif st.session_state['current_page'] == 'infix_to_prefix':
            st.button("Infix To Postfix", on_click=App().navigateTo, args=('infix_to_postfix',))
            st.button("Infix To Prefix", on_click=App().navigateTo, args=('infix_to_prefix',))
            page.infix_to_prefix()    
        elif st.session_state['current_page'] == 'base_convertor':
            page.base_convertor()   
            
            
    

    def run(self):
        if "current_page" not in st.session_state:
            st.session_state["current_page"] = 'home'
        app.Route()
        
        
        
        # โค้ดสำหรับสร้าง UI และโต้ตอบกับผู้ใช้

if __name__ == "__main__":
    app = App()
    app.run()
    
    
    

