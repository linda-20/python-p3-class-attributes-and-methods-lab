class Song:
    count = 0
    genre_count = {}
    artist_count = {}
    genres = []
    artists = []

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.count += 1

        if genre not in Song.genres:
            Song.genres.append(genre)

        if artist not in Song.artists:
            Song.artists.append(artist)

        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1

    @classmethod
    def total(cls):
        return cls.count
