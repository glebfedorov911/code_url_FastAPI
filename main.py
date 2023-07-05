# ИСПОЛЬЗОВАЛ КОДИРОВКУ ПО ЭТОЙ ССЫЛКЕ
# https://translated.turbopages.org/proxy_u/
# en-ru.ru.6f5cddb7-64a3ee4d-6eb0903f-74722d776562/https/en.wikipedia.org/wiki/URL_encoding

from fastapi import FastAPI, Request

app = FastAPI()


class Coding:
    CODE_DATA = {
        " ":"%20", "!":"%21", '"':"%22", "#":"%23", "$":"%24", "%":"%25", "&":"%26", "'":"%27", "(":"%28", ")":"%29",
        "*":"%2A", "+":"%2B", ",":"%2C", ";":"%3B", "=":"%3D", "?":"%3F", "@":"%40", "[":"%5B",
        "]":"%5D", "\n":"%0A", "-":"%2D", "<":"%3C", ">":"%3E", "^":"%5E", "_":"%5F", "`":"%60", "{":"%7B",
        "|":"%7C", "}":"%7D", "~":"%7E", "£":"%C2%A3"
    }

    def __init__(self, url):
        self.url = url

    def code_url(self):
        return ''.join(self.coding_process(self.url, self.CODE_DATA))

    def coding_process(self, url, data):
        for symbol in url:
            try:
                yield data[symbol]
            except:
                yield symbol

@app.get("/")
def code_url(request: Request, url: str = None):
    result = {}
    try:
        code = Coding(url)
        result.update({"status": "success", "url":code.code_url()})
    except:
        result.update({"status": "not success", "url":""})

    return result

@app.get("/%/%")
def test():
    return {"message": "Hello world!"}