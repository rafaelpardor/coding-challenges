#!/usr/bin/python3
# Challenge: codewars.com/kata/515e188a311df01cba000003/

def get_planet_name(id):
    planets = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune",
    }
    return planets[id]
