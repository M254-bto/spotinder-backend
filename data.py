import requests

client_id = '4b7fa2bf3f504c359281219a68c48cab'
client_secret = '0f33ead49e17443387549b6dbe2fb04c'


myToken = 'BQAJV2QXbsoMAOrSnaOElbe4g989-JAJtBEYGl8Cl3QrbEho2oNDoGOp33VS6-BW7CQB0jCT4sUSjFRtoeqirs11VOXSfAqtfz2JgLVtjskvQUdfcLZYdxLLzGVhQPYYntC9UURtsDd8wR9Ch9s1-GO92g3clZSC3UOB5r_OxSLFIsFDKG_F85XJSQFtopoL2GH4B8IKyQ9wEBzH7EREQfZN'
myUrl = 'https://api.spotify.com/v1/me/top/tracks?time_range=short_term&limit=50'
head = {'Authorization': 'Bearer f"{myToken}"'}

id = requests.get('https://api.spotify.com/v1/me', headers=head)