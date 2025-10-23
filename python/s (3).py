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

class Remix(MusicTrack):
    def __init__(self, title, artist, duration, genre, remixer):
        super().__init__(title, artist, duration, genre)
        self.remixer = remixer

    def play(self):
        print(f"{self.title} (Remix by {self.remixer}) - {self.artist} [{self.genre}]")

track1 = MusicTrack("Angels", "Morandi", 215, "Electronic")
track1.play()
track1.info()

remix = Remix("Angels", "Morandi", 215, "Electronic", "DJ Anemia")
remix.play()