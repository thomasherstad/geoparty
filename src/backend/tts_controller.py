from elevenlabs.client import ElevenLabs
from elevenlabs import play

ELEVENLABS_API_KEY = '1aa08c1ac49c3c9566c1d93156ab7fc9'

client = ElevenLabs(
    api_key = ELEVENLABS_API_KEY
)

standard = 'pNInz6obpgDQGcFmaJgB'
john = 'sLjXPEgayrhC8RIDHCcV'


def play_audio(message):
    audio = client.generate(
    text = message, 
    voice = john
    )
    play(audio)

if __name__ == '__main__':
    test_text = 'Hello guys!'
    play_audio(test_text)