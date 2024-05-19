from elevenlabs.client import ElevenLabs
from elevenlabs import play

ELEVENLABS_API_KEY = '1aa08c1ac49c3c9566c1d93156ab7fc9'
test_text = 'Yeah hello guys!'


client = ElevenLabs(
    api_key = ELEVENLABS_API_KEY
)

audio = client.generate(
    text = test_text, 
    voice = 'pNInz6obpgDQGcFmaJgB'
)

play(audio)