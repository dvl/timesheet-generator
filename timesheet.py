import random
import pendulum


class Timesheet:

    def __init__(self, start_date, end_date):
        if isinstance(start_date, str):
            start_date = pendulum.parse(start_date)

        if isinstance(end_date, str):
            end_date = pendulum.parse(end_date)

        self.start_date = start_date
        self.end_date = end_date

    def get_filled_timesheet(self):
        timesheet = []
        period = pendulum.period(self.start_date, self.end_date)

        for date in period:
            arrival_time = self.get_arrival_time()
            lunch_start_time = self.get_lunch_start_time()
            lunch_end_time = self.get_lunch_end_time(lunch_start_time)
            departure_time = self.get_departure_time(arrival_time)

            timesheet.append((date, arrival_time, lunch_start_time, lunch_end_time, departure_time))

        return timesheet

    def get_arrival_time(self):
        hour = random.choice(range(9, 12))
        minute = random.choice(range(1, 60))

        return pendulum.from_time(hour, minute)

    def get_lunch_start_time(self):
        hour = random.choice(range(12, 14))
        minute = random.choice(range(1, 60))

        return pendulum.from_time(hour, minute)

    def get_lunch_end_time(self, lunch_start_time):
        return lunch_start_time.add(hours=1)

    def get_departure_time(self, arrival_time):
        return arrival_time.add(hours=9)


if __name__ == '__main__':
    ts = Timesheet('01-11-2016', '30-11-2016').get_filled_timesheet()

    for day in ts:
        print(day)

## TODO: Margem de erro pra volta de almoço e saida, pra não ficar +1 e +9 hrs certinho
