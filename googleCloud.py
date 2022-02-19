import os
from google.cloud import speech
import io
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\adeDd\\Downloads\\ideate-341719-20a224022406.json"
client = speech.SpeechClient()
def sample_recognize(speech_file, accent):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\adeDd\\Downloads\\ideate-341719-20a224022406.json"
    client = speech.SpeechClient()
    with open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    """
     Note that transcription is limited to a 60 seconds audio file.
     Use a GCS file for audio longer than 1 minute.
    """
    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code=accent,
        audio_channel_count=2
    )

    x =''
    try:
        operation = client.long_running_recognize(config=config, audio=audio)
    except:
        config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code=accent,
        audio_channel_count=1
    )
        operation = client.long_running_recognize(config=config, audio=audio)
    response = operation.result(timeout=90)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        x += result.alternatives[0].transcript + "\n" + str(result.alternatives[0].confidence)
    return x
        #print("Confidence: {}".format(result.alternatives[0].confidence))




"""
Print confidence level for individual words in a transcription of a short audio
file.
Args:
    local_file_path Path to local audio file, e.g. /path/audio.wav
"""
"""
# local_file_path = 'resources/brooklyn_bridge.flac'

# When enabled, the first result returned by the API will include a list
# of words and the confidence level for each of those words.
enable_word_confidence = True

# The language of the supplied audio
# language_code = "es-ES"
language_code= "en-IN"
config = {
    "enable_word_confidence": enable_word_confidence,
    "language_code": language_code,
    "audio_channel_count": 1,
}
# print(type(input_audio))
# song = AudioSegment.from_file(io.BytesIO(input_audio), format="wav")
# song.export("tmp.wav", format="wav")
# with io.open("tmp.wav", "rb") as f:
#     content = f.read()
# # print(type(song))
# audio = {"content": content}

audio = {"content": input_audio}

response = client.recognize(config, audio)
print("response", response)
# print("response", response)
# The first result includes confidence levels per word
# print("result", response.results)

# First alternative is the most probable result
try:
    result = response.results[0]
except IndexError:
    # No matches found
    return "FAILED", 0
alternative = result.alternatives[0]
# print(u"Transcript: {}".format(alternative.transcript))
# # Print the confidence level of each word
for word in alternative.words:
    return word.word, word.confidence
    # if word.confidence > .4:
    #     return word.word
return "FAILED", 0
    # print("word", word.word)
    # print("Confidence", word.confidence)
    # print(u"Word: {}".format(word.word))
    # print(u"Confidence: {}".format(word.confidence))
    """
