import streamlit as st
import openai

with st.form("my_form"):
    uploaded_file = st.file_uploader("Choose an audio file")
    st.markdown(
        """File uploads are currently limited to 25 MB and the following input file types are supported: `mp3`, `mp4`, `mpeg`, `mpga`, `m4a`, `wav`, and `webm`."""
    )
    on_submit = st.form_submit_button("변환")
    if on_submit:
        with st.spinner("변환중입니다"):
            transcript = openai.Audio.transcribe("whisper-1", uploaded_file)
        st.write("## 변환된 텍스트")
        st.write(transcript)
