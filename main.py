import tkinter as tk
import random

PASSWORD = "$lith3r"
SNAKE_FACTS = [
    "Snakes are cool",
    "Pythons are a type of snake",
    "Snake have vestigial legs",
    "Some snakes have venom",
    "Not all snakes are venomous",
    "Snakes are reptiles",
    "Snakes are carnivores",
]
success = False


class AdvertisementSpam(tk.Frame):
    def __init__(self, root, images):
        tk.Frame.__init__(self, root)
        self.images = images
        self.password_label = tk.Label(self, text="Enter password to continue")
        self.password_label.pack(side="top", pady=(20, 10))
        self.input_box = tk.Entry(self, show="*")
        self.input_box.pack(side="top", pady=(0, 20), padx=20)
        self.input_box.bind(
            "<Return>", lambda _: self.check_password(self.input_box.get())
        )
        width = 200
        height = 100
        total_width = root.winfo_screenwidth()
        total_height = root.winfo_screenheight()
        # display in center
        root.geometry(
            f"{width}x{height}+{int((total_width - width) / 2)}+{int((total_height - height) / 2)}"
        )
        self.new_window(self.images[0])

    def check_password(self, password):
        global success
        if password == PASSWORD:
            success = True
            self.quit()
        else:
            self.input_box.delete(0, "end")
            self.password_label.config(text="Wrong password, try again")
            self.new_window(random.choice(self.images))

    def new_window(self, image):
        window = tk.Toplevel(self)
        x_max = root.winfo_screenwidth() - image.width()
        y_max = root.winfo_screenheight() - image.height()
        window.geometry(
            f"{image.width()}x{image.height()}+{random.randint(0, x_max)}+{random.randint(0, y_max)}"
        )
        label = tk.Label(window, image=image)
        label.grid(row=0, column=0)

        window.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(window))

    def on_closing(self, window):
        window.destroy()
        first = random.choice(self.images)
        self.new_window(first)
        self.new_window(random.choice(list(img for img in self.images if img != first)))


if __name__ == "__main__":
    print("Welcome to the snake fact program!")
    print("Before we begin, you must authenticate yourself")
    input("Press enter to continue...")
    root = tk.Tk()
    images = [
        tk.PhotoImage(file=f"images/snake-ad-{image_id}.png") for image_id in range(3)
    ]

    AdvertisementSpam(root, images).pack(side="top", fill="both", expand=True)
    root.mainloop()
    if not success:
        print("You have not been authenticated!")
        exit(1)
    print("You have been authenticated!")
    print("Time for a snake fact!")
    print(random.choice(SNAKE_FACTS))
    print("Run again for more snake facts!")
