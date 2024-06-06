# Plays random song in a specified folder

# Windows
import random, os
music_dir = 'E:\\musicfolder'
songs = os.listdir(music_dir)

song = random.randint(0,len(songs)-1)  # subtract 1 because list indices start at 0

# Prints The Song Name
print(songs[song])  

os.startfile(os.path.join(music_dir, songs[song]))  # play the random song

# Linux
import os
import random
import subprocess

music_dir = '/musicdirectory'
songs = os.listdir(music_dir)

song = random.choice(songs)
song_path = os.path.join(music_dir, song)

print(f'Playing: {song}')

# Use a music player command to play the song
# Replace 'vlc' with your preferred music player command
subprocess.call(['vlc', song_path])