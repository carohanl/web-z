from PIL import Image 
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="AWS price comparator", page_icon=":sparkles✨:", layout="wide") 

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
       return None 
    return r.json()

# Use local CSS
def local_CSS(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_CSS("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = "https://lottie.host/ad02b2a9-a755-4a5d-97b8-fb9ef86ab8b8/gwxxEU4FA2.json"
#img_contact_from = Image.open("images/pic1.jpg")
#img_contact_from = Image.open("image/pic2.jng")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi From AWS :👋:")
    st.title("A Data Analysis of Price Range")
    st.write("AWS PriceTool")
    st.write("[Learn More > ](DATA FILE  .........)")

# ----  WHAT It Will DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("With our tool, you can:")
        st.write("##")
        st.write(
            """
            Compare pricing across AWS services like EC2, RDS, Lambda, S3, and more.
             - Find the best deals for your specific usage patterns.
             -Identify cost-saving opportunities through reserved instances, spot instances, and other pricing models.
             -Track regional price variations and optimize your cloud spend globally.

              Find the Best Deals for Your Cloud Needs ,Are you looking for the most cost-effective way to leverage AWS cloud services.
              Our AWS Price Comparison tool helps you compare and choose the best pricing options tailored to your specific needs. Whether you are running EC2 instances, managing databases, or utilizing S3 storage, we provide transparent comparisons of AWS pricing across different regions and services"
              Take control of your AWS budget and avoid overpaying with our easy-to-use comparison engine.
              
              Start saving today with AWS price insights!

             """
        )
        st.write("[AWS Site >](https://aws.amazon.com)")
    with right_column:
        st_lottie(lottie_coding, height = 300, key="coding")

# ---- ADD ON INFO ---- 
with st.container():
    st.write("---")
    st.header("Best To Purchase")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        # insert image
        with text_column:
            st.subheader("We Recomand Best Instances")
            st.write(
            """
            For the best recommendation,
              we need to understand your specific needs. Could you tell us what you’re looking for in a product? 
              We will suggest the perfect option based on your preferences. 
              Feel free to share any details, and we are happy to help!
              """
        )
        st.markdown("[Customer Support...](/coustomer_care/index.html)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co? !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/your@email.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name " required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
     </form>
     """
    left_column, right_column = st.columns(2)
    with left_column:                                                                                                                   
       st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()