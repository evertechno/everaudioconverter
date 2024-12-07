import streamlit as st
import audioread
import numpy as np
import wave
import io

def convert_m4a_to_wav(m4a_file):
    try:
        # Initialize a memory buffer for the WAV file output
        output = io.BytesIO()

        # Read the uploaded file into memory as a bytes stream
        with io.BytesIO(m4a_file.read()) as audio_data:
            # Use audioread to open the in-memory .m4a file
            with audioread.audio_open(audio_data) as audio_file:
                # Read the data into numpy array
                samples = np.frombuffer(audio_file.read_data(), dtype=np.int16)

                # Write to a WAV format
                with wave.open(output, 'wb') as wav_file:
                    wav_file.setnchannels(1)  # Mono
                    wav_file.setsampwidth(2)  # 2 bytes per sample (16-bit)
                    wav_file.setframerate(audio_file.samplerate)  # Audio sample rate
                    wav_file.writeframes(samples.tobytes())

        output.seek(0)
        return output
    except Exception as e:
        st.error(f"Error during conversion: {e}")
        return None

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
