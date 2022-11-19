import pytumblr

class sathtumblr:
    def __init__(self, blogname:str, consumerKey:str, consumerSecret:str, oauthToken:str, oauthSecret:str):
        self.blogname = blogname
        self.client = pytumblr.TumblrRestClient(
            consumerKey,
            consumerSecret,
            oauthToken,
            oauthSecret
        )

    #post a text post to tumblr
    def postText(self, title:str, body:str):
        self.client.create_text(self.blogname, state="published", title=title, body=body)

    #post a photo post to tumblr
    def postPhoto(self, caption:str, path:str):
        self.client.create_photo(self.blogname, state="published", caption=caption, data=path)
