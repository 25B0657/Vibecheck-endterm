from dotenv import load_dotenv
import os
import pylast

load_dotenv()

def get_lastfm_client():

    network = pylast.LastFMNetwork(
        api_key=os.getenv("LASTFM_API_KEY"),
        api_secret=os.getenv("LASTFM_API_SECRET")
    )

    # print("Last.fm connected successfully")

    return network



def fetch_tracks(mood, limit=5):

    network = get_lastfm_client()
    tag = network.get_tag(mood)
    top_tracks = tag.get_top_tracks(limit=limit)
    results = []

    for item in top_tracks:
        track = item.item

# TO DO {
        # fetch cover image safely
        try:
            album = track.get_album()

            if album:
                cover_image = album.get_cover_image()
            else:
                cover_image = None  #none if the image is unavailable

        except:
            cover_image = None

        # build dictionary
        track_info = {
            "song": track.get_name(),
            "artist": track.get_artist().get_name(),
            "cover_image": cover_image,
            "url": track.get_url()
        }

        # append to results
        results.append(track_info)

# TO DO }

    return results



## moods = [ "joy", "sadness", "anger", "fear", "love", "surprise" ]
## 
## for mood in moods:
## 
##     print(mood)
##     tracks = fetch_tracks(mood)
## 
##     for track in tracks:
## 
##         print("Song:", track["song"])
##         print("Artist:", track["artist"])
##         print("Cover Image:", track["cover_image"])
##         print("URL:", track["url"])
## 
## import json
## 
## all_results = {}
## for mood in ["joy", "sadness", "anger", "fear", "love", "surprise"]:
##     all_results[mood] = fetch_tracks(mood)
## with open("lastfm_results.json", "w") as f:
##     json.dump(all_results, f, indent=2)
## 
## print("Saved to lastfm_results.json")