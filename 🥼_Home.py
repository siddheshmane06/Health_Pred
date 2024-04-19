It looks like you're encountering an indentation error in your Python code. In Python, indentation is crucial for indicating the structure of your code. In your case, the `st.markdown` calls inside the `home` function seem to have inconsistent indentation.

Here's the corrected version of your code with consistent indentation:

```python
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

home()  # Call the function to execute the code
```

Make sure all the lines inside the `home` function have the same level of indentation (typically 4 spaces or a tab). This should resolve the `IndentationError` you're encountering.
