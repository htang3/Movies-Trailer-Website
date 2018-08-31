### All the urls I obtained from internet. I do not OWN any of the url link.
import media #import media class
import fresh_tomatoes# obtained from Udacity.

#toy_story is an object of class Movie includes title, storyline, poster_image_url, trailer_youtube
toy_story = media.Movie("Toy Story 2",
                         "A story of a boy and his toys that come to life",
                        "https://image.tmdb.org/t/p/original/kuTPkbQmHxBHsxaKMUL1kUchhdE.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#avatar is an object of class Movie includes title, storyline, poster_image_url, trailer_youtube
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/sco/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#rush_hour2 is an object of class Movie includes title, storyline, poster_image_url, trailer_youtube
rush_hour2 = media.Movie("Rush hour 2",
                        "A comedy action movie filming in USA and Hong Kong",
                        "https://vignette.wikia.nocookie.net/warner-bros-entertainment/images/2/2a/Rush_Hour_2_poster.jpg/revision/latest?cb=20170522033553",
                        "https://www.youtube.com/watch?v=3TpzHFHUiiA")
#movies is list contains all the movie for the website
movies = [toy_story, avatar, rush_hour2]
fresh_tomatoes.open_movies_page(movies)# calling function to open movie webpage.





# print (Moviewebsite.Movie.VALID_RATINGS)
# print(avatar.show_trailer())
 # print (toy_story.poster_image_url)
# print Moviewebsite.Movie.__doc__ # this print out the documentation of the class
