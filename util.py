import datetime

def eprint(location, message):
    t = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
    print(f"[{t}] {location}: {message}")
