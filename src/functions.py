class Functions:
    @staticmethod
    def regression_line():
        lists = []
        count = 0
        while True:
            count += 1
            x = input("请输入x{}的值(Q/q退出)：".format(count))
            if x.upper() == 'Q':
                break
            y = input("请输入y{}的值(Q/q退出)：".format(count))
            print("------------------------------")
            if y.upper() == 'Q':
                break
            elif x is None:
                continue
            elif y is None:
                continue
            else:
                lists.append({"x": float(x), "y": float(y)})
        x_sum = 0
        y_sum = 0
        fen_zi = 0
        fen_mu = 0
        for i in range(len(lists)):
            xi = lists[i]["x"]
            yi = lists[i]["y"]
            x_sum += xi
            y_sum += yi
        x_avg = x_sum/len(lists)
        y_avg = y_sum/len(lists)
        for i in range(len(lists)):
            xi = lists[i]["x"]
            yi = lists[i]["y"]
            fen_zi += (xi - x_avg)*(yi - y_avg)
            fen_mu += (xi - x_avg)**2
        a = fen_zi / fen_mu
        constant = y_avg - a * x_avg
        return "y = {}x ".format(format(a, '.6f')) + "+ {}".format(format(constant, '.6f'))
