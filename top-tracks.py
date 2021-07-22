import requests 
from pprint import pprint


spotify_access_token = 'BQD_k7y9pHJyhCtJWYrZrBz23cLGRUMOVtOLUwUZgbiq0Tkl9oCELLQEyuYk3VnPoOyd6pOBsWn2oL5fxOEujWTUGjRrReR8-DOuehnJyxbvrxquPcrLy_2-lNL4OKL-ODnBAQuFdOISq0tPA7xfVRFWwjQpV0Bs71_bm3rqmg'
spotify_get_top_tracks_url = 'https://api.spotify.com/v1/me/top/tracks?time_range=long_term&limit=50'


def get_top_tracks(access_token):
    response = requests.get(
        spotify_get_top_tracks_url,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
    resp_json = response.json()
    items = resp_json['items']
    top_tracks = []
    for item in items:
        track_name = item['name']
        album_name = item['album']['name']
        release_date = item['album']['release_date']
        artists = item['artists']
        artist_name = artists[0]['name']
        top_track = {
        "name": track_name,
        "artist": artist_name,
        "album": album_name,
        "release_date": release_date
        }
        top_tracks.append(top_track)
        
    return top_tracks

def main():
    top_tracks_info = get_top_tracks(
        spotify_access_token
    )
    
    pprint(top_tracks_info, indent=4)

if __name__ == '__main__':
    main()