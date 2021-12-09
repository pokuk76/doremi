import os
import lyricsgenius

genius_client_access_token = os.environ.get('GENIUS_CLIENT_ACCESS_TOKEN')

genius = lyricsgenius.Genius(genius_client_access_token)
song = genius.search_song("Rich Gang", "Lifestyle")
song_lines.lyrics.split('\n')[:10]