from hair import CurlyHair, StraightHair, NoHair

def run_simulation(hair):
    print("\n-Before weather-")
    print(hair.describe())

    weather = input("\nEnter weather (rain / sun / wind / humid): ").lower()

    hair
