import streamlit as st
import ffmpeg
import io

def convert_m4a_to_wav(m4a_file):
    # Convert .m4a file to .wav using ffmpeg
    output = io.BytesIO()
    ffmpeg.input(m4a_file).output(output, format='wav').run()
    output.seek(0)
    return output

# Streamlit app
st.title("M4A to WAV Audio Converter")

# File uploader for M4A files
uploaded_file = st.file_uploader("Upload an M4A audio file", type=["m4a"])

# Check if a file is uploaded
if uploaded_file is not None:
    st.write(f"File uploaded: {uploaded_file.name}")
    
    # Convert the .m4a file to .wav
    st.write("Converting your M4A file to WAV...")
    wav_file = convert_m4a_to_wav(uploaded_file)

    # Provide download link for the converted WAV file
    st.write("Conversion successful! You can download your WAV file below:")
    st.download_button("Download WAV", wav_file, file_name="converted_audio.wav", mime="audio/wav")
else:
    st.write("Please upload an M4A file to convert.")
