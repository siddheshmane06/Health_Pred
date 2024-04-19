import streamlit as st

def home():
    st.set_page_config(
        page_title="HealthPred - Home",
        page_icon="👨‍⚕️",
    )
  st.markdown(
        '<p style="font-size:22px; text-align: center; color: black;font-size: 25px;">Improving Healthcare, Improving Lives, Bridging the gap between technology and health</p>',
        unsafe_allow_html=True
    )
    st.markdown("---")

    st.markdown(
        f"<p style='text-align: center; color: black; font-size: 20px'>💠 We provide digital health and healthcare solutions to help common people and health organizations power their care experience and improve health outcomes with advanced analytics</p>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    home()
