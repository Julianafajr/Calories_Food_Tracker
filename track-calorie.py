import datetime

class CalorieTracker:
    def __init__(self, daily_goal):
        self.daily_goal = daily_goal
        self.meals = [
            {"meal_name": "Sarapan", "calories": 350, "time": "08:00:00"},
            {"meal_name": "Makan Siang", "calories": 600, "time": "12:30:00"},
            {"meal_name": "Snack", "calories": 150, "time": "15:00:00"}
        ]
        self.timestamp = datetime.datetime.now()

    def add_meal(self, meal_name, calories):
        meal = {
            "meal_name": meal_name,
            "calories": calories,
            "time": datetime.datetime.now().strftime("%H:%M:%S")
        }
        self.meals.append(meal)

    def total_calories(self):
        return sum(meal["calories"] for meal in self.meals)

    def remaining_calories(self):
        return self.daily_goal - self.total_calories()

    def calorie_analysis(self):
        if not self.meals:
            print("\nNo meals recorded yet.")
            return

        print("\n--- Calorie Analysis ---")
        highest_cal_meal = max(self.meals, key=lambda x: x["calories"])
        lowest_cal_meal = min(self.meals, key=lambda x: x["calories"])
        
        print(f"Highest Calorie Meal: {highest_cal_meal['meal_name']} ({highest_cal_meal['calories']} kcal at {highest_cal_meal['time']})")
        print(f"Lowest Calorie Meal: {lowest_cal_meal['meal_name']} ({lowest_cal_meal['calories']} kcal at {lowest_cal_meal['time']})")
        print(f"Total Meals Recorded: {len(self.meals)}")

    def suggest_next_meal(self):
        remaining = self.remaining_calories()
        if remaining <= 0:
            print("\nSuggestion: You have no remaining calories. Consider avoiding more intake.")
        else:
            print(f"\nSuggestion: You can still consume approximately {remaining} kcal for the day.")

    def summary(self):
        print("\n--- Daily Calorie Summary ---")
        print(f"Date: {self.timestamp.strftime('%Y-%m-%d')}")
        print(f"Daily Calorie Goal: {self.daily_goal} kcal")
        print(f"Total Calories Consumed: {self.total_calories()} kcal")
        print(f"Remaining Calories: {self.remaining_calories()} kcal")

        if self.total_calories() > self.daily_goal:
            print("Warning: You have exceeded your daily calorie goal.")
        elif self.total_calories() < self.daily_goal:
            print("You still have calories left to consume today.")
        else:
            print("Great job! You've met your daily calorie goal perfectly.")

        self.calorie_analysis()
        self.suggest_next_meal()

def main():
    try:
        daily_goal = float(input("Enter your daily calorie goal (in kcal): "))
        tracker = CalorieTracker(daily_goal)

        print("\n--- Existing Meals ---")
        for meal in tracker.meals:
            print(f"{meal['meal_name']}: {meal['calories']} kcal at {meal['time']}")

        print("\nStart logging your meals. Enter 'done' to finish.\n")

        while True:
            meal_name = input("Enter meal name (or type 'done' to finish): ")
            if meal_name.lower() == 'done':
                break
            
            try:
                calories = float(input(f"Enter calories for '{meal_name}': "))
                tracker.add_meal(meal_name, calories)
            except ValueError:
                print("Invalid input. Please enter a numeric value for calories.")

        tracker.summary()

    except ValueError:
        print("Please enter a valid number for the calorie goal.")

if __name__ == "__main__":
    main()
