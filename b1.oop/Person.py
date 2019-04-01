class Person:
    ten = 'quy'
    gioiTinh = True
    tuoi = "tuoi"
    cmd = 123
    def __init__(self, cmnd = 123, tuoi = 12, ten = 'quy', gioiTinh = True) :
        self.cmnd = cmnd
        self.tuoi = tuoi
        self.ten = ten
        self.gioiTinh = gioiTinh

    def setCmnd(self, cmnd) :
        self.cmnd = cmnd

    def getCmnd(self):
        return self.cmnd

    def setTuoi(self, tuoi):
        self.tuoi = tuoi

    def getTuoi(self):
        return self.tuoi

    def setTen(self, ten):
        self.ten = ten

    def getTen(self):
        return self.ten

    def setGioiTinh(self, gioiTinh):
        self.gioiTinh = gioiTinh

    def getGioiTinh(self):
        return self.gioiTinh

    def run(self):
        return self.chay()
