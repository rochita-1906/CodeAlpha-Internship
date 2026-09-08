from music21 import corpus
from pathlib import Path

data_folder = Path("data")
data_folder.mkdir(exist_ok=True)

# Get Bach pieces from music21
bach_files = corpus.getComposer("bach")

# Remove old files
for file in data_folder.iterdir():
    if file.is_file():
        file.unlink()

count = 0

for source in bach_files:
    if count >= 20:
        break

    try:
        # Parse the Bach piece
        score = corpus.parse(source)

        # Convert the piece to MIDI
        midi_path = data_folder / f"bach_{count + 1}.mid"
        score.write("midi", fp=str(midi_path))

        count += 1
        print(f"Created: {midi_path}")

    except Exception as e:
        print(f"Skipped {source}: {e}")

print(f"\nSuccessfully created {count} MIDI files.")