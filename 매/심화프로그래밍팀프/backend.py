from flask import Flask, request, jsonify, render_template_string
from datetime import datetime, timedelta
import threading
import time

app = Flask(__name__)

# 예시 데이터
stations = {
    "34151": {
        "name": "중대앞 버스정류장",
        "buses": ["4401", "8200", "8201", "8204"]
    }
}

# 대기자 리스트
waiting_data = {
    "34151": {bus: [] for bus in stations["34151"]["buses"]}
}

@app.route("/")
def index():
    return render_template_string(open("index.html").read())

# 정류장 정보 가져오기
@app.route("/api/get_station", methods=["POST"])
def get_station():
    data = request.json
    station_id = data.get("station_id")
    station = stations.get(station_id)
    if not station:
        return jsonify({"error": "정류장 없음"}), 404
    return jsonify({
        "name": station["name"],
        "buses": station["buses"]
    })

# 대기자 등록
@app.route("/api/tag", methods=["POST"])
def tag():
    data = request.json
    station_id = data["station_id"]
    bus_no = data["bus_no"]
    user_id = data["user_id"]

    now = datetime.now()
    expire_time = now + timedelta(minutes=15)

    waiting_data[station_id][bus_no].append({
        "user_id": user_id,
        "expire_time": expire_time
    })

    previous_count = len(waiting_data[station_id][bus_no])

    return jsonify({
        "message": f"{user_id}님, 대기 등록 완료!",
        "position": len(waiting_data[station_id][bus_no]),
        "previous_count": previous_count,
        "expire_time": expire_time.strftime("%H:%M:%S")
    })

# 상태 조회
@app.route("/api/status", methods=["POST"])
def status():
    data = request.json
    station_id = data["station_id"]
    bus_no = data["bus_no"]

    now = datetime.now()
    valid_waiting = [
        d for d in waiting_data[station_id][bus_no]
        if d["expire_time"] > now
    ]
    return jsonify({
        "count": len(valid_waiting),
        "expire_times": [d["expire_time"].strftime("%H:%M:%S") for d in valid_waiting]
    })

# 유효시간 연장
@app.route("/api/extend", methods=["POST"])
def extend():
    data = request.json
    station_id = data["station_id"]
    bus_no = data["bus_no"]
    user_id = data["user_id"]

    for d in waiting_data[station_id][bus_no]:
        if d["user_id"] == user_id:
            d["expire_time"] += timedelta(minutes=10)
            return jsonify({
                "message": "유효시간 10분 연장 완료!",
                "new_expire": d["expire_time"].strftime("%H:%M:%S")
            })

    return jsonify({"error": "사용자 정보 없음"}), 404

# 만료된 대기자 정리
def cleanup():
    while True:
        now = datetime.now()
        for station_id in waiting_data:
            for bus_no in waiting_data[station_id]:
                waiting_data[station_id][bus_no] = [
                    d for d in waiting_data[station_id][bus_no] if d["expire_time"] > now
                ]
        time.sleep(60)  # 1분 간격으로 정리

# 클린업 스레드 시작
cleanup_thread = threading.Thread(target=cleanup, daemon=True)
cleanup_thread.start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # '0.0.0.0'으로 설정하여 모든 네트워크 인터페이스에서 접속 가능하도록 설정

