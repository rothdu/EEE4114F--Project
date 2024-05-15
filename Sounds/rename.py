import os

# Create arrays of ground truth data

sound_types = ["Piano"]

data = []

for sound_type in sound_types:

    # establish output directories
    # TODO: Add checks that directorties exist
    sound_dir = os.fsencode(sound_type)
    
    # remove all existing spectrograms
    for i, spec_file in  enumerate(os.listdir(sound_dir)):
        
        filename = os.fsdecode(spec_file)
        
        if filename.endswith(".wav") or filename.endswith(".mp3") or filename.endswith(".flac"):
            extension = os.path.splitext(filename)[1]

            temprename = filename + ".temprename"
            os.rename(os.path.join(sound_dir, os.fsencode(filename)), os.path.join(sound_dir, os.fsencode(temprename)))
            
    
    for i, spec_file in  enumerate(os.listdir(sound_dir)):
        
        temprename = os.fsdecode(spec_file)
        if temprename.endswith(".temprename"):
            
            filename = os.path.splitext(temprename)[0]

            if filename.endswith(".wav") or filename.endswith(".mp3") or filename.endswith(".flac"):
                extension = os.path.splitext(filename)[1]
                os.rename(os.path.join(sound_dir, os.fsencode(temprename)), os.path.join(sound_dir, os.fsencode(sound_type + "_" + str(i).zfill(3) + extension)))
                
    
        
            