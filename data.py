import requests
import pandas as pd

client_id = '4b7fa2bf3f504c359281219a68c48cab'
client_secret = '0f33ead49e17443387549b6dbe2fb04c'


myToken = 'BQC0rNSshfhTBsPRdFd_uMjiwgMGFK1MYgbvirMM3p5zFxZdorPmMyL-gB9P5F2ehN_ZOTNRBKHVSTR_PD_nW6l_F36hFsZkFssk1cr8TzgtKL8E2_2mWHNyODB4LKdAoJLglc6Rt_EIeZrmREdymnxF47XqjuZWxZf7zLEhNuf5n-TCaASERJXDElcpx-A4AylrLP2Xs6J0QMmqsR15aGviWZS_owIgOyo'
myUrl = 'https://api.spotify.com/v1/me/top/tracks?time_range=short_term&limit=50'
head = {'Authorization': 'Bearer {}'.format(myToken)}

id = requests.get('https://api.spotify.com/v1/me', headers=head)
print(id.json())
