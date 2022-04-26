{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "54246327-9fd6-4117-9994-9fb503ab6b2d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Importing libraries\n",
    "\n",
    "import spotipy\n",
    "import spotipy.util as util\n",
    "from spotipy.oauth2 import SpotifyClientCredentials\n",
    "import pandas as pd\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "2ed940be-acad-4a57-a469-0503013cf928",
   "metadata": {},
   "outputs": [],
   "source": [
    "#ID - API Spotify\n",
    "client_id = \"673b79adfd804ab4a23af985d9cbb658\"\n",
    "client_secret = \"52dd4615fddb4b40bc37d32f1c8d47a3\"\n",
    "client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)\n",
    "sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "4452bc78-0bf4-4907-97e7-16dacc41d7ce",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "42\n",
      "['6r6n5OmXkdsOxN2iCj5UE0', '5Ohxk2dO5COHF1krpoPigN', '1v1oIWf2Xgh54kIWuKsDf6', '50PWlIBU7PlGGwzgN8TiFJ', '3O2pB9JHreUZ9F83qSNmu8', '3rgCo7v5weniRXyS33oci5', '3Z0YN50RzRtmYre1bRG8H6', '6epvwUINain4iSHCTWA0sj', '2DyCLtTrd9f2DRRDq1ngJx', '2Ro9FLIVhPwIQopSr48oJT', '75JFxkI2RXiU7L9VXzMkle', '0YywjDvFudcaHG74NuWISy', '7Bc7VX0EvuqcPQKB1ryl9n', '4JuJZzGcswQszYiKJSnC6i', '5eXnC2B5RU5fAhfwvV2ABD', '1Fid2jjqsHViMX6xNH70hE', '2eL0BfP66sUvn4NF6qhhXt', '2Q3UgGcvhdaX6k13PDNguP', '6dVa7xk5dOoT6pOkDw1TMH', '0y1QJc3SJVPKJ1OvFmFqe6', '4cOHlNcWTar1cxZHsFJinm', '6z4VbB0iJuCb5Sa4JyToA3', '3cUxncrTWSA9lhlQbuIwUY', '3uYxmgnOA9lJYAsHyEbbWA', '0HC0DQfCneEYFMRYCG9m4s', '4unF8ldGPeedLz8HRIvgxg', '3Mz4SvGYz0006jcJzXZN6Q', '5Qn7UBFKV5iemqZMJ5F5ve', '3V8GgZl2XQf3RXJPHyXPhK', '4Jxpl6VyiKxq8okAnvJjzE', '31Bo96RZ9kXjzQ5e19Ufwg', '4NZKQIAbpUPd0jn0CzvRpS', '7lpmIGFw7Kc9qIdq4cGs34', '1SCXzqKZdif5b33POmzwI4', '60udPy5pdeKLDaP15A5iXO', '4oLLl2b0pZ5Ksp4SWISJyx', '2YGqpzBhtJxt9M5g1czYg4', '5MzXUNfn8AAcz4Z6j2KgTK', '1z6ytxdIawe7Dd14cfiSQf', '0TbP1ASV5mBpwpME75LWRA', '2ofamXq9GDR9pk9m6CCOi9', '4JCrcaEMsvYHji82lGRc4G']\n"
     ]
    }
   ],
   "source": [
    "#Collect data from playlist\n",
    "def getTrackIDs(user, playlist_id):\n",
    "    ids = []\n",
    "    playlist = sp.user_playlist(user, playlist_id)\n",
    "    for item in playlist['tracks']['items']:\n",
    "        track = item['track']\n",
    "        ids.append(track['id'])\n",
    "    return ids\n",
    "\n",
    "ids = getTrackIDs('r80y0fe9xhvvovsbjsap8pt6k', '7yltiHmKPFUFV4XBJYe2tk')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "332ff69f-e46e-4016-96f1-f5b39a837039",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Get track info from ids\n",
    "def getTrackFeatures(id):\n",
    "  meta = sp.track(id)\n",
    "  features = sp.audio_features(id)\n",
    "\n",
    "  # meta\n",
    "  name = meta['name']\n",
    "  album = meta['album']['name']\n",
    "  artist = meta['album']['artists'][0]['name']\n",
    "  release_date = meta['album']['release_date']\n",
    "  length = meta['duration_ms']\n",
    "  popularity = meta['popularity']\n",
    "\n",
    "  # features\n",
    "  acousticness = features[0]['acousticness']\n",
    "  danceability = features[0]['danceability']\n",
    "  energy = features[0]['energy']\n",
    "  instrumentalness = features[0]['instrumentalness']\n",
    "  liveness = features[0]['liveness']\n",
    "  loudness = features[0]['loudness']\n",
    "  speechiness = features[0]['speechiness']\n",
    "  tempo = features[0]['tempo']\n",
    "  time_signature = features[0]['time_signature']\n",
    "\n",
    "  track = [name, album, artist, release_date, length, popularity, danceability, acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature]\n",
    "  return track"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "89919286-e985-4173-ac7f-925fff71e304",
   "metadata": {},
   "outputs": [],
   "source": [
    "# loop over track ids \n",
    "tracks = []\n",
    "for i in range(len(ids)):\n",
    "  time.sleep(.5)\n",
    "  track = getTrackFeatures(ids[i])\n",
    "  tracks.append(track)\n",
    "\n",
    "# create dataset\n",
    "df = pd.DataFrame(tracks, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])\n",
    "df.to_csv(\"spotify.csv\", sep = ',')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ee15127d-f5b7-47ae-9c7e-65c2c2bc4bdf",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
