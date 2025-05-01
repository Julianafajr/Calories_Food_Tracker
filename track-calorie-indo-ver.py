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
            print("\nBelum ada makanan yang tercatat.")
            return
        print("\n--- Analisis Kalori ---")
        highest_cal_meal = max(self.meals, key=lambda x: x["calories"])
        lowest_cal_meal = min(self.meals, key=lambda x: x["calories"])
        print(f"Makanan dengan Kalori Tertinggi: {highest_cal_meal['meal_name']} ({highest_cal_meal['calories']} kcal pada {highest_cal_meal['time']})")
        print(f"Makanan dengan Kalori Terendah: {lowest_cal_meal['meal_name']} ({lowest_cal_meal['calories']} kcal pada {lowest_cal_meal['time']})")
        print(f"Total Makanan yang Tercatat: {len(self.meals)}")

    def suggest_next_meal(self):
        remaining = self.remaining_calories()
        if remaining <= 0:
            print("\nSaran: Anda sudah melebihi batas kalori harian. Pertimbangkan untuk tidak menambah asupan.")
        else:
            print(f"\nSaran: Anda masih dapat mengkonsumsi sekitar {remaining} kcal untuk hari ini.")

    def summary(self):
        print("\n--- Ringkasan Kalori Harian ---")
        print(f"Tanggal: {self.timestamp.strftime('%Y-%m-%d')}")
        print(f"Tujuan Kalori Harian: {self.daily_goal} kcal")
        print(f"Total Kalori yang Terkonsumsi: {self.total_calories()} kcal")
        print(f"Kalori yang Tersisa: {self.remaining_calories()} kcal")
        if self.total_calories() > self.daily_goal:
            print("Peringatan: Anda telah melebihi tujuan kalori harian.")
        elif self.total_calories() < self.daily_goal:
            print("Anda masih memiliki kalori yang tersisa untuk dikonsumsi hari ini.")
        else:
            print("Selamat! Anda telah mencapai tujuan kalori harian dengan sempurna.")
        self.calorie_analysis()
        self.suggest_next_meal()

def main():
    try:
        daily_goal = float(input("Masukkan tujuan kalori harian Anda (dalam kcal): "))
        tracker = CalorieTracker(daily_goal)
        print("\n--- Makanan yang Sudah Ada ---")
        for meal in tracker.meals:
            print(f"{meal['meal_name']}: {meal['calories']} kcal pada {meal['time']}")
        print("\nMulailah mencatat makanan Anda. Ketik 'done' untuk selesai.\n")
        while True:
            meal_name = input("Masukkan nama makanan (atau ketik 'done' untuk selesai): ")
            if meal_name.lower() == 'done':
                break
            try:
                calories = float(input(f"Masukkan kalori untuk '{meal_name}': "))
                tracker.add_meal(meal_name, calories)
            except ValueError:
                print("Input tidak valid. Harap masukkan angka untuk kalori.")
        tracker.summary()
    except ValueError:
        print("Harap masukkan angka yang valid untuk tujuan kalori.")

if __name__ == "__main__":
    main()