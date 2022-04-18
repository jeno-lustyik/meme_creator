import cv2 as cv
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image

st.title('Meme creator v0.1')

img = st.file_uploader('Upload your image here:')

if img is not None:
    img = Image.open(img)
    img.save('img.jpg')
    img = cv.imread('img.jpg')
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img_grey = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    meme_copy = img.copy()

    font = cv.FONT_HERSHEY_SIMPLEX
    text1 = st.text_input('Upper text')
    text2 = st.text_input('Bottom text')

    if len(text1) > 0 and len(text2) >0:
        textsize1 = cv.getTextSize(text1, font, 2, 2)
        textsize2 = cv.getTextSize(text2, font, 2, 2)

        textX1 = int((img_grey.shape[1] - textsize1[0][0]) / 2)
        textY1 = int(img.shape[0] - (img.shape[0] - 2 * textsize1[1]))

        textX2 = int((img_grey.shape[1] - textsize2[0][0]) / 2)
        textY2 = int((img.shape[0] - textsize2[1]))

        cv.putText(meme_copy, text1, (textX1, textY1), font, 2, (0, 0, 0), 3)

        cv.putText(meme_copy, text2, (textX2, textY2), font, 2, (0, 0, 0), 3)

        cv.imshow('meme', meme_copy)
        cv.waitKey(0)
        cv.destroyAllWindows()
        cv.waitKey(1)

# plt.figure(figsize=(10, 8))
# plt.imshow(meme_copy)
# plt.show()
