import requests
import lyricsgenius


genius_client_access_token = "SHyOOT2U2P6LrULDfZyOcS72HZLaPe0Vmpa4INPJvJHku9bqVk1I5gOfaFBJQTEA"

# genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={client_access_token}"
# response = requests.get('https://api.genius.com/songs/378195/', auth=('user', 'pass'))

# data = response.json()

# with open('response.json', 'w') as outfile:
#     json.dump(data, outfile)

genius = lyricsgenius.Genius(genius_client_access_token)
song = genius.search_song("Rich Gang", "Lifestyle")
print(type(song))
song.save_lyrics(extension='txt')
