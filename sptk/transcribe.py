import sys
# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
from pathlib import Path


def main(path_to_file: str, do_translate: bool = False):
    audio_file = open(path_to_file, "rb")
    if do_translate:
        transcript = translate(audio_file)
    else:
        transcript = transcribe(audio_file)
    print(transcript)


import openai
import os


def transcribe(file_path: str, model_name: str = "whisper-1") -> str:
    """
    Transcribe the given audio file using OpenAI's Whisper ASR model.

    :param file_path: Path to the audio file to be transcribed.
    :param model_name: Path to the audio file to be transcribed.
    :return: Transcribed text.
    """
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set in the environment variables.")

    openai.api_key = api_key

    print(f"Calling transcribe API with model='{model_name}'")

    try:
        response = openai.Completion.create(
            model=model_name,   # "whisper-large"
            prompt=file_path,
            temperature=0,
            max_tokens=3000
        )
        return response.choices[0].text.strip()
    except Exception as e:
        raise RuntimeError(f"Error occurred while transcribing the audio: {str(e)}")


def translate(file):
    print(f"Calling 'openai.Audio.translate'")
    return openai.Audio.translate("whisper-1", file)


if __name__ == "__main__":
    if len(sys.argv[1:]) == 0:
        print("Missing required argument: audio filename (Exiting)")
    else:
        filename = sys.argv[1]
        translation = bool(sys.argv[2]) if len(sys.argv[1:]) == 2 else False
        print(f"Starting: audio filename = '{filename}', translation = {translation}\n")
        main(filename, translation)
        print("\nDone")
