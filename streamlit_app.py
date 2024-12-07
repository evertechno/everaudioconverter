import streamlit as st
import ffmpeg
import io

def convert_mp4a_to_wav(mp4a_file):
    # Convert .mp4a file to .wav using ffmpeg
    output = io.BytesIO()
    ffmpeg.input(mp4a_file).output(output, format='wav').run()
    output.seek(0)
    return output

# Streamlit app
st.title("MP4A to WAV Audio Converter")

# File uploader for MP4A files
uploaded_file = st.file_uploader("Upload an MP4A audio file", type=["mp4a"])

# Check if a file is uploaded
if uploaded_file is not None:
    st.write(f"File uploaded: {uploaded_file.name}")
    
    # Convert the .mp4a file to .wav
    st.write("Converting your MP4A file to WAV...")
    wav_file = convert_mp4a_to_wav(uploaded_file)

    # Provide download link for the converted WAV file
    st.write("Conversion successful! You can download your WAV file below:")
    st.download_button("Download WAV", wav_file, file_name="converted_audio.wav", mime="audio/wav")
else:
    st.write("Please upload an MP4A file to convert.")
