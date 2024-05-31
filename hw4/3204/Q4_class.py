class virus:
    def __init__(self, people, city) -> None:
        self.city = city
        self.people = people
        self.total = 0

    def infect(self, times, spread, separate):
        inf = self.total if self.total else 1
        for _ in range(times):
            inf = inf + inf * (spread - separate)

        self.total = inf
        if (self.total > self.people): self.total = self.people
        print("{}'s infected people: {}/{}".format(self.city, self.total, self.people))

    def show_detail(self):
        print("city name: {}".format(self.city))
        print("people num: {}".format(self.people))
        print("current infected: {}".format(self.total))
