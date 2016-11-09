import pendulum
import unittest

from timesheet import Timesheet


class TimesheetTestCase(unittest.TestCase):

    def setUp(self):
        self.timesheet = Timesheet('01-11-2016', '30-11-2016')

    def test_constructor_should_be_able_to_recive_string(self):
        t = Timesheet('01-01-2001', '31-01-2001')

        self.assertIsInstance(t.start_date, pendulum.Pendulum)
        self.assertIsInstance(t.end_date, pendulum.Pendulum)

    def test_constructor_should_be_able_to_recive_date(self):
        t = Timesheet(pendulum.from_date(2001, 1, 1), pendulum.from_date(2001, 1, 1))

        self.assertIsInstance(t.start_date, pendulum.Pendulum)
        self.assertIsInstance(t.end_date, pendulum.Pendulum)

    def test_arrival_time_should_be_in_range(self):
        arrival_time = self.timesheet.get_arrival_time()

        self.assertGreaterEqual(arrival_time, pendulum.from_time(9, 0))
        self.assertLessEqual(arrival_time, pendulum.from_time(11, 59))

    def test_lunch_start_time_should_be_in_range(self):
        lunch_start_time = self.timesheet.get_lunch_start_time()

        self.assertGreaterEqual(lunch_start_time, pendulum.from_time(12, 0))
        self.assertLessEqual(lunch_start_time, pendulum.from_time(14, 0))

    def test_lunch_end_time_should_be_1_hour_later(self):
        lunch_start_time = pendulum.from_time(12, 0)

        self.assertEqual(self.timesheet.get_lunch_end_time(lunch_start_time), pendulum.from_time(13, 0))

    def test_departure_time_should_be_9_hours_later(self):
        arrival_time = pendulum.from_time(9, 0)

        self.assertEqual(self.timesheet.get_departure_time(arrival_time), pendulum.from_time(18, 0))

    def test_timesheet_should_have_all_days_in_range(self):
        timesheet = self.timesheet.get_timesheet()

        self.assertEqual(timesheet, [])


if __name__ == '__main__':
    unittest.main()
