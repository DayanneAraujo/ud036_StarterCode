class Movie:
    """
    The movie attributes to render the movie on the web page.

    Attributes:
        title (str): Movie's title.
        img (str): Link to a web image for the movie poster.
        trailer (str): Youtube movie trailer link.
    """
    def __init__(self, title, img, trailer):
        self.title = title
        self.poster_image_url = img
        self.trailer_youtube_url = trailer
