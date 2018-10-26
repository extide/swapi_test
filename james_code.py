#!/usr/bin/env python

import swapi

for starship in swapi.get_all("starships").order_by("name"):
    if len(starship.pilots) > 0:
        print("Starship: " + starship.name.encode('utf8'))
        for pilot in starship.get_pilots().order_by("name"):
            print("Pilot: " + pilot.name.encode('utf8'))
        print("")


