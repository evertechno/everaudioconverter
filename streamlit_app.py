import streamlit as st
import ffmpeg
import io

def convert_mp4_to_wav(mp4_file):
    # Convert .mp4 (audio or video) file to .wav using ffmpeg
    output = io.BytesIO()
    ffmpeg.input(mp4_file).output(output, format='wav').run()
    output.seek(0)
    return output

# Streamlit app
st.title("MP4 and MP4A to WAV Audio Converter")

# File uploader for MP4 or MP4A files
uploaded_file = st.file_uploader("Upload an MP4 or MP4A audio file", type=["mp4", "mp4a"])

# Check if a file is uploaded
if uploaded_file is not None:
    st.write(f"File uploaded: {uploaded_file.name}")
    
    # Convert the .mp4 or .mp4a file to .wav
    st.write("Converting your file to WAV...")
    wav_file = convert_mp4_to_wav(uploaded_file)

    # Provide download link for the converted WAV file
    st.write("Conversion successful! You can download your WAV file below:")
    st.download_button("Download WAV", wav_file, file_name="converted_audio.wav", mime="audio/wav")
else:
    st.write("Please upload an MP4 or MP4A file to convert.")
