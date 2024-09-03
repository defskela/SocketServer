import threading
import time


def task(name, duration):
    print(f"Starting task {name}")
    time.sleep(duration)
    print(f"Task {name} completed")

# Создаем несколько потоков
threads = []
for i in range(30):
    t = threading.Thread(target=task, args=(f"Task-{i+1}", 2))
    threads.append(t)
    t.start()

# Ждем завершения всех потоков
for t in threads:
    t.join()

print("All tasks completed")
