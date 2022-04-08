import requests

# Make voicemonkey announcement via Alexa
def call_monkey(monkey,announcement = ' '):

    PAT = '970f7c8f32b261b84dedd33ba2f77ee1'
    ST = '43e69e6ade59dff6bc96b9531ab12a3f'

    announcement.replace(' ','%20')
    url = 'https://api.voicemonkey.io/trigger?access_token=' + PAT + '&secret_token=' + ST + '&monkey=' + monkey + '&announcement=' + announcement

    requests.get(url)