from urllib.request import urlopen, urlretrieve
import re
import os

def download_files(link, regular_link, regular_name):
    resp = urlopen(link)
    htmltext=resp.read().decode('utf-8')

    titles = re.findall(regular_link, htmltext)
    for title in titles:
        try:
            urlretrieve('https://2ch.hk' + title, os.path.join('Download', re.findall(regular_name, title)[0]))
        except Exception as e:
            print(e)


if not os.path.exists('Download'):
    os.makedirs('Download')

case = input('Input 1 for pictures, input 2 for videos: ')
site = input('Input link thread: ')

if case is '1':
    download_files(site, '/b\/src\/\d{1,}\/\w{1,}.jpg', '\w{1,}.jpg')
    download_files(site, '/b\/src\/\d{1,}\/\w{1,}.png', '\w{1,}.png')
elif case is '2':
    download_files(site, '/b\/src\/\d{1,}\/\w{1,}.webm', '\w{1,}.webm')
    download_files(site, '/b\/src\/\d{1,}\/\w{1,}.mp4', '\w{1,}.mp4')
