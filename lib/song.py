class Song:
    count = 0
    genres = []
    artists = []
    genres_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(self.genre)
        self.add_to_artists(self.artist)

    def add_song_to_count(self):
        Song.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre in cls.genres:
            cls.genre_count[genre] += 1
        else:
            cls.genres.append(genre)
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists(cls, artist):
        if artist in cls.artists:
            cls.artist_count[artist] += 1
        else:
            cls.artists.append(artist)
            cls.artist_count[artist] = 1

    @classmethod
    def add_to_genre_count(cls):
        for song in cls.genre:
            genre =  song.genre
            cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artist_count(cls):
        for song in cls.artist:
            artist = song.artist
            cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1

    
#Next, let's move on to implementing remaining class methods:addtogenrecount and `addtoartistcount.

# add_to_genre_count() This method should create histogram of the number songs for each genre. To implement this, we'll add a class attribute calledgenre_count`, which will be a dictionary. The keys of the should be the names of each genre, and the values should be the number of songs that have that genre.
# In the add_genre_count() method, you'll iterate over the genres list and populate the genre_count dictionary with key-value pairs. Check if the genre is already a key in the dictionary. If it is, increment the value of that key by one. If it's not, create a new key-value pair with the genre and set the value to 1.

# Here's an example implementation:

# class Song:
#     count = 0
#     genres = []
#     artists = []
#     genre_count = {}

#     def __init__(self, name, artist, genre):
#         self.name = name
#         self.artist = artist
#         self.genre = genre
#         Song.add_song_to_count()
#         Song.add_to_genres(self.genre)
#         Song.add_to_artists(self.artist)
#         Song.add_to_genre_count(self.genre)

#     @classmethod
#     def add_song_to_count(cls):
#         cls.count += 1

#     @classmethod
#     def add_to_genres(cls, genre):
#         cls.genres.append(genre)

#     @classmethod
#     def add_to_artists(cls, artist):
#         cls.artists.append(artist)

#     @classmethod
#     def add_to_genre_count(cls, genre):
#         if genre in cls.genre_count:
#             cls.genre_count[genre] += 1
#         else:
#             cls.genre_count[genre] = 1


# add_to_artist_count(): This method should create a histogram of the number of songs for each artist. Similar to add_to_genre_count(), you'll add a class attribute called artist_count, which will be a dictionary. The keys of the dictionary should be the names of each artist, and the values should be the number of songs assigned to each artist.
# In the add_to_artist_count() method, iterate over the artists list and populate the artist_count dictionary with key-value pairs. Check if the artist is already a key in the dictionary. If it is, increment the value of that key by one. If it's not, create a new key-value pair with the artist and set the value to 1.

# Here's an example implementation:

# class Song:
#     count = 0
#     genres = []
#     artists = []
#     genre_count = {}
#     artist_count = {}

#     def __init__(self, name, artist, genre):
#         self.name = name
#         self.artist = artist
#         self.genre = genre
#         Song.add_song_to_count()
#         Song.add_to_genres(self.genre)
#         Song.add_to_artists(self.artist)
#         Song.add_to_genre_count(self.genre)
#         Song.add_to_artist_count(self.artist)

#     @classmethod
#     def add_song_to_count(cls):
#         cls.count += 1

#     @classmethod
#     def add_to_genres(cls, genre):
#         cls.genres.append(genre)

#     @classmethod
#     def add_to_artists(cls, artist):
#         cls.artists.append(artist)

#     @classmethod
#     def add_to_genre_count(cls, genre):
#         if genre in cls.genre_count:
#             cls.genre_count[genre] += 1
#         else:
#             cls.genre_count[genre] = 1

#     @classmethod
#     def add_to_artist_count(cls, artist):
#         if artist in cls.artist_count:
#             cls.artist_count[artist] += 1
#         else:
#             cls.artist_count[artist] = 1
# Now you have implemented the add_to_genre_count() and add_to_artist_count() methods. These methods should update the genre_count and artist_count class attributes respectively.

# Feel free to ask any questions or let me know if you need further assistance!