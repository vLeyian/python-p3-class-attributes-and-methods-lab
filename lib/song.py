class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genre(genre)
        self.add_to_artists(artist)
    
    @classmethod
    def add_to_genre(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
            cls.genre_count[genre] = 1
        else:
            cls.genre_count[genre] += 1

        
    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment
    
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
            cls.artist_count[artist] = 1
        else:
            cls.artist_count[artist] += 1
    


    

        