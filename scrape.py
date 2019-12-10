# this is a collection of scripts to give some sample
#   data scraping using the multiple modules in
#   this repo
import consts
import logger
import wiki
import youtube

def main():
    logger.log(str(wiki.checkExists('Python Programming Language')))
    links = youtube.getVidURLs('Python Programming')
    for link in links:
        logger.log(link)
        logger.log(youtube.getVidInfo(link))

main()
