from htbapi.core import rawPostSSL, getRequest, shoutboxToText

def getShoutboxLatest(apitoken):
    return rawPostSSL(f"/shouts/get/initial/html/1", "", apitoken, "", "}")

# currently not working... gonna fix
# def sendShoutbox(msg, apitoken):
#    return rawPostSSL("/shouts/new/", f"text={msg}", apitoken, "x-www-form-urlencoded", "")

# def sendConversationMessage(msg, recipient, apitoken):
#    return rawPostSSL("/conversations/new/", f"recipients%5B%5D={recipient}&message={msg}", apitoken, "x-www-form-urlencoded", "")

def getConversations(apitoken):
    return rawPostSSL("/conversations/list/", "", apitoken, "", "")