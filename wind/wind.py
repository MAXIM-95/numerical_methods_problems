import math
import sys

class System:
    def __init__(self, h, t, a1, a2, a3, a4, a5):
        self.h = h
        self.t = t
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.y1 = [0.2]
        self.y2 = [10.0]
        self.y3 = [15.0]

    def printParam(self):
        res = "t = " + str(self.t) + " h = " + str(self.h) + " a1 = " + str(self.a1) + " a2 = " + str(
            self.a2) + " a3 = " + str(self.a3) + " a4 = " + str(self.a4) + " a5 = " + str(self.a5)
        print(res)

    def printY(self):
        print("#x\t\ty1\t\ty2\t\ty3\t\tyr1\t\tyr2\t\tyr3")
        for i in range(len(self.y1)):
            res = str(i * self.h) + "\t\t" + str(self.y1[i]) + "\t\t" + str(self.y2[i]) + "\t\t" + str(
                self.y3[i]) + "\t\t" + str(self.__yr1(i * self.h)) + "\t\t" + str(
                self.__yr2(i * self.h, self.__yr1(i * self.h))) + "\t\t" + str(
                self.__yr3(i * self.h, self.__yr1(i * self.h)))
            print(res)

    def sett(self, arg):
        self.t = arg

    def seth(self, arg):
        self.h = arg

    def seta1(self, arg):
        self.a1 = arg

    def seta2(self, arg):
        self.a2 = arg

    def seta3(self, arg):
        self.a3 = arg

    def seta4(self, arg):
        self.a4 = arg

    def seta5(self, arg):
        self.a5 = arg

    def __dy1(self, y1, y2, y3, t):
        return self.a1 * (y2 - y3) - self.a2 * (y1 - self.__f(t))

    def __dy2(self, y1, y2, y3):
        return y1 * y3 - y2 + self.a5

    def __dy3(self, y1, y2, y3):
        return -y1 * y2 - y3 + self.a5

    def __f(self, t):
        return self.a3 + self.a4 * math.sin(2 * 3.14 * t)

    def __yr1(self, t):
        return math.sqrt(2 * self.a5 - self.a2 / self.a1) * math.sqrt(self.a1 / self.a2)

    def __yr2(self, t, y1):
        return 0.5 * self.a2 / self.a1 * (1 + y1)

    def __yr3(self, t, y1):
        return 0.5 * self.a2 / self.a1 * (1 - y1)

    def calculate(self):
        x = self.h
        i = 0
        while x <= self.t:
            self.y1.append(self.y1[i] + self.h * self.__dy1(self.y1[i], self.y2[i], self.y3[i], x))
            self.y2.append(self.y2[i] + self.h * self.__dy2(self.y1[i], self.y2[i], self.y3[i]))
            self.y3.append(self.y3[i] + self.h * self.__dy3(self.y1[i], self.y2[i], self.y3[i]))
            i += 1
            x += self.h


def main(a1, a2, a3, a4, a5):
    sys = System(.01, 500.0, float(a1), float(a2), float(a3), float(a4), float(a5))
    # sys.printParam()
    sys.calculate()
    sys.printY()


main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
