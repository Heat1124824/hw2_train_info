class Train:
    def __init__(self, number, time, via, destination, train, platform):
        #編寫初始化參數
        self.number = number 
        self.time = time
        self.via = via
        self.destination = destination
        self.train = train
        self.platform = platform
    def info(self):
        #回傳列車資訊
        return f"車次：{self.number}\n時間：{self.time}\n經由：{self.via}\n終點：{self.destination}\n車種：{self.train}\n月台：{self.platform}"
def main():
    #train_data = Train('472', '07:56', '山線', '台東', '自強號', '2')
    #train_data = Train('2174', '13:59', '山線', '瑞芳', '區間車', '1')
    train_data = Train('521', '17:00', '海線', '潮州', '莒光號', '3')
    train_info = train_data.info() #取得列車資訊
    print(train_info)

if __name__=="__main__": 
    main() 