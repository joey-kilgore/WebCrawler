import wikipediaapi

def checkExists(pageName):
    # getting a wiki page
    wiki = wikipediaapi.Wikipedia('en')
    page = wiki.page(pageName)

    # check if page exists
    return page.exists()

def getURL(pageName):
    # get the URL
    wiki = wikipediaapi.Wikipedia('en')
    page = wiki.page(pageName)
    return page.fullurl

def getText(pageName):
    # get full text
    wiki = wikipediaapi.Wikipedia(
            language = 'en',
            extract_format = wikipediaapi.ExtractFormat.WIKI
            )
    testWiki = wiki.page(pageName)
    return testWiki.text

def getHTML(pageName):
    # get in html format
    wiki = wikipediaapi.Wikipedia(
            language = 'en',
            extract_format = wikipediaapi.ExtractFormat.HTML
            )
    testWiki = wiki.page(pageName)
    return testWiki.text

# get links to other pages
def getLinks(pageName):
    wiki = wikipediaapi.Wikipedia('en')
    page = wiki.page(pageName)
    links = page.links
    listLinksText = []
    for title in sorted(links.keys()):
        listLinksText.append(title)
    return listLinksText
