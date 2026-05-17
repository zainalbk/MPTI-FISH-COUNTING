import random
from datetime import datetime, timedelta


def random_status():
    return random.choice(["Sehat", "Rusak", "Perlu Cek"])


def generate_dashboard_metrics():
    healthy = random.randint(700, 1200)
    broken = random.randint(50, 280)
    total = healthy + broken + random.randint(0, 80)
    accuracy = round(random.uniform(88.0, 99.5), 1)
    return {
        "healthy": healthy,
        "broken": broken,
        "total": total,
        "accuracy": accuracy,
        "counter": random.randint(0, 25000),
        "progress": random.randint(45, 98),
    }


def generate_realtime_series(length=24):
    base = random.randint(300, 700)
    return [max(0, base + random.randint(-130, 130)) for _ in range(length)]


def generate_history_rows(count=40):
    rows = []
    now = datetime.now()
    for idx in range(count):
        dt = now - timedelta(minutes=idx * random.randint(5, 30))
        status = random_status()
        rows.append({
            "id": f"SB-{1000 + idx}",
            "tanggal": dt.strftime("%d-%m-%Y %H:%M"),
            "status": status,
            "jumlah": random.randint(80, 1500),
            "akurasi": f"{round(random.uniform(85.0, 99.8), 1)}%",
            "keterangan": random.choice([
                "Normal",
                "Sampling",
                "Perlu kalibrasi",
                "Batch malam",
                "QC aktif",
            ]),
        })
    return rows


def generate_statistical_data():
    labels = ["Sen", "Sel", "Rab", "Kam", "Jum", "Sab", "Min"]
    bars = [random.randint(300, 1300) for _ in labels]
    lines = [random.randint(200, 1500) for _ in range(12)]
    pie = {
        "Sehat": random.randint(50, 80),
        "Rusak": random.randint(10, 35),
        "Perlu Cek": random.randint(5, 20),
    }
    return {
        "bar_labels": labels,
        "bar_values": bars,
        "line_values": lines,
        "pie_values": pie,
    }


def validate_login(username, password):
    return bool(username.strip()) and bool(password.strip())
