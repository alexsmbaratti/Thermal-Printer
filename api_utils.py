import requests

api_url = 'http://pixel-shelf.local:3000'


def getLibraryCount():
    print('Fetching library count from server...')
    try:
        r = requests.get(url=api_url + '/api/library/size')
        data = r.json()
        count = data['size']
        print('Fetched ' + str(count) + ' games from server')
        return count
    except requests.exceptions.ConnectionError:
        print('Could not fetch size from server!')
        return -1
