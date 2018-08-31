# import webbrowser
#Class Movie contains init function to initialize the movie info.
class Movie():#google python style guide:
    """This class allows user to store movies info"""
    VALID_RATINGS = ["G","PG","PG-13","R"]#class variable ALL CAPS
    def __init__(self, movie_title, move_storyline, poster_image,trailer_youtube):  #a constructor, self is python mandatory word, self pointed to object.
        """ this function initialize title, storyline, poster, trailer of a movieself.
            @param movie_title presents the titile of a movieself.
            @param storyline shows the content of the movie, what movie is absolute
            @param poster_image show the poster of the movies
            @param trailer_youtube shows the trailer of the movie through youtube."""
        self.title = movie_title
        self.storyline =move_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # def show_trailer(self):
    #     """show_trailer is to open the youtube url when user click on the poster  """
    #     webbrowser.open(self.trailer_youtube_url)
