import tkinter as tk
from tkinter import Canvas, Frame, Button, BOTH, NW, TOP, BOTTOM, X
from PIL import Image, ImageTk
import os
import turtle

class MathApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Цифровий зошит")
        self.root.state('zoomed')
        self.root.configure(bg="#f4f4f4")

        self.current_color = "black"
        self.pen_size = 1.2
        self.last_x, self.last_y = None, None

        # --- ВЕРХНЯ ПАНЕЛЬ ---
        self.top_frame = Frame(root, bg="#ffffff", bd=1, relief="raised")
        self.top_frame.pack(side=TOP, fill=X, padx=5, pady=5)
               
        for i in range(1, 7):
            Button(self.top_frame, text=f"Завдання {i}", 
                   command=lambda n=i: self.load_task(f"task{n}.png"),
                   bg="#e8f0fe", fg="#1a73e8", width=12, height=2,
                   font=("Arial", 10, "bold"), relief="flat").pack(side="left", padx=10, pady=10)
        Button(self.top_frame, text="Пейзаж",command=self.draw_full_landscape,
                   bg="#e0f7fa", fg="#1a73e8", width=12, height=2,
                   font=("Arial", 10, "bold"), relief="flat").pack(side="left", padx=10, pady=10)

        # --- НИЖНЯ ПАНЕЛЬ ---
        self.bottom_frame = Frame(root, bg="#ffffff", bd=1, relief="raised")
        self.bottom_frame.pack(side=BOTTOM, fill=X, padx=5, pady=5)

        colors = [("Чорний", "black"), ("Червоний", "red"), ("Синій", "blue"), ("Зелений", "green")]
        for name, col in colors:
            Button(self.bottom_frame, text=name, bg=col, fg="white",
                   width=12, height=2, font=("Arial", 10, "bold"),
                   command=lambda c=col: self.set_color(c)).pack(side="left", padx=10, pady=10)

        Button(self.bottom_frame, text="Очистити", bg="#fce8e6", fg="#d93025",
               width=12, height=2, font=("Arial", 10, "bold"),
               command=self.clear_canvas).pack(side="right", padx=10)
        
        Button(self.bottom_frame, text="Вихід", bg="#f1f3f4",
               width=12, height=2, font=("Arial", 10, "bold"),
               command=root.quit).pack(side="right", padx=10)

        # --- ЦЕНТРАЛЬНЕ ПОЛОТНО ---
        self.canvas = Canvas(root, bg="white", highlightthickness=0, cursor="hand2")
        self.canvas.pack(fill=BOTH, expand=True, padx=5, pady=5)

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset_coords)

        self.tk_img = None
        self.root.update() 
        self.draw_grid()   
        self.load_task("task1.png")
    def draw_full_landscape(self):
        # 1. Імпортуємо вашу бібліотеку безпосередньо в методі
        import my_graphics
        import turtle
        
        # 2. Налаштовуємо вікно малювання
        screen = turtle.Screen()
        screen.setup(width=800, height=600)
        screen.title("Морський пейзаж з власної бібліотеки за шкільною програмою")
        
        t = turtle.Turtle()
        t.reset()
        t.speed(0)
        my_graphics.draw_waves(t, -440, -60, "cyan")
        my_graphics.draw_waves(t, -460, -20, "cyan")
        my_graphics.draw_custom_ship(t, 280, 200, size=0.3, p_color="red")
        my_graphics.draw_custom_ship(t, 380, -10, size=0.7, p_color="green")
        my_graphics.draw_custom_ship(t, -580, -10, size=0.5, p_color="green")
        my_graphics.draw_custom_ship(t, -300, -220, size=1.2, p_color="teal")
        my_graphics.draw_whale(t, -100, -10, size=0.7, color="navy")
        my_graphics.draw_whale(t, 99, -10, size=0.3, color="skyblue")
        my_graphics.draw_sun(t, -580, 250)
        my_graphics.draw_bird(t, -150, 200, size=0.5, color="black") 
        my_graphics.draw_bird(t, -180, 230, size=0.3, color="grey")  
        my_graphics.draw_bird(t, -210, 210, size=0.2, color="grey")  
        t.hideturtle()

    def draw_grid(self):
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        for i in range(0, w, 25):
            self.canvas.create_line(i, 0, i, h, fill="#e0e0e0", tags="grid")
        for i in range(0, h, 25):
            self.canvas.create_line(0, i, w, i, fill="#e0e0e0", tags="grid")

    def set_color(self, color): self.current_color = color
    def load_task(self, filename):
        if os.path.exists(filename):
            # 1. Відкриваємо малюнок і конвертуємо в RGBA (додаємо альфа-канал)
            img = Image.open(filename).convert("RGBA")
            img.thumbnail((900, 700)) 

            # 2. Змінюємо прозорість (0 - невидимий, 255 - повністю видимий)
            # Створимо новий малюнок з потрібною прозорістю
            new_data = []
            opacity = 100  # Чим менше число, тим прозоріша картинка (спробуйте від 50 до 150)
            
            for item in img.getdata():
                # Зберігаємо колір (item[0,1,2]), але міняємо прозорість (item[3])
                # Якщо піксель не прозорий, ставимо йому наше значення opacity
                if item[3] > 0:
                    new_data.append((item[0], item[1], item[2], opacity))
                else:
                    new_data.append(item)
            
            img.putdata(new_data)
            
            # 3. Відображаємо оброблений малюнок
            self.tk_img = ImageTk.PhotoImage(img)
            self.clear_canvas() 
            self.canvas.delete("image_bg")
            self.canvas.create_image(5, 5, anchor=NW, image=self.tk_img, tags="image_bg")
            
            # Важливо: щоб лінійка була ПОВЕРХ малюнка, піднімаємо її
            self.canvas.tag_raise("grid")

    def paint(self, event):
        if self.last_x and self.last_y:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y,
                                   fill=self.current_color, width=self.pen_size, 
                                   capstyle=tk.ROUND, smooth=tk.TRUE, tags="drawing")
        self.last_x, self.last_y = event.x, event.y

    def reset_coords(self, event): self.last_x = self.last_y = None

    def clear_canvas(self): self.canvas.delete("drawing")

if __name__ == "__main__":
    root = tk.Tk()
    app = MathApp(root)
    root.mainloop()
