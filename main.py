import random

#getDinner() function not only gets the users input for the amount of dinners but it also checks to see if they have picked a number out of the length the of fortunes array
def getDinner(): 
    dinner = validateDinner("Please enter the amount of dinners: ")
    while True:
        if dinner > 8:
            dinner = validateDinner("Please choose a number less than 9: ")
        else:
            break
    return dinner

def validateDinner(question):
    while True:
        try:
            dinner = int(input(question))
            return dinner
        except ValueError:
            print("Please enter a valid number.")

# A list of all fortunes
fortunes = ["A closed mouth gathers no feet.","He who throws dirt is losing ground.","Borrow money from a pessimist. They don't expect it back.","Life is what happens to you while you are busy making other plans.","Help! I'm being held prisoner in a fortune cookie factory","Dance as if no one is watching.","Live this day as if it were your last.","Your life will be happy and peaceful.","Reach for joy and all else will follow.","Move in the direction of your dreams.","Bloom where you are planted.","Appreciate. Appreciate. Appreciate.","Happy News is on its way.","All the troubles you have will pass away very quickly.","All will go well with your new project.","All your hard work will soon pay off.","Allow compassion to guide your decisions.","An acquaintance of the past will affect you in the near future.","An agreeable romance might begin to take on the appearance.","An important person will offer you support.","An inch of time is an inch of gold.","Any day above ground is a good day."]

dinner = getDinner()
pickedFortunes = [] # This stores the index of the random number picked
for i in range(dinner):
    while True: #   This while loop is used so that it chooses a fortune that is not already in the pickedFortunes array

        pickedFortune = random.randint(0, len(fortunes))  # This gets the random number used for the index of the array

        if pickedFortune not in pickedFortunes: # This IF statement is used to check if the pickedFortune is in the list or not
            pickedFortunes.append(pickedFortune)
            print(f"{i+1}: {fortunes[pickedFortune - 1]}") # Displays the sayings inside the fortune
            break
