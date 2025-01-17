import asyncio
from shazamio import Shazam
from shazamio import Serialize


# async def process_sound(audio_input):
#     shazam = Shazam()
#     out = await shazam.recognize_song(audio_input)
#     result = Serialize.full_track(data=out)
#     youtube_data = await shazam.get_youtube_data(link=result.track.youtube_link)
#     serialized_youtube = Serialize.youtube(data=youtube_data)
#     return serialized_youtube.uri

text = "mestre barrao"

import json

async def search_songs():
    text_input = "hello"
    shazam = Shazam()
    tracks = await shazam.search_track(query=text_input, limit=5)
    print(json.dumps(tracks, indent=4))


asyncio.run(search_songs())
