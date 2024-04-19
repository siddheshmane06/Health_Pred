import streamlit as st

def home():
    st.set_page_config(
        page_title="HealthPred - Home",
        page_icon="👨‍⚕️",
    )
    st.image("img/logo.png")
    
    st.markdown(
        '<p style="font-size:22px; text-align: center; color: black;font-size: 25px;">Connected Health, Connected Lives: Seamless Solutions for Every Step of the Journey</p>',
        unsafe_allow_html=True
    )
    st.markdown("---")

    st.markdown(
        f"<p style='text-align: center; color: black; font-size: 20px'>💠 "Unlocking the Potential of Digital Health: Harnessing Technology, Personalized Solutions, and Advanced Analytics to Revolutionize Healthcare and Elevate Your Care Experience Today."</p>",
        unsafe_allow_html=True
    )
    st.markdown("---")

    st.markdown(
        f"<p style='text-align: center; color: black; font-size: 20px'>💠 We provide digital health and healthcare solutions to help common people and health organizations power their care experience and improve health outcomes with advanced analytics</p>",
        unsafe_allow_html=True,
    )

    st.markdown("---")

    st.markdown(
        f"<h2 style='text-align: center; color: black'>Our Services</h2>",
        unsafe_allow_html=True,
    )
    st.write("")

    st.markdown(
        f"⚕️ **Disease Diagnosis** - Enter the symptoms you are suffering from and you will get to know the disease you are suffering from, precautions to take, medications and specialists near you to cure the disease"
    )
    st.markdown(
        f"⚕️ **Early Diabetes Detection** - Enter the patients attributes from the test report and check whether he/she have chances of diabetes or not"
    )

    st.markdown(
        f"⚕️ **Liver Disease Detection** - Enter the patients attributes from the test report and check whether he/she have chances of any type of liver disease or not"
    )

    st.markdown(
        f"⚕️ **Pneumonia Detection** - Upload the chest X-ray image of the patient and check whether the patient have chances of Pneumonia"
    )

home()  # Call the function to execute the code
