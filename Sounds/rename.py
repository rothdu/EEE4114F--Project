import os

# Create arrays of ground truth data

sound_types = ["Snare", "Trumpet", "Violin"]

data = []

for sound_type in sound_types:

    # establish output directories
    # TODO: Add checks that directorties exist
    sound_dir = os.fsencode("../Sounds/" + sound_type)
    
    # remove all existing spectrograms
    for i, spec_file in  enumerate(os.listdir(sound_dir)):
        
        filename = os.fsdecode(spec_file)
        
        if filename.endswith(".wav") or filename.endswith(".mp3") or filename.endwith(".flac"):
            extension = os.path.splittext(filename)[1]
            os.rename(spec_file, os.join(spec_file, os.fsencode(sound_type + "_" + str(i).zfill(3) + extension)))
            