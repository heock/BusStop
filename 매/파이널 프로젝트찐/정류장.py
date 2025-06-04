import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

# 전체 정류장 데이터 (확장됨)
stations = {
    "33121": {"name": "한경국립대학교 (강남역 방면)", "buses": ["4401", "8200", "8201", "8204"], "previous_station": None},
    "34151": {"name": "중앙대.롯데캐슬아파트 (강남역 방면)", "buses": ["4401", "8200", "8201", "8204"], "previous_station": "33121"},
    "33061": {"name": "대림동산 (강남역 방면)", "buses": ["4401", "8200", "8201", "8204"], "previous_station": "34151"},
    "33789": {"name": "공도시외버스정류장 (강남역 방면)", "buses": ["4401", "8200", "8201", "8204"], "previous_station": "33061"},
    "33018": {"name": "주은.풍림아파트 (강남역 방면)", "buses": ["4401", "8200", "8201", "8204"], "previous_station": "33789"},
    "22297": {"name": "매헌시민의숲.양재꽃시장 (강남역 방면)", "buses": ["4401"], "previous_station": "33018"},
    "22002": {"name": "말죽거리공원사거리(중) (강남역 방면)", "buses": ["4401"], "previous_station": "22297"},
    "22004": {"name": "양재역.서초문화예술회관(중) (강남역 방면)", "buses": ["4401"], "previous_station": "22002"},
    "22006": {"name": "뱅뱅사거리(중) (강남역 방면)", "buses": ["4401"], "previous_station": "22004"},
    "22008": {"name": "래미안아파트.파이낸셜뉴스(중) (강남역 방면)", "buses": ["4401"], "previous_station": "22006"},
    "22010": {"name": "신분당선강남역(중) (회차)", "buses": ["4401"], "previous_station": "22008"},
    "33017": {"name": "주은.풍림아파트 (한경대 방면)", "buses": ["4401"], "previous_station": "22010"},
    "33668": {"name": "공도시외버스정류장 (한경대 방면)", "buses": ["4401"], "previous_station": "33017"},
    "33060": {"name": "대림동산 (한경대 방면)", "buses": ["4401"], "previous_station": "33668"},
    "34157": {"name": "중앙대.롯데캐슬아파트 (한경대 방면)", "buses": ["4401"], "previous_station": "33060"},
    "33120": {"name": "한경국립대학교 (한경대 방면)", "buses": ["4401"], "previous_station": "34157"}
}

# 대기자 리스트 초기화
waiting_list = {
    sid: {bus: [] for bus in info["buses"]}
    for sid, info in stations.items()
}

# 사용자 ID 생성 함수
def make_user_id():
    now = datetime.now()
    return f"user_{now.timestamp()}"

class BusApp:
    def __init__(self, root):
        self.root = root
        self.root.title("버스 대기자 관리 시스템")

        # 선택 정보
        self.station_id = None
        self.bus_no = None
        self.user_id = None
        self.expire_time = None
        self.timer_job = None

        # UI 생성
        self.make_ui()

    def make_ui(self):
        tk.Label(self.root, text="정류장 번호 입력:").pack()
        self.entry_station = tk.Entry(self.root)
        self.entry_station.pack()

        tk.Button(self.root, text="정류장 확인", command=self.select_station).pack()

        self.selected_bus = tk.StringVar(self.root)
        self.menu_bus = tk.OptionMenu(self.root, self.selected_bus, ())
        self.menu_bus.pack()

        tk.Button(self.root, text="대기자 등록", command=self.register_user).pack()

        self.label_status = tk.Label(self.root, text="", font=("Arial", 14))
        self.label_status.pack(pady=10)

        self.label_timer = tk.Label(self.root, text="", font=("Arial", 12), fg="red")
        self.label_timer.pack()

        tk.Button(self.root, text="유효시간 연장 (10분)", command=self.extend_time).pack()

    def select_station(self):
        sid = self.entry_station.get().strip()
        if sid in stations:
            self.station_id = sid
            buses = stations[sid]["buses"]
            menu = self.menu_bus["menu"]
            menu.delete(0, "end")
            for bus in buses:
                menu.add_command(label=bus, command=tk._setit(self.selected_bus, bus))
            self.selected_bus.set(buses[0])
            messagebox.showinfo("확인", f"{stations[sid]['name']} 선택됨")
        else:
            messagebox.showerror("오류", "존재하지 않는 정류장 번호입니다.")

    def register_user(self):
        if not self.station_id or not self.selected_bus.get():
            messagebox.showwarning("주의", "정류장과 버스를 모두 선택하세요.")
            return

        self.bus_no = self.selected_bus.get()
        self.user_id = make_user_id()
        self.expire_time = datetime.now() + timedelta(minutes=15)

        waiting_list[self.station_id][self.bus_no].append({
            "user_id": self.user_id,
            "expire_time": self.expire_time
        })

        self.update_status()
        self.start_timer()

    def update_status(self):
        self.remove_expired_users()
        now = datetime.now()

        current = waiting_list[self.station_id][self.bus_no]
        current_users = [u for u in current if u["expire_time"] > now]
        current_count = len(current_users)

        prev_sid = stations[self.station_id]["previous_station"]
        prev_count = 0
        prev_name = "없음"
        if prev_sid and self.bus_no in waiting_list[prev_sid]:
            prev_users = waiting_list[prev_sid][self.bus_no]
            prev_users = [u for u in prev_users if u["expire_time"] > now]
            prev_count = len(prev_users)
            prev_name = stations[prev_sid]["name"]

        text = (
            f"정류장: {stations[self.station_id]['name']}\n"
            f"버스 번호: {self.bus_no}\n"
            f"현재 대기자 수: {current_count}명\n"
            f"이전 정류장: {prev_name} / 대기자 수: {prev_count}명"
        )
        self.label_status.config(text=text)

    def start_timer(self):
        if self.timer_job:
            self.root.after_cancel(self.timer_job)
        self.update_timer()

    def update_timer(self):
        now = datetime.now()
        if self.expire_time and self.expire_time > now:
            diff = self.expire_time - now
            minutes, seconds = divmod(diff.seconds, 60)
            self.label_timer.config(text=f"{minutes}분 {seconds}초 남음")
            self.timer_job = self.root.after(1000, self.update_timer)
        else:
            self.label_timer.config(text="만료됨")
            self.update_status()

    def extend_time(self):
        for user in waiting_list[self.station_id][self.bus_no]:
            if user["user_id"] == self.user_id:
                user["expire_time"] += timedelta(minutes=10)
                self.expire_time = user["expire_time"]
                self.start_timer()
                self.update_status()
                break

    def remove_expired_users(self):
        now = datetime.now()
        for sid in waiting_list:
            for bus in waiting_list[sid]:
                waiting_list[sid][bus] = [
                    user for user in waiting_list[sid][bus]
                    if user["expire_time"] > now
                ]

# 실행
root = tk.Tk()
app = BusApp(root)
root.mainloop()
