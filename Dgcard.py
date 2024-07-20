import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import qrcode

def create_digital_card(biodata, image_path):
    card_width = 681
    card_height = 599
    background_color = ('#B2A4D4')
    card = Image.new('RGB', (card_width, card_height), background_color)
    
    draw = ImageDraw.Draw(card)
    
    try:
        font = ImageFont.truetype("arial.ttf", size=20)
    except IOError:
        font = ImageFont.load_default()
    
    user_img = Image.open(image_path)
    user_img = user_img.resize((150, 150))
    
    x_start = 50
    y_start = 50
    line_height = 30
    
    for i, (key, value) in enumerate(biodata.items()):
        text = f"{key}: {value}"
        draw.text((x_start, y_start + i * line_height), text, font=font, fill=(0, 0, 0))
    
    img_position = (card_width - 200, 50)
    card.paste(user_img, img_position)
    
    qr_data = "\n".join([f"{key}: {value}" for key, value in biodata.items()])
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=8,  
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    
    qr_img = qr.make_image(fill='black', back_color='white')
    qr_img = qr_img.resize((120, 120))  
    
    qr_position = (card_width - 200, card_height - 200)
    card.paste(qr_img, qr_position)
    
    card_filename = "digital_card_with_image_and_qr.png"
    card.save(card_filename)
    return card_filename

st.title("Digital Card Generator")

name = st.text_input("Enter your name:")
age = st.text_input("Enter your age:")
gender = st.selectbox("Select your gender:", ["Male", "Female", "Other"])
occupation = st.text_input("Enter your occupation:")
email = st.text_input("Enter your email:")
phone = st.text_input("Enter your phone number:")
address = st.text_input("Enter your address:")
linkedin_id = st.text_input("Enter your LinkedIn ID (optional):")
github_repo = st.text_input("Enter your GitHub Repo (optional):")
instagram_id = st.text_input("Enter your Instagram ID (optional):")
facebook_id = st.text_input("Enter your Facebook ID (optional):")
uploaded_image = st.file_uploader("Upload your image", type=['png', 'jpg', 'jpeg'])

if st.button("Generate Digital Card"):
    if not all([name, age, gender, occupation, email, phone, address, uploaded_image]):
        st.error("Please fill in all required fields and upload an image.")
    else:
        biodata = {
            "Name": name,
            "Age": age,
            "Gender": gender,
            "Occupation": occupation,
            "Email": email,
            "Phone": phone,
            "Address": address,
        }
        
        if instagram_id:
            biodata["Instagram ID"] = instagram_id
        if facebook_id:
            biodata["Facebook ID"] = facebook_id
        if linkedin_id:
            biodata["LinkedIn ID"] = linkedin_id
        if github_repo:
            biodata["GitHub Repo"] = github_repo

        with open("uploaded_image.png", "wb") as f:
            f.write(uploaded_image.getbuffer())
        
        card_filename = create_digital_card(biodata, "uploaded_image.png")
        
        st.image(card_filename, caption="Your Digital Card")
        with open(card_filename, "rb") as f:
            st.download_button("Download Digital Card", f, file_name="digital_card_with_image_and_qr.png")
