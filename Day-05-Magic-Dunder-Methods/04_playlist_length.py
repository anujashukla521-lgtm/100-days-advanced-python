class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

    def __str__(self):
        return f"List of songs: {self.songs}"

playlist = Playlist(["SongA", "SongB", "SongC"])
print(len(playlist))
print(playlist)
