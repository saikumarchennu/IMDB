from  imdb import imdb


def findRating():
    # Assigning the imdb instance to a local instance named localsearch
    localsearch= IMDb()

    # Accepting the  movie name from user
    name  = input("Enter movie of your choice : ")

    # This looks in imdb DB for movies relevant to the user
    query = localsearch.search_movie(name)



    # Displaying  the  movie list
    for movie in query:
        print(movie.movieID, movie)

    print("__")

    # getting movie specific id from user
    movieid = input("Enter the id for the movie you looking from above list: ")

    # collecting movie queryset
    query = localsearch.get_movie(movieid)

    # display the rating
    print("Ratings for the Movie is: {}".format(query.data['rating']))


findrating()