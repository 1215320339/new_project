import random


class Game:
    def __init__(self):
        self.__dict_target = {0: "猜对了！", 1: "大了！", 2: "小了！"}

    def guess_numbers_game(self):
        while True:
            random_number = random.randint(0, 100)
            while True:
                print("-----猜数字游戏-----")
                number = int(input("请输入0-100之间的一个整数\n:"))
                result = self.__judge_size(number, random_number)
                if result == Option.equal:
                    print(self.__dict_target[result])
                    if self.__is_continue():
                        break
                    return
                else:
                    print(self.__dict_target[result])

    def __is_continue(self):
        info = input("继续玩？y/n\n:")
        if info == "y":
            return True
        return False


    def __judge_size(self, number, random_number):
        if random_number > number:
            return Option.small
        elif random_number < number:
            return Option.big
        elif random_number == number:
            return Option.equal


class Option:
    equal = 0
    big = 1
    small = 2


if __name__ == '__main__':
    g = Game()
    g.guess_numbers_game()











