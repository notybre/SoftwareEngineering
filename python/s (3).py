import time
from datetime import datetime
for i in range(5):
    print(datetime.now().strftime("%H:%M:%S"))  # выводим текущее время
    time.sleep(1)                               # задержка на 1 секунду
