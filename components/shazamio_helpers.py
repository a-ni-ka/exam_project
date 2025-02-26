import asyncio
from shazamio import Shazam, Serialize


def process_sound(audio_input):
    # wrapping the async function in another function that executes it with asyncio.run
    async def _process():
        shazam = Shazam()
        # awaits the shazamio function recognize()
        match_results = await shazam.recognize(audio_input)
        if len(match_results["matches"]) == 0:
            # if there's no results, we return None - otherwise, we continue with the function
            return None
        # awaits the shazamio function track_about() to get some data for the results
        about_track = await shazam.track_about(track_id=match_results["matches"][0]["id"])
        # serializing in shazamio helps display the data in a nicer and simpler way
        serialize = Serialize.track(data=about_track)
        # we add only the data we need into our song_data dictionary
        song_data = {
            "title": serialize.title,
            "artist": serialize.subtitle,
            "album_cover": serialize.sections[0].meta_pages[1].image,
            "preview": serialize.ringtone
        }
        return song_data
    return asyncio.run(_process())


def search_songs(text_input):
    # wrapping the async function in another function that executes it with asyncio.run
    async def _search():
        shazam = Shazam()
        # we return the results of the shazamio function search_track, limited to 7 results
        return await shazam.search_track(query=text_input, limit=7)

    result = asyncio.run(_search())
    if result == {}:
        # if there's no result, the function returns None
        return None
    song_list = []
    for element in result["tracks"]["hits"]:
        # we add the resulting song data dictionaries to a list and return this list
        song_list.append({
            "title": element["heading"]["title"],
            "artist": element["heading"]["subtitle"],
            "album_cover": element["images"]["default"],
            "preview": element["stores"]["apple"]["previewurl"]
        })
    return song_list
