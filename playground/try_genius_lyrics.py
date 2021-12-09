import os
import requests
import lyricsgenius


genius_client_access_token = os.environ.get('GENIUS_CLIENT_ACCESS_TOKEN')

# genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={client_access_token}"
# response = requests.get('https://api.genius.com/songs/378195/', auth=('user', 'pass'))

# data = response.json()

# with open('response.json', 'w') as outfile:
#     json.dump(data, outfile)

genius = lyricsgenius.Genius(genius_client_access_token)
song = genius.search_song("Rich Gang", "Lifestyle")
print(song.lyrics.split('\n')[:10])  # print first 10 lines
# song.save_lyrics(extension='txt')
