class virus:
    def __init__(self) -> None:
        self.city_list = list()
        self.global_people = 0
        self.global_infect_num = 0
        self.global_infect_rate = 0

    def add_city(self, city_and_infect):
        self.city_list.append(city_and_infect)
        self.count()

    def count(self):
        self.global_people = sum(city.people for city in self.city_list)
        self.global_infect_num = sum(city.infected for city in self.city_list)
        self.global_infect_rate = self.global_infect_num / self.global_people

    def infect(self, city, times, spread, separate):
        for c in self.city_list:
            if (c.name == city): city = c
        inf = city.infected if city.infected else 1
        for _ in range(times):
            inf = inf + inf * (spread - separate)

        city.infected = inf
        if (city.infected > city.people): city.infected = city.people
        print("{}'s infected people: {}/{}".format(city.name, city.infected, city.people))
        self.count()

    def show_detail(self):
        print("Total: {}".format(self.global_people))
        print("current infected: {}".format(self.global_infect_num))
        print("infected rate: {:.2f}".format(self.global_infect_rate))

        for city in self.city_list:
            print("city name: {}".format(city.name))
            print("people num: {}".format(city.people))
            print("current infected: {}".format(city.infected))

class city_and_infect:
    def __init__(self, name, people, infected) -> None:
        self.name = name
        self.people = people
        self.infected = infected

