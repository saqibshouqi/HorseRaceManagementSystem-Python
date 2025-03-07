import random
import json

horse_details = []
selected_horses = []
sorted_horses = []
race_started = False  # Variable to track whether the race has started

def adding_horse_details():
    # Function to add horse details
    if not race_started:
        horse_id =input("Enter horse ID: ")
        # Check if the horse with the same ID already exists
        existing_horse = next((horse for horse in horse_details if horse["horse_id"] == horse_id), None)
        if existing_horse:
            print(f"Horse with ID {horse_id} already exists:")
            print(existing_horse)
        else:
            horse_name = input("Enter horse name: ")
            jockey_name = input("Enter Jockey name: ")
            age = input("Enter horse age: ")
            breed = input("Enter horse breed: ")
            race_record = input("Enter horse race record: ")
            group = input("Enter horse group: ").upper()

            horse = {"horse_id":horse_id,"horse_name": horse_name,"jockey_name":jockey_name, "age": age, "breed": breed,"race_record":race_record, "group":group}
            horse_details.append(horse)
            print("Horse details added successfully!")

    else:
        print("Cannot add horse details after the race has started.")

def deleting_horse_details():
    # Function to delete horse details based on horse_id
    if not race_started:
        horse_id = input("Enter horse id to delete horse details: ")
        for horse in horse_details:
            if horse["horse_id"] == horse_id:
                horse_details.remove(horse)
                print("Horse details deleted successfully!")
                return
        print("Horse not found.")
    else:
        print("Cannot delete horse details after the race has started.")

def update_horse_details():
    # Function to update horse details based on horse_id
    if not race_started:
        horse_id= input("Enter horse id to update: ")
        for horse in horse_details:
            if horse["horse_id"] == horse_id:
                horse["horse_name"] = input("Enter new horse name: ")
                horse["jockey_name"] = input("Enter new jockey name: ")
                horse["age"] = input("Enter new horse age: ")
                horse["breed"] = input("Enter new horse breed: ")
                horse["race_record"] = input("Enter new race record: ")
                horse["group"] = input ("Enter new horse group: ").upper()
                print("Horse details updated successfully!")
                return
        print("Horse not found.")
    else:
        print("Cannot update horse details after the race has started.")

def view_horses_details():
    # Function to view horse details sorted by Horse ID
    sorted_horses = sorted(horse_details, key=lambda x: x.get("horse_id", 0))
    print("\nHorse Details Table (Sorted by Horse ID):")
    print("{:<10} {:<15} {:<15} {:<10} {:<15} {:<25} {:<10}".format(
        "horse_id", "horse_name", "jockey_name", "age", "breed", "race_record", "group"))
    for horse in sorted_horses:
        print("{:<10} {:<15} {:<15} {:<10} {:<15} {:<25} {:<10}".format(
            horse.get("horse_id", ""),
            horse.get("horse_name", ""),
            horse.get("jockey_name", ""),
            horse.get("age", ""),
            horse.get("breed", ""),
            horse.get("race_record", ""),
            horse.get("group", "")
        ))

def save_horse_details():
    # Function to save horse details to a text file
    with open("horse_details.txt", "w") as file:
        json.dump(horse_details, file)
    print("Horse details saved to file successfully!")


def select_for_major_round():
    global horse_details  # Add this line to make changes to the global variable
    # Ensure that the horse details are loaded from the file
    try:
        with open("horse_details.txt", "r") as file:
            horse_details = json.load(file)
    except FileNotFoundError:
        print("Error: Horse details file not found. Please add horse details first.")
        return []
    # Group horses by their group attribute
    grouped_horses = {}
    for horse in horse_details:
        group = horse.get("group", "")
        if group not in grouped_horses:
            grouped_horses[group] = []
        grouped_horses[group].append(horse)
    # Select a random horse from each group and initialize the "Time" attribute
    selected_horses = []
    for group, horses_in_group in grouped_horses.items():
        if len(horses_in_group) >= 1:
            selected_horse = random.choice(horses_in_group)
            selected_horse["Time"] = 0  # Initialize the "Time" attribute
            selected_horses.append(selected_horse)
    # Display the randomly selected horses' details of each group
    if selected_horses:
        print("\nRandomly Selected Horses for the Major Round:")
        for horse in selected_horses:
            print(f"Group {horse['group']}: {horse['horse_name']} ({horse['horse_id']})")
    else:
        print("No horses available for the major round.")
    return selected_horses

def display_winning_horses(selected_horses):
    # Simulate random time for each horse selected for the major round
    for horse in selected_horses:
        horse["Time"] = random.randint(0, 90)

    # Sort selected horses by time
    sorted_horses = sorted(selected_horses, key=lambda x: x.get("Time", 0))

    # Display winning horses
    if sorted_horses:
        for i, horse in enumerate(sorted_horses[:3]):
            position = i + 1
            print(f"{position}st Place: {horse['horse_name']} - {horse.get('Time', 0)}s")
    else:
        print("No horses selected for the major round.")

def visualize_winning_horses(selected_horses):
    # Filter out horses without Time attribute
    horses_with_time = [horse for horse in selected_horses if "Time" in horse]

    # Sort horses by time in ascending order
    sorted_horses = sorted(horses_with_time, key=lambda x: x["Time"])

    # Display time chart for only the top 3 horses
    for i, horse in enumerate(sorted_horses[:3]):
        position = i + 1
        suffix = "st" if position == 1 else "nd" if position == 2 else "rd"  # Correct suffix for positions
        print(f"{horse['horse_name']}: {'*' * (horse['Time'] // 10)} {horse['Time']}s ({position}{suffix} Place)")

# Function to start the race
def start_race():
    global race_started
    race_started = True
    print("Race has started!")

# Main program loop
while True:

    print("Command Menu:")
    print("Type AHD for adding horse details.")
    print("Type UHD for updating horse details.")
    print("Type DHD for deleting horse details.")
    print("Type VHD for viewing the registered horses’ details table.")
    print("Type SHD for saving the horse details to the text file.")
    print("Type SDD for selecting four horses randomly for the major round.")
    print("Type WHD for displaying the Winning horses’ details.")
    print("Type VWH for Visualizing the time of the winning horses.")
    print("Type START to start the race.")
    print("Type ESC to exit the program.")

    user_input = input("Enter your choice: ")

    if user_input == "AHD":
        adding_horse_details()
    elif user_input == "DHD":
        deleting_horse_details()
    elif user_input == "UHD":
        update_horse_details()
    elif user_input == "VHD":
        view_horses_details()
    elif user_input == "SHD":
        save_horse_details()
    elif user_input == "SDD":
        selected_horses=select_for_major_round()
    elif user_input == "WHD":
        display_winning_horses(selected_horses)
    elif user_input == "VWH":
        visualize_winning_horses(selected_horses)
    elif user_input == "START":
        start_race()
    elif user_input == "ESC":
        print("Exiting the program!")
        break
    else:
        print("Invalid input. Please enter a valid command.")