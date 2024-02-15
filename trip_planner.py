from tkinter import Tk, Label, Entry, Button, OptionMenu, StringVar
from datetime import datetime

destinations = {
    "Delhi": {
        "name": "Delhi",
        "places_to_visit": ["Red Fort", "Qutub Minar", "India Gate"],
        "activities": ["Heritage Walk", "Street Food Tour", "Shopping in Chandni Chowk"],
        "accommodations": ["Luxury Hotel", "Budget Guesthouse", "Homestay"],
        "transportation_options": ["Local Metro", "Rental Car", "Auto Rickshaw"],
    },
    "Mumbai": {
        "name": "Mumbai",
        "places_to_visit": ["Gateway of India", "Marine Drive", "Elephanta Caves"],
        "activities": ["Bollywood Studio Tour", "Beach Hopping", "Shopping in Colaba"],
        "accommodations": ["Beachfront Resort", "City Hotel", "Hostel"],
        "transportation_options": ["Local Train", "Taxi", "Mumbai Metro"],
    },
    "Jaipur": {
        "name": "Jaipur",
        "places_to_visit": ["Amber Fort", "Hawa Mahal", "City Palace"],
        "activities": ["Elephant Ride at Amber Fort", "Hot Air Balloon Ride", "Rajasthani Folk Dance Show"],
        "accommodations": ["Heritage Haveli", "Palace Hotel", "Guesthouse"],
        "transportation_options": ["Local Rickshaw", "Private Car", "Horse Carriage"],
    },
    "Hyderabad": {
                "name": "Hyderabad",
                "places_to_visit": ["Charminar", "Birlamandir", "Hussain Sagar"],
                "activities": ["Zoo Park","Wondarla water park","Ramoji filimcity"],
                "accommodations": ["Swagath Grand Hotel","paradise Hotel","Guesthouse"],
                "transportation_options": ["Govt. Bus","Hyd Metro","Pre-paid Taxi"]            
    }
}

def trip_planner():
    destination_choice = destination_var.get()

    if destination_choice not in destinations:
        result_label.config(text="Invalid destination choice!")
        return

    destination = destinations[destination_choice]
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()

    # Convert input dates to datetime objects
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    # Calculate the trip duration
    trip_duration = (end_date - start_date).days + 1

    # Calculate additional costs
    room_price_per_day = 50
    food_price_per_person_per_day = 20
    travel_price = 100 + (trip_duration * 50)  # Assuming $100 for initial travel cost + $50 per day for travel
    room_cost = trip_duration * room_price_per_day
    food_cost = trip_duration * len(destination["places_to_visit"]) * food_price_per_person_per_day

    result_label.config(text="\n--- Trip Itinerary ---\n"
                             f"Destination: {destination['name']}\n"
                             f"Start Date: {start_date.strftime('%Y-%m-%d')}\n"
                             f"End Date: {end_date.strftime('%Y-%m-%d')}\n"
                             f"Duration: {trip_duration} days\n"
                             "\nPlaces to visit:\n" +
                             "\n".join(f"- {place}" for place in destination["places_to_visit"]) +
                             "\n\nAdditional Costs:\n" +
                             f"Travel Cost: ${travel_price}\n"
                             f"Room Cost: ${room_cost}\n"
                             f"Food Cost: ${food_cost}\n"
                             f"\nTotal Cost: ${travel_price + room_cost + food_cost}\n" +
                             "\n--- Additional Features ---\n"
                             "Suggested Activities:\n" +
                             "\n".join(f"- {activity}" for activity in destination["activities"]) +
                             "\n\nAccommodation Options:\n" +
                             "\n".join(f"- {accommodation}" for accommodation in destination["accommodations"]) +
                             "\n\nTransportation Options:\n" +
                             "\n".join(f"- {transportation_option}" for transportation_option in destination["transportation_options"]))

# Create GUI window
window = Tk()
window.title("Trip Planner")
window.configure(background="#E6E6FA")

# Destination selection
destination_label = Label(window, text="Select a destination:", background="#E6E6FA")
destination_label.grid(row=0, column=0, padx=10, pady=5, sticky="W")

destination_var = StringVar(window)
destination_var.set("Delhi")  # Set default value

destination_optionmenu = OptionMenu(window, destination_var, *destinations.keys())
destination_optionmenu.grid(row=0, column=1, padx=10, pady=5)

# Start date input
start_date_label = Label(window, text="Start Date (YYYY-MM-DD):", background="#E6E6FA")
start_date_label.grid(row=1, column=0, padx=10, pady=5, sticky="W")

start_date_entry = Entry(window)
start_date_entry.grid(row=1, column=1, padx=10, pady=5)

# End date input
end_date_label = Label(window, text="End Date (YYYY-MM-DD):", background="#E6E6FA")
end_date_label.grid(row=2, column=0, padx=10, pady=5, sticky="W")

end_date_entry = Entry(window)
end_date_entry.grid(row=2, column=1, padx=10, pady=5)

# Calculate button
calculate_button = Button(window, text="Calculate", command=trip_planner, background="#8B008B", foreground="white")
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Result label
result_label = Label(window, text="", background="#E6E6FA", wraplength=400)
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
window.mainloop()