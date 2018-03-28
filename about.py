import wikipedia
def tellmeabout(a):
    content=a[13::]
    try:
        a=wikipedia.summary(content,sentences=3)
        return a
    except:
        return "EITHER THIS IS DIIFICULT OR YOU HAVE USED WRONG SPELLINGS."

