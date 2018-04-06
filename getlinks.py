import feedparser

def getlinks(url):

    log = open("log.txt", "a")
    f = feedparser.parse(url)
    links = []

    if "bozo_exception" in f:
            print("Error in " + url + " : " + str(f["bozo_exception"]), file=log, flush=True, end=" ")

    for x in range(len(f.entries)):
        link = f.entries[x]["link"]
        if "?source=" in link:
            link = link[0:link.find("?source=")]
        links.append(link)

    print("|", file=log, end=" ", flush=True)

    return links
