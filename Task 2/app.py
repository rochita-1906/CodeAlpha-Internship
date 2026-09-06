import streamlit as st
import subprocess
import sys
from pathlib import Path

st.set_page_config(
    page_title="AI Music Generator",
    page_icon="🎵",
    layout="centered"
)

st.title("🎵 AI Music Generator")
st.write(
    "Generate an original MIDI music sequence using a trained LSTM neural network."
)

st.divider()

if st.button("🎹 Generate New Music", use_container_width=True):

    with st.spinner("AI is composing your music..."):

        result = subprocess.run(
            [sys.executable, "generate.py"],
            capture_output=True,
            text=True
        )

    if result.returncode == 0:

        st.success("Music generated successfully! 🎉")

        midi_file = Path("generated_music/generated_song.mid")
        audio_file = Path("generated_music/generated_song.wav")

        # Convert MIDI to WAV
        subprocess.run([
            "fluidsynth",
            "-ni",
            ".\\GeneralUser-GS.sf2",
            str(midi_file),
            "-F",
            str(audio_file),
            "-r",
            "44100"
        ])

        # Play generated audio
        if audio_file.exists():

            st.audio(
                str(audio_file),
                format="audio/wav"
            )

            with open(midi_file, "rb") as file:
                st.download_button(
                    "⬇️ Download Generated MIDI",
                    data=file,
                    file_name="generated_song.mid",
                    mime="audio/midi"
                )

    else:

        st.error("Something went wrong while generating the music.")
        st.code(result.stderr)

st.divider()

st.caption("AI Internship Project | CodeAlpha")