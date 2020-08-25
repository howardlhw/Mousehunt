import datetime

def eprint(location, message):
    t = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
    print(f"[{t}] {location}: {message}")


def debug(message, debug=False):
    if debug:
        t = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
        print(f"[{t}] DEBUG: {message}")

