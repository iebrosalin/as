class APIRange:
    def __init__(self, API):
        self.API = API

objects = [APIRange("В исходном коде не обнаружено URL ведущих к API skillbox.ru.")]

print(objects[0].API)