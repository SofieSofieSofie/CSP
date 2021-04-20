# import required modules
from os import path
from pydub import AudioSegment

# assign files
input_file = "transcribe/episodesMP3/cth499.mp3"
output_file = "transcribe/episodesWav/cth499.wav"
  
# convert mp3 file to wav file
sound = AudioSegment.from_mp3(input_file)
sound.export(output_file, format="wav")