import streamlit as st
from PIL import Image

st.title('カモノスアプリだよ')
st.caption('これはテストアプリです')

#　画像
image = Image.open('./data/download.png')							#	image = Image.open('download.png')   だとエラー吐いた。相対パスを指定してあげれたから？
st.image(image, width=200)
