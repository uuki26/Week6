import requests
import json

__author__ = "Xinyue"

api_search_url = 'http://schlesinger.radcliffe.harvard.edu/onlinecollections/blackwell/search?query=&doctypes%5B%5D=Notebooks%2C+sketchbooks%2C+etc'

params = {
    'proxtext': 'archeology'      
}

params['format'] = 'json'

response = requests.get(api_search_url, params=params)

print('Here\'s the formatted url that gets sent to the ChronAmerca API:\n{}\n'.format(response.url))

if response.status_code == requests.codes.ok:
    print('All ok')
elif response.status_code == 403:
    print('There was an authentication error. Did you paste your API above?')
else:
    print('There was a problem. Error code: {}'.format(response.status_code))

data = response.json()

from pygments import highlight, lexers, formatters

formatted_data = json.dumps(data, indent=2)

highlighted_data = highlight(formatted_data, lexers.JsonLexer(), formatters.TerminalFormatter())

print(highlighted_data)

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)

