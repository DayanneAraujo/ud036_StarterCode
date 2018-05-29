class Movie:
    '''
    The movie class has the attributes required to render the movie on the web page.
    '''
    def __init__(self, title, img, trailer):
        self.title = title
        self.poster_image_url = img
        self.trailer_youtube_url = trailer