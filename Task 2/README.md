# Task 2 - AI Music Generation

## Project Overview

This project uses a Long Short-Term Memory (LSTM) neural network to generate original music sequences from MIDI data.

## Technologies Used

- Python
- TensorFlow / Keras
- Music21
- NumPy
- Streamlit
- FluidSynth
- MIDI

## Features

- MIDI dataset processing
- LSTM model training
- AI-generated music
- MIDI file generation
- MIDI to WAV audio conversion
- Streamlit web interface
- Generated music playback and download

## How It Works

1. MIDI files are collected and processed.
2. Musical notes are converted into numerical sequences.
3. An LSTM neural network is trained on the sequences.
4. The trained model generates new musical sequences.
5. The generated MIDI is converted into WAV audio using FluidSynth.
6. The Streamlit application allows the user to generate and play the music.

## Output

The application generates:

- `generated_song.mid`
- `generated_song.wav`

## Author

CodeAlpha Internship Project
