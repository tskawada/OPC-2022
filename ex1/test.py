class Test:
    def __init__(self):
        self.ang = 0
    def angle(self, ang):
        self.ang = ang
        print(ang)
    def read_ang(self):
        return self.ang
    def __del__(self):
        self.ang = 0
        print("deconstruct")