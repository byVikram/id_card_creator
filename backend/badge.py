from PIL import Image, ImageDraw, ImageFont
def print_badge(name,id,contact):
# Create a blank ID card template
    width, height = 400, 500
    background_color = (255, 255, 255)
    id_card = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(id_card)
    font = ImageFont.truetype("arial.ttf", 20)

    # Add ID card information
    parent_path_qr = "D:\\qrreg\\backend\\qrphotos\\"


    qr_name=str(id+".png")
    path=parent_path_qr+qr_name
    print(type(path),"type of Path")
    print(path)

    photo = Image.open(path)  # Replace with the path to the photo


    pr_name=str(id+"pic"+".png")
    print(pr_name,"from badge.py")

    parentpath_profile_pic="D:\\qrreg\\backend\\profilephotos\\"

    pr_path=parentpath_profile_pic+pr_name
    print(type(pr_name))
    id_number = id

    pr_pic=Image.open(pr_path)
    card_name = name
    contact_number = contact

    photo = photo.resize((150, 150))
    pr_pic = pr_pic.resize((150, 150))

    id_card.paste(pr_pic, (125, 20))
    id_card.paste(photo, (125, 345))

    draw.text((30, 200), "ID Number", fill=(0, 0, 0), font=font)
    draw.text((140, 200), ":", fill=(0, 0, 0), font=font)
    draw.text((150, 200),id_number, fill=(0, 0, 0), font=font)

    draw.text((30, 240), "card_name", fill=(0, 0, 0), font=font)
    draw.text((140, 240), ":", fill=(0, 0, 0), font=font)
    draw.text((150, 240), card_name, fill=(0, 0, 0), font=font)

    draw.text((30, 280), "Contact", fill=(0, 0, 0), font=font)
    draw.text((140, 280), ":", fill=(0, 0, 0), font=font)
    draw.text((150, 280), contact_number, fill=(0, 0, 0), font=font)



    # Paste the photo on the ID card
    photo = photo.resize((100, 100))  # Resize the photo to fit
    id_card.paste(photo, (400, 20))

    # Save the ID card
    lastname=str(id+"last"+".png")

    last_parent="D:\\qrreg\\backend\\final\\"
    final_path = last_parent+lastname

    id_card.save(final_path)

    # Display the ID card (optional)
    id_card.show()




