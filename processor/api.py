import os
import openai
import whisper
import soundfile as sf
import numpy as np

from dotenv import load_dotenv
from pydub import AudioSegment
from io import BytesIO

def process_blob(blob_file):
    # Save blob file to server
    if blob_file:
        blob_filename = blob_file.filename
        blob_filepath = os.path.join("uploads", blob_filename)
        blob_file.save(blob_filepath)
        print("File saved:", blob_filepath)

    if blob_filepath.endswith('.m4a'):
        audio = AudioSegment.from_file(blob_filepath, format="m4a")
        wav_filepath = blob_filepath.replace('.m4a', '.wav')
        audio.export(wav_filepath, format="wav")
        blob_filepath = wav_filepath
    
    transcript = _get_resonpse_from_whisper(blob_filepath)
    print(transcript['text'])

    response_data = {
        'message': 'Blob processed',
        'processed_string': transcript['text']
    }
    return response_data

def process_string(prompt):

    answer = _get_resonpse_from_gpt(prompt)
    response_data = {
        'message': 'String processed',
        'processed_string': answer
    }

    return response_data

def _get_resonpse_from_gpt(message):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    gpt_answer = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message},
        ]
    )
    return gpt_answer

def _get_resonpse_from_whisper(audio_file):
    model = whisper.load_model("base")
    transcript = model.transcribe(audio_file)
    return transcript