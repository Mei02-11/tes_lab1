import streamlit as st
from PIL import Image  # Import Image from Pillow

st.title("🎈 testtt")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.header("Hello world!") 
st.subheader("Hello world!!")
st.text("Hello world!!!")
# Create a dropdown menu for selecting a hobby
hobby = st.selectbox("Select a Hobby:", ['Dancing', 'Reading', 'Sports'])

# Display the selected hobby
st.write("Your hobby is:", hobby)

st.button("Click Me")
if st.button("About"):
    img = Image.open("images.png") # Open the image file
    st.image(img, width=200) # Display the image with a specified width
