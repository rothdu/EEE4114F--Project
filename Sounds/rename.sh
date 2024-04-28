n=1; 
for f in *.wav; 
do mv "$f" "$(printf "$1_%03i.wav" "$n")"; 
((n++)); 
done

for f in *.aiff; 
do mv "$f" "$(printf "$1_%03i.aiff" "$n")"; 
((n++)); 
done

for f in *.mp3; 
do mv "$f" "$(printf "$1_%03i.mp3" "$n")"; 
((n++)); 
done

for f in *.flac; 
do mv "$f" "$(printf "$1_%03i.flac" "$n")"; 
((n++)); 
done
