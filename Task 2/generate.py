import pickle
import random
from pathlib import Path

import numpy as np
from music21 import note, chord, stream
from tensorflow.keras.models import load_model


# Load the trained model
model = load_model("music_model.keras")

# Load the original notes
with open("notes.pkl", "rb") as file:
    notes = pickle.load(file)

# Create a mapping of notes to numbers
pitchnames = sorted(set(notes))
note_to_int = {name: number for number, name in enumerate(pitchnames)}
int_to_note = {number: name for name, number in note_to_int.items()}

# Sequence length used during training
sequence_length = 50

# Pick a random starting point
start = random.randint(0, len(notes) - sequence_length - 1)

pattern = notes[start:start + sequence_length]

prediction_output = []

print("Generating music...")

# Generate 200 new notes
for _ in range(200):

    prediction_input = np.array(
        [[note_to_int[char] for char in pattern]]
    )

    prediction_input = prediction_input.reshape(
        1, sequence_length, 1
    )

    prediction_input = prediction_input / float(len(pitchnames))

    prediction = model.predict(
        prediction_input,
        verbose=0
    )

    index = np.argmax(prediction)

    result = int_to_note[index]

    prediction_output.append(result)

    pattern.append(result)
    pattern = pattern[1:]


# Create a MIDI file
output_folder = Path("generated_music")
output_folder.mkdir(exist_ok=True)

midi_stream = stream.Stream()

for pattern in prediction_output:

    if "." in pattern:
        notes_in_chord = pattern.split(".")

        chord_notes = []

        for current_note in notes_in_chord:
            chord_notes.append(
                note.Note(int(current_note))
            )

        new_chord = chord.Chord(chord_notes)
        midi_stream.append(new_chord)

    else:
        midi_stream.append(note.Note(pattern))


# Save the generated music
output_file = output_folder / "generated_song.mid"

midi_stream.write(
    "midi",
    fp=str(output_file)
)

print("\nMusic generation complete!")
print(f"Saved to: {output_file}")