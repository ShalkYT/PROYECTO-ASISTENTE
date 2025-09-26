import spotipy
from spotipy import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="5c661126bf62489182b0af067f2f1c27",
    client_secret="9dfd2f4237804dd6be0d818e15065148",
    redirect_uri="https://developer.spotify.com/dashboard/5c661126bf62489182b0af067f2f1c27",  # o la que hayas registrado
    scope="user-modify-playback-state user-read-playback-state"
))

def buscar_cancion(cancion):
    resultado = sp.search(q=cancion, type="track", limit=1)
    if resultado["tracks"]["items"]:
        uri = resultado["tracks"]["items"][0]["uri"]
        sp.start_playback(uris=[uri])
        print(f"Reproduciendo: {resultado['tracks']['items'][0]['name']}")
    else:
        print("No encontré la canción.")
    return