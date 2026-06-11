from abc import ABC, abstractmethod


class Hair(ABC):
    def __init__(self, moisture, elasticity,condition):
        self.moisture = moisture
        self.elasticity = elasticity
        self.condition = condition

    @abstractmethod
    def the_weather(self, weather):
        pass

    def describe(self):
        return f"moisture = {self.moisture}, elasticity = {self.elasticity}, conditon = {self.condition}"
    
class CurlyHair(Hair):
    def __init__(self):
        super().__init__(moisture=40, elasticity=60, condition = "")
    def the_weather(self, weather):
        
        if weather == "rain":
            self.moisture += 20
            self.elasticity += 15
            self.condition = "Your hair is now wet, soggy, and looks like a bag of seaweed."
        
        elif weather == "sun":
            self.moisture -= 10
            self.elasticity +=5
            self.condition = "Your hair is now a bit dry."
        
        elif weather == "wind":
            self.moisture += 0
            self.elasticity +=20
            self.condition = "Your hair is now messed up, have fun dealing with them tangled hairs."

        elif weather == "humid":
            self.moisture += 30
            self.elasticity +=10
            self.conditon = "Your hair is now humid, make sure to wash them."

class StraightHair(Hair):
    def __init__(self):
        super().__init__(moisture=40, elasticity=40, condition = "")
    def the_weather(self, weather):
        
        if weather == "rain":
            self.moisture += 20
            self.elasticity += 10
            self.conditon = "Your hair is now wet and soggy."

        elif weather == "sun":
            self.moisture -= 10
            self.elasticity +=5
            self.condition = "Your hair is now a bit dry."

        elif weather == "wind":
            self.moisture += 0
            self.elasticity +=15
            self.condition = "Your hair is a bit messy."

        elif weather == "humid":
            self.moisture += 30
            self.elasticity +=10
            self.condition = "Your hair is now humid, and get's oiled easily, make sure to wash them."

class NoHair(Hair):
    def __init__(self):
        super().__init__(moisture=20, elasticity=0, condition = "")
    def the_weather(self, weather):
        
        if weather == "rain":
            self.moisture += 10
            self.elasticity += 0
            self.condition = "Your head is wet and hair is still non-existence."
        
        elif weather == "sun":
            self.moisture -= 10
            self.elasticity +=0
            self.condition = "Your head is now a cheap IKEA lightbulb with face on it."
        
        elif weather == "wind":
            self.moisture += 5
            self.elasticity +=0
            self.condition = "Your head is now more aerodynamic than my neighbour's cat."

        elif weather == "humid":
            self.moisture += 5
            self.elasticity +=0
            self.condtion = "Your head is now humid, and perhaps..more refreshing! But still bald tho."


hair_type = { "straight": StraightHair, "curly": CurlyHair, "bald": NoHair}

choice = input("What's your hair type? (straight/curly/bald): ")

hair_class = hair_type.get(choice)

if not hair_class:
    print("Sorry, we don't have this hairstyle yet")

else :
    hair = hair_class()
    print("\nBefore weather : ")
    print(hair.describe())

    weather = input("\nWhat's the weather outside like ? (rain/humid/sun/wind) : ")

    hair.the_weather(weather)

    print("\nAfter the weather : ")
    print(hair.describe())
