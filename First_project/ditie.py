class Buy_Ticket(object):

    def __init__(self, starts, ends, dict):
        self.starts = starts
        self.ends = ends
        self.dict = dict

    def buy(self):
        global price
        print('该地铁的起止站为：%s，终止站为：%s' % (self.starts, self.ends))
        print('*' * 50)
        print('1:哈东站\n'
              '2:太平桥\n'
              '3：交通学院\n'
              '4：工程大学站\n'
              '5：烟厂站\n'
              '6：医大二院站\n'
              '7：博物馆站\n'
              '8：铁路局站 ')
        print('*' * 50)
        local = int(input('请选择你的目的地：'))
        print('你选择的目的地为：', dict[local])

        if local >= 6:
            print('去往%s的票价为：%d'%(dict[local],price+1))
            return price + 1
        else:
            print('去往%s的票价为：%d'%(dict[local],price))
            return price


class Pay_Ticket(object):
    def __init__(self, money,price):
        self.money = money
        self.price=price

    def pay(self):
        if self.money > price:
            print('出票成功！')
            print('给你返零：', self.money - self.price)
            return self.money-self.price
        else:
            return None

class TickectPrice(Pay_Ticket):

    def tickect_price(self):
        list = [1, 5, 10, 20, 50]
        while self.money not in list:
            print('不好意思，不符合交易条件请重新提交金额！')
            self.money = int(input('请提交你的金额（金额只收5元/10元/20元/50元）：'))
        submit = Pay_Ticket(self.money, price_1).pay()
        while submit == None:
            print('*' * 50)
            print('价格不足，请重新提交你的金额！')
            money = int(input('请提交你的金额：'))
            submit = Pay_Ticket(money, price_1).pay()



if __name__ == '__main__':
    price=2
    dict = {1: '哈东站', 2: '太平桥', 3: '交通学院', 4: '工程大学站', 5: '烟厂站', 6: '医大一院站',
            7: '博物馆站', 8: '铁路局站'}
    print('-'*50,'欢迎进入地铁购票系统：','-'*50)
    print('1、地点买票')
    print('2、票价买票')
    print('-'*50)
    choose=int(input('请选择你的操作：'))
    if choose!=1 and choose!=2:
        raise Exception(ValueError)
    else:
        if choose==1:
            print('开始购票！')
            buy = Buy_Ticket('哈东站', '铁路局站', dict=dict).buy()
            price_1 = buy
            ch = input("买一张?(y/n)")
            if ch == 'y':
                money = int(input('请提交你的金额（金额只收1元/5元/10元/20元/50元）：'))
                TickectPrice(money,price_1).tickect_price()
            else:
                print('请重新开始购票！')
                Buy_Ticket('哈东站', '铁路局站', dict=dict).buy()
        elif choose==2:
            print('开始购票！')
            print('票价为两种: \n1、2元\n2、3元')
            xuanze=int(input('选择你要购买的票价类型：'))
            if xuanze==1:
                money = int(input('请提交你的金额（金额只收1元/5元/10元/20元/50元）：'))
                price_1=2
                TickectPrice(money,price_1).tickect_price()
            elif xuanze==2:
                money = int(input('请提交你的金额（金额只收1元/5元/10元/20元/50元）：'))
                price_1=3
                TickectPrice(money,price_1).tickect_price()





