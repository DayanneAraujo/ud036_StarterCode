# -*- coding: utf-8 -*-
import fresh_tomatoes
import media


# Creating Movie Objects
# Matrix
matrix = media.Movie(
    title="Matrix",
    img="http://t0.gstatic.com/images?q=tbn:ANd9GcQq3pIz-aKgkmYX1dJ-EL-AlHSPcOO7wdqRIJ5gJy9qNinXpmle",
    trailer="https://www.youtube.com/watch?v=vKQi3bBA1y8"
)

# Nemo
nemo = media.Movie(
    title="Finding Nemo",
    img="http://t1.gstatic.com/images?q=tbn:ANd9GcSoStMb2jeN136xQhf2g3ROpTB9Dker9IlfGbMbwYB3ruC9VcOj",
    trailer="https://www.youtube.com/watch?v=wZdpNglLbt8"
)

# Mad Max
mad_max = media.Movie(
    title='Mad Max: Fury Road',
    img="http://t0.gstatic.com/images?q=tbn:ANd9GcQuK41mExh1Qv3kbXoxohWYGlcstOQ6zEnnNdSI2BGIKywQwgRI",
    trailer="https://www.youtube.com/watch?v=hEJnMQG9ev8"
)

# Quiet Place
quiet_place = media.Movie(
    title="A quiet place",
    img="https://pbs.twimg.com/media/DVOikE9V4AEalKX.jpg",
    trailer="https://www.youtube.com/watch?v=WR7cc5t7tv8"
)

# America Captain
captain_america = media.Movie(
    title="Captain America: The First Avenger",
    img="https://upload.wikimedia.org/wikipedia/en/3/37/Captain_America_The_First_Avenger_poster.jpg",
    trailer="https://www.youtube.com/watch?v=JerVrbLldXw"
)


# Star Wars
star_wars = media.Movie(
    title="Star Wars: the force awakens",
    img="http://t0.gstatic.com/images?q=tbn:ANd9GcT6nGxj1D4P-9EiVSY32sb6Ql-XQrbeK5FgM37UI6QxcZwfcfVw",
    trailer="https://www.youtube.com/watch?v=sGbxmsDFVnE"
)


# Creating movie's list
movies = [matrix, nemo, mad_max, quiet_place, captain_america, star_wars]

# Open the web browser rendering the movie's list
fresh_tomatoes.open_movies_page(movies)
