class MusicTrack:
    def __init__(self, title, artist, duration, genre):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.genre = genre

    def play(self):
        print(f"Сейчас играет: {self.title} - {self.artist} ({self.duration} сек.)")

    def info(self):
        minutes = self.duration // 60
        seconds = self.duration % 60
        print(f"Продолжительность: {minutes} мин {seconds} сек")

track1 = MusicTrack("Angels", "Morandi", 215, "Electronic")

track1.play()
track1.info()