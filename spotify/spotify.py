import os
import requests
import pickle
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import numpy as np
from collections import Counter, defaultdict


class SpotinderModel:
    def __init__(self, acess_token):
        self.access_token = acess_token
        self.extracted_data = []

    def create_spotify(self):
        client_id = '4b7fa2bf3f504c359281219a68c48cab'
        client_secret = '0f33ead49e17443387549b6dbe2fb04c'
        client_credentials_manager = SpotifyClientCredentials(
            client_id=client_id, client_secret=client_secret)
        return spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    def get_user_songs(self):
        myUrl = 'https://api.spotify.com/v1/me/top/tracks?time_range=short_term&limit=50'
        head = {'Authorization': 'Bearer {}'.format(self.access_token)}
        response = requests.get(myUrl, headers=head)
        # id = requests.get('https://api.spotify.com/v1/me', headers=head)
        res = response.json()
        songs = list(
            map(lambda i: {"id":i["id"], "name": i["name"], "uri": i["uri"]}, res['items']))

        return songs

    def feature_extract(self):
        # features = []
        # test this
        songs = self.get_user_songs()
        song_ids = list(map(lambda i: i["id"], songs))
        head = {'Authorization': 'Bearer {}'.format(self.access_token)}
        ids = ','.join([x for x in song_ids])
        url = f'https://api.spotify.com/v1/audio-features?ids={ids}'
        features = requests.get(url, headers=head)
        t_df = []
        for i in features.json().values():
            for j in i:
                t_df.append(j)
        return pd.DataFrame(t_df)
        #
        # song_uris = list(map(lambda i: i["uri"], songs))
        # features = self.create_spotify().audio_features(song_uris)
        # features = filter(lambda i: i != None, features)
        # return pd.DataFrame(features)

    def prep(self):
        data = self.feature_extract()
        ids = pd.DataFrame(data["id"])
        # print(data["id"])
        data.drop(['id', 'uri', 'track_href', 'analysis_url',
                  'time_signature', 'type'], axis=1, inplace=True)

        from sklearn.preprocessing import MinMaxScaler
        scale = MinMaxScaler()
        scale_data = scale.fit(data).transform(data)
        return ids, pd.DataFrame(scale_data, columns=data.columns)

    def fit_model(self):
        ids, data = self.prep()
        song_cluster_labels = self.load_model().predict(data)
        data_with_labels = pd.concat(
            [ids, pd.DataFrame(song_cluster_labels, columns=["cluster_label"])], axis=1)

        value_counts = list(
            data_with_labels['cluster_label'].value_counts().index[0:3])

        values = data_with_labels[data_with_labels['cluster_label'].isin(
            value_counts)]

        value_dict = defaultdict(list)
        for value in values.to_records(index=False):
            # value_dict.setdefault(value[1],[])
            value_dict[value[1]].append(value[0])

        print(value_dict)

        # print(values.to_records(index=False))
        # for value in values:
        # print(value)

        return values

    def predict(self):
        return self.fit_model()

    def load_model(self):
        model = None
        with open(os.path.join(os.getcwd(), 'model.pkl'), 'rb') as f:
            model = pickle.load(f)

        return model

    def assign_labels(self):
        pass



