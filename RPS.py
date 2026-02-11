import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("파이썬 가위바위보")
        self.root.geometry("500x620")
        
        self.wins, self.draws, self.losses = 0, 0, 0
        self.options = ["가위", "바위", "보"]
        self.shapes = {"가위": "✌️", "바위": "✊", "보": "✋"}
        self.is_playing = False 

        # --- UI 구성 ---
        tk.Label(root, text="[ 가위 바위 보 무한 대결 ]", font=("맑은 고딕", 18, "bold")).pack(pady=20)

        display_frame = tk.Frame(root, relief="sunken", bd=2, padx=20, pady=20)
        display_frame.pack(pady=10)

        self.user_disp = tk.Label(display_frame, text="내 선택\n❓", font=("맑은 고딕", 20))
        self.user_disp.grid(row=0, column=0, padx=30)

        tk.Label(display_frame, text="VS", font=("맑은 고딕", 25, "bold")).grid(row=0, column=1)

        self.com_disp = tk.Label(display_frame, text="컴퓨터 선택\n❓", font=("맑은 고딕", 20))
        self.com_disp.grid(row=0, column=2, padx=30)

        self.label_status = tk.Label(root, text="버튼을 눌러 대결하세요!", font=("맑은 고딕", 18, "bold"), fg="darkblue")
        self.label_status.pack(pady=20)

        self.label_score = tk.Label(root, text="현재 전적: 0승 0무 0패", font=("맑은 고딕", 12, "bold"))
        self.label_score.pack(pady=5)

        # 게임 버튼 영역
        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack(pady=20)

        for choice in self.options:
            tk.Button(self.btn_frame, text=choice, width=10, height=2, font=("맑은 고딕", 11),
                      command=lambda c=choice: self.start_animation(c)).pack(side="left", padx=10)

        # --- 나가기 버튼 추가 ---
        self.exit_btn = tk.Button(root, text="게임 종료 및 결과 보기", width=25, height=2, 
                                  bg="#f44336", fg="white", font=("맑은 고딕", 10, "bold"),
                                  command=self.show_final_result)
        self.exit_btn.pack(pady=30)

    def start_animation(self, user_choice):
        if self.is_playing: return 
        self.is_playing = True
        self.user_disp.config(text=f"내 선택\n{self.shapes[user_choice]}", fg="blue")
        self.label_status.config(text="컴퓨터가 고민 중...", fg="orange")
        self.animate_computer(user_choice, 0)

    def animate_computer(self, user_choice, count):
        if count < 10:
            temp_choice = random.choice(self.options)
            self.com_disp.config(text=f"컴퓨터 선택\n{self.shapes[temp_choice]}", fg="red")
            self.root.after(80, lambda: self.animate_computer(user_choice, count + 1))
        else:
            self.final_result(user_choice)

    def final_result(self, user_choice):
        computer_choice = random.choice(self.options)
        self.com_disp.config(text=f"컴퓨터 선택\n{self.shapes[computer_choice]}", fg="red")

        if user_choice == computer_choice:
            msg, color = "🤝 무승부입니다!", "gray"
            self.draws += 1
        elif (user_choice == "가위" and computer_choice == "보") or \
             (user_choice == "바위" and computer_choice == "가위") or \
             (user_choice == "보" and computer_choice == "바위"):
            msg, color = "🎉 승리했습니다!", "green"
            self.wins += 1
        else:
            msg, color = "🤖 패배했습니다...", "red"
            self.losses += 1

        self.label_status.config(text=msg, fg=color)
        self.label_score.config(text=f"현재 전적: {self.wins}승 {self.draws}무 {self.losses}패")
        self.is_playing = False

    def show_final_result(self):
        # 최종 승패 계산 및 메시지 구성
        total_games = self.wins + self.draws + self.losses
        if total_games == 0:
            messagebox.showinfo("종료", "한 판도 안 하시고 가시다니 아쉬워요! 수고하셨습니다.")
        else:
            result_summary = (
                f"--- 최종 전적 ---\n"
                f"승리: {self.wins}회\n"
                f"무승부: {self.draws}회\n"
                f"패배: {self.losses}회\n\n"
                f"수고하셨습니다!"
            )
            messagebox.showinfo("게임 종료", result_summary)
        
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()