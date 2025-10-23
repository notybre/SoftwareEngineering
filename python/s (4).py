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

    def set_duration(self, seconds):
        if seconds > 0:
            self.__duration = seconds
        else:
            print("Ошибка: длительность должна быть положительной")

    def get_duration(self):
        return self.__duration

class Remix(MusicTrack):
    def __init__(self, title, artist, duration, genre, remixer):
        super().__init__(title, artist, duration, genre)
        self.remixer = remixer

    def play(self):
        print(f"{self.title} (Remix by {self.remixer}) - {self.artist} [{self.genre}]")

track1 = MusicTrack("Angels", "Morandi", 215, "Electronic")
track1.play()
track1.info()
track1.set_duration(290)
print("Новая длительность: ", track1.get_duration())

remix = Remix("Angels", "Morandi", 215, "Electronic", "DJ Anemia")
remix.play()