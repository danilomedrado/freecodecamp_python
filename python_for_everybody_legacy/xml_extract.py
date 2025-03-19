import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)

comments = tree.findall('comments/comment')
nums = list()
for comment in comments:
    nums.append(int(comment.find('count').text))
print('Count:', len(nums))
print('Sum:', sum(nums))
