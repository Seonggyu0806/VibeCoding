import tkinter as tk
from tkinter import messagebox
import math
import random

class CustomRoulette:
    def __init__(self, root):
        self.root = root
        self.root.title("돌림판")
        self.root.geometry("750x550")
        self.root.configure(bg="#F8F9FA")
        
        self.options = []
        # 선명한 8가지 색상 고정
        self.colors = ["#1AFFF0", "#75FA61", "#7E84F7", "#FFFE91", "#FF33A8", "#507F80", "#75163F", "#F08650"]
        self.angle = 0
        self.is_spinning = False

        # --- 레이아웃 설정 ---
        self.left_frame = tk.Frame(root, padx=20, pady=20, bg="#F8F9FA")
        self.left_frame.pack(side="left", fill="y")
        self.right_frame = tk.Frame(root, padx=20, pady=20, bg="white")
        self.right_frame.pack(side="right", expand=True, fill="both")

        # --- 왼쪽 UI (입력 및 제한 표시) ---
        tk.Label(self.left_frame, text="항목 입력 (최대 8개)", font=("Malgun Gothic", 11, "bold"), bg="#F8F9FA").pack()
        self.entry = tk.Entry(self.left_frame, width=20, font=("Malgun Gothic", 11))
        self.entry.pack(pady=5)
        self.entry.bind("<Return>", lambda event: self.add_option())

        # 추가 버튼
        tk.Button(self.left_frame, text="추가하기", command=self.add_option, bg="#A1FB8E", relief="flat").pack(fill="x")
        
        # 개수 표시 레이블
        self.count_label = tk.Label(self.left_frame, text="현재 항목: 0 / 8", fg="blue", bg="#F8F9FA")
        self.count_label.pack(pady=5)

        self.listbox = tk.Listbox(self.left_frame, height=10, font=("Malgun Gothic", 10))
        self.listbox.pack(pady=5)
        
        tk.Button(self.left_frame, text="선택 삭제", command=self.delete_option, bg="#FFCCCC", relief="flat").pack(fill="x")
        tk.Button(self.left_frame, text="전체 초기화", command=self.reset_options, bg="#DDDDDD", relief="flat").pack(fill="x", pady=5)

        # --- 오른쪽 UI (캔버스 및 메인 버튼) ---
        self.canvas = tk.Canvas(self.right_frame, width=420, height=400, bg="white", highlightthickness=0)
        self.canvas.pack()
        
        # [수정] 가시성을 극대화한 황금색 대형 버튼
        self.spin_btn = tk.Button(
            self.right_frame, 
            text="🔥 지금 바로 돌리기! 🔥", 
            font=("Malgun Gothic", 20, "bold"), 
            bg="#FFD700",      # 황금색
            fg="black",        # 검정 글씨로 가독성 확보
            activebackground="#FFA500", 
            relief="raised",    
            bd=8,               
            cursor="hand2",     
            command=self.spin
        )
        self.spin_btn.pack(fill="x", padx=30, pady=20)

        # 버튼 호버 효과
        self.spin_btn.bind("<Enter>", lambda e: self.spin_btn.config(bg="#FFF000"))
        self.spin_btn.bind("<Leave>", lambda e: self.spin_btn.config(bg="#FFD700"))

        self.draw_wheel(0)

    def update_count(self):
        self.count_label.config(text=f"현재 항목: {len(self.options)} / 8")

    def add_option(self):
        # [핵심] 8개 제한 로직
        if len(self.options) >= 8:
            messagebox.showwarning("제한", "항목은 최대 8개까지만 추가할 수 있습니다!")
            return

        text = self.entry.get().strip()
        if text:
            self.options.append(text)
            self.listbox.insert(tk.END, text)
            self.entry.delete(0, tk.END)
            self.update_count()
            self.draw_wheel(self.angle)
        else:
            messagebox.showwarning("경고", "항목을 입력해주세요!")

    def delete_option(self):
        try:
            index = self.listbox.curselection()[0]
            self.options.pop(index)
            self.listbox.delete(index)
            self.update_count()
            self.draw_wheel(self.angle)
        except IndexError:
            messagebox.showwarning("경고", "삭제할 항목을 선택해주세요.")

    def reset_options(self):
        self.options = []
        self.listbox.delete(0, tk.END)
        self.angle = 0
        self.update_count()
        self.draw_wheel(0)

    def draw_wheel(self, offset):
        self.canvas.delete("all")
        n = len(self.options)
        
        if n == 0:
            self.canvas.create_oval(60, 50, 360, 350, outline="#ddd", width=2)
            self.canvas.create_text(210, 200, text="항목을 추가해주세요", fill="gray")
            return

        if n == 1:
            self.canvas.create_oval(60, 50, 360, 350, fill=self.colors[0], outline="white", width=2)
            self.canvas.create_text(210, 200, text=self.options[0], font=("Malgun Gothic", 13, "bold"))
        else:
            arc_angle = 360 / n
            for i in range(n):
                start = i * arc_angle + offset
                self.canvas.create_arc(60, 50, 360, 350, start=start, extent=arc_angle, 
                                       fill=self.colors[i % len(self.colors)], outline="white", width=2)
                
                rad = math.radians(start + arc_angle/2)
                x, y = 210 + 100 * math.cos(rad), 200 - 100 * math.sin(rad)
                
                curr_angle = (start + arc_angle/2) % 360
                self.canvas.create_text(x, y, text=self.options[i], font=("Malgun Gothic", 10, "bold"),
                                        angle=curr_angle if not (90 < curr_angle < 270) else curr_angle+180)

        # 화살표
        self.canvas.create_polygon(370, 200, 410, 180, 410, 220, fill="red", outline="black", width=2)

    def spin(self):
        if len(self.options) < 2:
            messagebox.showwarning("알림", "최소 2개 이상의 항목이 필요합니다.")
            return
        if not self.is_spinning:
            self.is_spinning = True
            self.spin_btn.config(state="disabled", text="두구두구두구...", bg="#CCCCCC")
            # 긴장감을 위해 마찰력 애니메이션 적용
            speed = random.uniform(40, 60)
            friction = random.uniform(0.97, 0.985)
            self.animate(speed, friction)

    def animate(self, speed, friction):
        if speed > 0.05:
            self.angle = (self.angle + speed) % 360
            self.draw_wheel(self.angle)
            next_call = 20 if speed >= 2 else 35
            self.root.after(next_call, lambda: self.animate(speed * friction, friction))
        else:
            self.is_spinning = False
            self.spin_btn.config(state="normal", text="🔥 지금 바로 돌리기! 🔥", bg="#FFD700")
            self.show_result()

    def show_result(self):
        n = len(self.options)
        final_angle = (360 - (self.angle % 360)) % 360
        idx = int(final_angle / (360 / n))
        messagebox.showinfo("🎊 당첨! 🎊", f"결과: 【 {self.options[idx]} 】")

if __name__ == "__main__":
    root = tk.Tk()
    app = CustomRoulette(root)
    root.mainloop()