import streamlit as st
from PIL import Image, ImageFilter, ImageEnhance
import io

st.title('Tentang Kami✨')
st.write(""" Haiii! Kami adalah tim Uhuyy dari Universitas Yarsi.""")

st.write (""" Kami, mahasiswa semester 5 Jurusan Teknik Informatika, tengah fokus dalam peminatan yang sedang tren, yaitu Artificial Intelligence (AI). Pilihan kami pada AI didasari keyakinan bahwa teknologi ini akan membawa perubahan besar, dan kami memiliki niatan kuat untuk turut berkontribusi.
""")

st.write("""
Dalam tim, kami memiliki anggota yang gemar coding, ahli dalam mengatur model, dan tentu saja yang mampu membuat AI menjadi keren. Jika ditanya, "Ada yang bisa ngoding sambil ngopi?" Jawabannya pasti, "Bisa banget!" meskipun kadang sambil menghadapi tantangan, hehe.
""")

st.write("""
Semangat dan kegigihan kami mengemban perjalanan di dunia AI terus membawa kami untuk lebih memahami dan mengembangkan teknologi ini. Kami yakin, dengan kolaborasi dan dedikasi, proyek-proyek inovatif dari tim Uhuyy akan menjadi kontribusi berarti dalam merintis masa depan yang penuh potensi.
""")

st.write("""
Terima kasih telah menjadi bagian dari perjalanan kami, dan nantikan keberlanjutan kisah kami dalam proyek-proyek mendatang! 🌟🤖
""")


def enhance_image(image_data):
    image = Image.open(io.BytesIO(image_data))

    enhanced_image = image.filter(ImageFilter.SHARPEN)

    border_size = 2
    border_color = "black"
    img_with_border = Image.new(
        "RGB",
        (enhanced_image.width + border_size * 2, enhanced_image.height + border_size * 2),
        border_color,
    )
    img_with_border.paste(enhanced_image, (border_size, border_size))

    with io.BytesIO() as output:
        img_with_border.save(output, format="JPEG")
        return output.getvalue()


col1, col2, col3 = st.columns(3)

with col1:
    st.image(enhance_image(open("img_sources/3.png", "rb").read()), caption="Kafah Al Farizi", width=200)

with col2:
    st.image(enhance_image(open("img_sources/2.png", "rb").read()), caption="Mohammad Zaki", width=200)

with col3:
    st.image(enhance_image(open("img_sources/1.png", "rb").read()), caption="Enggar Galih W", width=200)

st.divider()     
st.write("""
Copyright © 2023 - Uhuyy, All Rights Reserved.
""")
