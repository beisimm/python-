class ChinaGetter():
    def __init__(self):
        self.trans = {"dog": "小狗", "cat": "小猫"}

    def get(self, id):
        try:
            return self.trans[id]
        except:
            return str(id)

if __name__ == '__main__':
    print(ChinaGetter().get("dog"))