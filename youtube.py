from pytube import YouTube
from bs4 import BeautifulSoup
import requests

def getVidURLs(search):
    # using the passed search string, get all links from the search page
    #   from youtube
    # build youtube search url from search keywords
    searchURL = 'https://www.youtube.com/results?search_query='+search.replace(" ","+")
    print(searchURL)
    r = requests.get(searchURL)
    data = r.text
    
    # after getting the page we can use BeautifulSoup to scrape links
    soup = BeautifulSoup(data)
    aTags = soup.findAll(attrs={'class':'yt-uix-tile-link'})
    links = []
    for a in aTags:
        if('adservices' not in a['href']):
            links.append('https://www.youtube.com' + a['href'])
    
    return links

def getVidInfo(vid_url):
    # return a string containing the title, vid id, and age restricted bool
    #   from the video at the url passed
    # get the video
    youtube = YouTube(vid_url)

    # get the info
    info = 'Title: %s\n' % (youtube.title)
    info += 'ID   : %s\n' % (youtube.video_id)
    info += 'AGE RESTRICTED: %s\n' % (youtube.age_restricted)
    
    return info

def downloadVid(vid_url, directory):
    # download the vid at the passed url and save it
    #   to the passed directory
    # get the video
    youtube = YouTube(vid_url)

    # download
    vid = youtube.streams.first()
    vid.download(directory)

def getVidCaptions(vid_url):
    # return a string containing the english captions from the video
    # get the video
    youtube = YouTube(vid_url)
    
    # get captions
    caption = youtube.captions.get_by_language_code('en')
    return caption.generate_srt_captions()
