class Camera:
    def click_photo(self):
        print("Photo clicked")

    def record_video(self):
        print("Recording started")

class MusicPlayer:
    def play_song(self):
        print("Playing song")

    def pause_song(self):
        print("Song paused")

class SmartPhone(Camera, MusicPlayer):
    pass

s = SmartPhone()
s.click_photo()
s.record_video()
s.play_song()
s.pause_song()