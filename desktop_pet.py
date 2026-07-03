import tkinter as tk
import random
import math
import time


class DesktopPet:
    """A lightweight desktop pet built with Tkinter only."""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Desktop Pet")
        self.root.geometry("220x220+800+420")
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)

        self.transparent_color = "#ff00ff"
        self.root.configure(bg=self.transparent_color)
        try:
            self.root.wm_attributes("-transparentcolor", self.transparent_color)
        except tk.TclError:
            pass

        self.canvas = tk.Canvas(
            self.root,
            width=220,
            height=220,
            bg=self.transparent_color,
            highlightthickness=0,
        )
        self.canvas.pack(fill="both", expand=True)

        self.drag_start_x = 0
        self.drag_start_y = 0
        self.mood = "happy"
        self.frame = 0
        self.sleeping = False
        self.bubble_id = None
        self.bubble_text_id = None

        self.messages = [
            "今天也要加油呀～",
            "记得喝水！",
            "我在陪你工作 🐾",
            "点我一下看看？",
            "今天要不要早点休息？",
            "主人，我饿啦～",
        ]

        self.root.bind("<ButtonPress-1>", self.start_drag)
        self.root.bind("<B1-Motion>", self.drag)
        self.root.bind("<Button-1>", self.on_click)
        self.root.bind("<Button-3>", self.show_menu)

        self.menu = tk.Menu(self.root, tearoff=0)
        self.menu.add_command(label="喂食 Feed", command=self.feed)
        self.menu.add_command(label="玩耍 Play", command=self.play)
        self.menu.add_command(label="睡觉 Sleep / Wake", command=self.toggle_sleep)
        self.menu.add_separator()
        self.menu.add_command(label="隐藏 5 秒 Hide", command=self.hide_temporarily)
        self.menu.add_command(label="退出 Quit", command=self.root.destroy)

        self.draw_pet()
        self.animate()
        self.random_talk()

    def start_drag(self, event):
        self.drag_start_x = event.x
        self.drag_start_y = event.y

    def drag(self, event):
        x = self.root.winfo_x() + event.x - self.drag_start_x
        y = self.root.winfo_y() + event.y - self.drag_start_y
        self.root.geometry(f"+{x}+{y}")

    def on_click(self, event):
        self.sleeping = False
        self.mood = random.choice(["happy", "excited", "love"])
        self.say(random.choice(["嘿嘿～", "你点到我啦！", "继续努力！", "我喜欢这里～"]))

    def show_menu(self, event):
        self.menu.tk_popup(event.x_root, event.y_root)

    def feed(self):
        self.sleeping = False
        self.mood = "happy"
        self.say("好吃！谢谢主人 🍪")

    def play(self):
        self.sleeping = False
        self.mood = "excited"
        self.say("一起玩！")

    def toggle_sleep(self):
        self.sleeping = not self.sleeping
        self.mood = "sleepy" if self.sleeping else "happy"
        self.say("Zzz..." if self.sleeping else "我醒啦～")

    def hide_temporarily(self):
        self.root.withdraw()
        self.root.after(5000, self.root.deiconify)

    def say(self, text, duration=2600):
        self.clear_bubble()
        self.bubble_id = self.canvas.create_round_rect(
            20,
            8,
            200,
            52,
            radius=16,
            fill="white",
            outline="#444",
            width=2,
        )
        self.bubble_text_id = self.canvas.create_text(
            110,
            30,
            text=text,
            fill="#222",
            font=("Microsoft YaHei", 11, "bold"),
            width=160,
        )
        self.root.after(duration, self.clear_bubble)

    def clear_bubble(self):
        if self.bubble_id:
            self.canvas.delete(self.bubble_id)
            self.bubble_id = None
        if self.bubble_text_id:
            self.canvas.delete(self.bubble_text_id)
            self.bubble_text_id = None

    def random_talk(self):
        if not self.sleeping and random.random() < 0.7:
            self.say(random.choice(self.messages), duration=3000)
        self.root.after(random.randint(9000, 17000), self.random_talk)

    def draw_pet(self):
        self.canvas.delete("pet")
        bob = math.sin(self.frame / 8) * 4
        ear_wiggle = math.sin(self.frame / 6) * 3

        self.canvas.create_oval(58, 178, 162, 198, fill="#bdbdbd", outline="", tags="pet")
        self.canvas.create_arc(
            132,
            108 + bob,
            202,
            172 + bob,
            start=25,
            extent=230,
            style="arc",
            outline="#7a4b2a",
            width=8,
            tags="pet",
        )
        self.canvas.create_oval(55, 78 + bob, 165, 185 + bob, fill="#f5b35c", outline="#5d351e", width=3, tags="pet")
        self.canvas.create_oval(78, 115 + bob, 142, 178 + bob, fill="#ffe1aa", outline="", tags="pet")
        self.canvas.create_oval(48, 54 + bob, 172, 152 + bob, fill="#f5b35c", outline="#5d351e", width=3, tags="pet")

        self.canvas.create_polygon(
            62,
            68 + bob,
            42 + ear_wiggle,
            28 + bob,
            86,
            55 + bob,
            fill="#f5b35c",
            outline="#5d351e",
            width=3,
            tags="pet",
        )
        self.canvas.create_polygon(
            158,
            68 + bob,
            178 - ear_wiggle,
            28 + bob,
            134,
            55 + bob,
            fill="#f5b35c",
            outline="#5d351e",
            width=3,
            tags="pet",
        )
        self.canvas.create_polygon(63, 61 + bob, 52, 39 + bob, 79, 55 + bob, fill="#ffcfcb", outline="", tags="pet")
        self.canvas.create_polygon(157, 61 + bob, 168, 39 + bob, 141, 55 + bob, fill="#ffcfcb", outline="", tags="pet")

        paw_offset = math.sin(self.frame / 5) * 2 if self.mood == "excited" else 0
        self.canvas.create_oval(68, 162 + bob + paw_offset, 98, 190 + bob, fill="#f09d49", outline="#5d351e", width=2, tags="pet")
        self.canvas.create_oval(122, 162 + bob - paw_offset, 152, 190 + bob, fill="#f09d49", outline="#5d351e", width=2, tags="pet")

        if self.sleeping or self.mood == "sleepy":
            self.canvas.create_arc(78, 95 + bob, 98, 108 + bob, start=0, extent=180, style="arc", width=3, tags="pet")
            self.canvas.create_arc(122, 95 + bob, 142, 108 + bob, start=0, extent=180, style="arc", width=3, tags="pet")
            self.canvas.create_text(150, 72 + bob, text="Z", font=("Arial", 14, "bold"), fill="#444", tags="pet")
            self.canvas.create_text(165, 55 + bob, text="z", font=("Arial", 11, "bold"), fill="#444", tags="pet")
        elif self.mood == "love":
            self.canvas.create_text(88, 100 + bob, text="♥", font=("Arial", 20, "bold"), fill="#d94b6a", tags="pet")
            self.canvas.create_text(132, 100 + bob, text="♥", font=("Arial", 20, "bold"), fill="#d94b6a", tags="pet")
        else:
            eye_size = 8 if self.mood == "happy" else 10
            self.canvas.create_oval(80, 92 + bob, 80 + eye_size, 100 + bob + eye_size, fill="#222", outline="", tags="pet")
            self.canvas.create_oval(130, 92 + bob, 130 + eye_size, 100 + bob + eye_size, fill="#222", outline="", tags="pet")
            self.canvas.create_oval(83, 94 + bob, 86, 97 + bob, fill="white", outline="", tags="pet")
            self.canvas.create_oval(133, 94 + bob, 136, 97 + bob, fill="white", outline="", tags="pet")

        self.canvas.create_oval(104, 108 + bob, 116, 117 + bob, fill="#4b2d1f", outline="", tags="pet")
        if self.mood == "excited":
            self.canvas.create_arc(92, 114 + bob, 128, 140 + bob, start=200, extent=140, style="arc", width=3, tags="pet")
            self.canvas.create_oval(103, 125 + bob, 117, 139 + bob, fill="#ff7a7a", outline="", tags="pet")
        else:
            self.canvas.create_arc(98, 114 + bob, 110, 126 + bob, start=260, extent=130, style="arc", width=2, tags="pet")
            self.canvas.create_arc(110, 114 + bob, 122, 126 + bob, start=150, extent=130, style="arc", width=2, tags="pet")

        self.canvas.create_oval(63, 116 + bob, 82, 128 + bob, fill="#ffb1a7", outline="", tags="pet")
        self.canvas.create_oval(138, 116 + bob, 157, 128 + bob, fill="#ffb1a7", outline="", tags="pet")

    def animate(self):
        self.frame += 1
        self.draw_pet()
        if self.bubble_id and self.bubble_text_id:
            self.canvas.tag_raise(self.bubble_id)
            self.canvas.tag_raise(self.bubble_text_id)
        self.root.after(80 if self.mood == "excited" else 120, self.animate)

    def run(self):
        self.root.mainloop()


def add_round_rect_to_canvas():
    def create_round_rect(self, x1, y1, x2, y2, radius=25, **kwargs):
        points = [
            x1 + radius,
            y1,
            x2 - radius,
            y1,
            x2,
            y1,
            x2,
            y1 + radius,
            x2,
            y2 - radius,
            x2,
            y2,
            x2 - radius,
            y2,
            x1 + radius,
            y2,
            x1,
            y2,
            x1,
            y2 - radius,
            x1,
            y1 + radius,
            x1,
            y1,
        ]
        return self.create_polygon(points, smooth=True, **kwargs)

    tk.Canvas.create_round_rect = create_round_rect


if __name__ == "__main__":
    add_round_rect_to_canvas()
    DesktopPet().run()
