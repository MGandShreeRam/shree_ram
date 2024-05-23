import streamlit as st 
import qrcode
from PIL import Image
from random import randint

code = st.text_input("Enter your first code")
number = int(st.number_input("Enter last number"))

st.image("infrared spectroscopy.png")

def forward():
    global number,code
    
    qr = qrcode.QRCode(version=1,
                    error_correction = qrcode.constants.ERROR_CORRECT_H,
                    box_size=50,border=10,)
    number = number + randint(0,10)
    qr_code = code + str(number)
    qr.add_data(qrcode)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("infrared spectroscopy.png")
    st.image("infrared spectroscopy.png")
    forward_btn = st.button("Forward",on_click=forward())
    
forward_btn = st.button("Forward",on_click=forward())