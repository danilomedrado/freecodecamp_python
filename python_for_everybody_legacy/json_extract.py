import urllib.request
import json

url = input('Enter location: ')
if len(url) < 1 : 
    url = 'https://py4e-data.dr-chuck.net/comments_42.json'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')
info = json.loads(data)

comments = info['comments']
nums = list()

for comment in comments:
    nums.append(int(comment['count']))

print('Count:', len(nums))
print('Sum:', sum(nums))
