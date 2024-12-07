import streamlit as st
from pydub import AudioSegment
import io

def convert_mp4a_to_wav(mp4a_file):
    # Convert .mp4a file to .wav using pydub
    audio = AudioSegment.from_file(mp4a_file, format="mp4a")
    wav_file = io.BytesIO()
    audio.export(wav_file, format="wav")
    wav_file.seek(0)
    return wav_file

# Streamlit app
st.title("MP4A to WAV Audio Converter")

uploaded_file = st.file_uploader("Upload an MP4A audio file", type=["mp4a", "mp3", "wav"])

if uploaded_file is not None:
    # Convert .mp4a file to .wav
    if uploaded_file.type == "audio/mp4a":
        st.write("Converting your MP4A file to WAV...")
        wav_file = convert_mp4a_to_wav(uploaded_file)

        # Provide download link for the converted WAV file
        st.write("Conversion successful! You can download your WAV file below:")
        st.download_button("Download WAV", wav_file, file_name="converted_audio.wav", mime="audio/wav")
    else:
        st.error("Please upload a valid MP4A audio file.")
