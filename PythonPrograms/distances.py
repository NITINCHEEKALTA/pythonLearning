distances={
  "Voyager 1" : 163,
  "Voyage 2" : 136,
  "Pioneer 10": 80,
  "New Horizons": 58,
  "Pioneer 11": 44

}

def main():
    for name in distances.keys():
        print(f"{name} is {distances[name]} AU away from Earth")



main()