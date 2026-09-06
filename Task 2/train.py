from pathlib import Path
import pickle

import numpy as np
from music21 import converter, instrument, note, chord
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.utils import to_categorical


# -----------------------------
# 1. Read MIDI files
# -----------------------------
notes = []

midi_files = list(Path("data").glob("*.mid")) + list(Path("data").glob("*.midi"))

print(f"Found {len(midi_files)} MIDI files.")

for file in midi_files:
    print(f"Processing: {file.name}")

    midi = converter.parse(file)

    notes_to_parse = None

    try:
        notes_to_parse = instrument.partitionByInstrument(midi)
        if notes_to_parse:
            notes_to_parse = notes_to_parse.parts[0].recurse()
        else:
            notes_to_parse = midi.flat.notes
    except Exception:
        notes_to_parse = midi.flat.notes

    for element in notes_to_parse:
        if isinstance(element, note.Note):
            notes.append(str(element.pitch))

        elif isinstance(element, chord.Chord):
            notes.append(".".join(str(n) for n in element.normalOrder))


print(f"\nTotal musical notes/chords collected: {len(notes)}")


# -----------------------------
# 2. Prepare sequences
# -----------------------------
pitchnames = sorted(set(notes))
n_vocab = len(pitchnames)

note_to_int = {note_name: number for number, note_name in enumerate(pitchnames)}

sequence_length = 50

network_input = []
network_output = []

for i in range(len(notes) - sequence_length):
    sequence_in = notes[i:i + sequence_length]
    sequence_out = notes[i + sequence_length]

    network_input.append(
        [note_to_int[char] for char in sequence_in]
    )

    network_output.append(note_to_int[sequence_out])


n_patterns = len(network_input)

network_input = np.reshape(
    network_input,
    (n_patterns, sequence_length, 1)
)

network_input = network_input / float(n_vocab)

network_output = to_categorical(
    network_output,
    num_classes=n_vocab
)


print(f"Vocabulary size: {n_vocab}")
print(f"Training sequences: {n_patterns}")


# -----------------------------
# 3. Build LSTM model
# -----------------------------
model = Sequential()

model.add(
    LSTM(
        256,
        input_shape=(sequence_length, 1),
        return_sequences=True
    )
)

model.add(Dropout(0.3))

model.add(
    LSTM(256)
)

model.add(Dropout(0.3))

model.add(Dense(n_vocab, activation="softmax"))

model.compile(
    loss="categorical_crossentropy",
    optimizer="adam"
)


model.summary()


# -----------------------------
# 4. Train the model
# -----------------------------
print("\nStarting training...")

model.fit(
    network_input,
    network_output,
    epochs=30,
    batch_size=64
)


# -----------------------------
# 5. Save model + notes
# -----------------------------
model.save("music_model.keras")

with open("notes.pkl", "wb") as file:
    pickle.dump(notes, file)

print("\nTraining complete!")
print("Model saved as music_model.keras")
print("Notes saved as notes.pkl")