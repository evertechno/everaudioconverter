import streamlit as st
import ffmpeg
import io

def convert_m4a_to_wav(m4a_file):
    # Create an in-memory buffer to store the converted WAV data
    output = io.BytesIO()
    
    try:
        # Run ffmpeg, passing the uploaded file as input and saving the output to an in-memory buffer
        ffmpeg.input('pipe:0').output('pipe:1', format='wav').run(input=m4a_file.read(), capture_stdout=True, capture_stderr=True)
        
        # We need to run this in a different way, so let's try using 'capture_stdout'
        output.seek(0)
    except Exception as e:
        st.error(f"Error during conversion: {e}")
        return None
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

    if wav_file:
        # Provide download link for the converted WAV file
        st.write("Conversion successful! You can download your WAV file below:")
        st.download_button("Download WAV", wav_file, file_name="converted_audio.wav", mime="audio/wav")
else:
    st.write("Please upload an M4A file to convert.")
