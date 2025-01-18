import asyncio
from shazamio import Shazam, Serialize


def process_sound(audio_input):
    async def _process():
        shazam = Shazam()
        match_results = await shazam.recognize(audio_input)
        if len(match_results["matches"]) == 0:
            return None
        about_track = await shazam.track_about(track_id=match_results["matches"][0]["id"])
        serialize = Serialize.track(data=about_track)
        song_data = {
            "title": serialize.title,
            "artist": serialize.subtitle,
            "album_cover": serialize.sections[0].meta_pages[1].image
        }
        return song_data
    return asyncio.run(_process())


def find_top_tracks():
    async def _top_tracks():
        shazam = Shazam()
        return await shazam.top_world_genre_tracks(genre="capoeira", limit=5)

    result = asyncio.run(_top_tracks())

    for track in result['tracks']:
        serialized_track = Serialize.track(data=track)
        print(serialized_track.spotify_url)


def search_songs(text_input):
    async def _search():
        shazam = Shazam()
        return await shazam.search_track(query=text_input, limit=7)

    result = asyncio.run(_search())
    song_list = []
    for element in result["tracks"]["hits"]:
        song_list.append({
            "title": element["heading"]["title"],
            "artist": element["heading"]["subtitle"],
            "album_cover": element["images"]["default"]
        })

    return song_list
