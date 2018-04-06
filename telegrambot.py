import urllib.parse
import urllib.request


def sendmsg(newitem):
    token = ""
    chatid = ""

    methods = {"msg" : "sendMessage"}

    url = "https://api.telegram.org/bot" + token + "/" + methods["msg"]
    values = {"chat_id" : chatid, "text" : newitem}
    data = urllib.parse.urlencode(values)
    data = data.encode("utf-8")

    req = urllib.request.Request(url, data)
    resp = urllib.request.urlopen(req)
