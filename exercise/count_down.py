import time
import winsound, platform
import ctypes

def sound():
    system = platform.system()
    if system == "Windows":
        winsound.MessageBeep()

def alert(title, msg):
    ctypes.windll.user32.MessageBoxW(0, msg, title, 0x40 | 0x1000)

def countdown(minute=1):
    total_seconds = int(minute * 60)
    print("倒计时开始：")
    for total_second in range(total_seconds, -1, -1):
        min, sec = divmod(total_second, 60)       
        print(f"\r{min:02d}:{sec:02d}", end="", flush=True)     #\r不是清除一行，而是将光标移到首位，所以新字符串长度不够时会有残留，用:<15格式化补空格
        time.sleep(1) 
    print("\n时间到！\a")
    # sound()
    alert("计时器", f"{minute}分钟，时间到啦")

if __name__ == "__main__":
    countdown(0.1)