class MusicTrack:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def play(self):
        print(f"Сейчас играет: {self.title} - {self.artist} ({self.duration} сек.)")

track1 = MusicTrack("Angels", "Morandi", 215)

track1.play()
