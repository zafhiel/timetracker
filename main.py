import os
from datetime import date, timedelta

import toml
from timetracker import timetracker

toml_data = {
    "credentials": {
        "username": "user",
        "password": "pass"
    },
    "options": {
        "project": "project exact name",
        "assignment": "Software Development",
        "focal": "focal exact name",
    }
}

config_file = os.path.join(os.getcwd(), "config.toml")

with open(config_file, "w") as toml_file:
    toml.dump(toml_data, toml_file)


def send(date_track, text, hours, kind):
    timetracker.load_hours(text, config_file, date_track, False, False, hours, kind)


today = date.today().strftime("%d/%m/%Y")
# today = (date.today() - timedelta(days=1)).strftime("%d/%m/%Y")  # yesterday

# 1:  Bug Fixing
# 2:  Code review
# 3:  Configuration
# 4:  Debug
# 5:  Deployment
# 6:  Environment setup
# 7:  Features development
# 8:  Other - Development'
# 9:  Requirements analysis
# 10: Research / Analysis
# 11: Research and Learning
# 12: Client Meeting

activities = [
    # ("Implement new environment", 1, 10),
    # ("Implement new environment", 1, 10),
    # ("Implement new environment", 1, 10),
    ("Meet Vacation Plan", 0.5, 12),
    # ("Analysis Ticket issues", 1, 11),
    # ("Analysis Ticket issues", 1, 11),
    # ("Analysis Ticket issues", 1, 11),
    # ("Testing ticket", 0.5, 1),
    # ("Testing ticket", 1, 1),
    # ("Testing ticket", 1, 1),
]

for track in activities:
    send(today, track[0], track[1], track[2])

timetracker.show_hours(config_file, today, today, True, False)
os.remove(config_file)

