import sys

class System():
    def __init__(self):
        pass

    def exit(self):
        try:
            sys.exit()
        except Exception as e:
            print(f"[WARNING] {e}")