import streamlit as st

st.title("Digitale Visitenkarte")
st.write(" ")
st.divider()
st.write(" ")
#visitenkarten felder
name = st.text_input("Name", value= "")
position = st.text_input("Position", value= "")
straße = st.text_input("Straße", value= "")
postleitzahl = st.text_input("Postleitzahl", value= "")
email = st.text_input("E-Mail", value = "")
handynummer = st.text_input("Handynummer", value = "")
st.write(" ")
st.divider()
st.write(" ")
st.subheader("Wähle deine gewünschte Hintergrundfarbe:")
color = st.color_picker("Deine Hintergrundfarbe")
st.divider()
st.write(" ")
st.subheader("Eigener Hintergrund")
uploaded_files = st.file_uploader("Dein Hintergrund", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)
st.divider()
st.write(" ")
with st.popover("Deine Visitenkarte"):
    st.text("{name}\n{position}\n{straße}\n{postleitzahl}\n{email}\n{handynummer}\n".format(name= name, position= position, straße= straße, postleitzahl= postleitzahl, email= email, handynummer= handynummer))
st.write(" ")
st.divider()
st.subheader("Downloade deine Visitenkarte:")
st.write(" ")
if st.button("Download"):
    st.write("Das downloaden von Visitenkarten ist derzeit nicht verfügbar...")
st.write(" ")
st.divider()
st.write(" ")
geheimnis = st.checkbox(" ")

if geheimnis:
    st.balloons()

