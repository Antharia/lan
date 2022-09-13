import sys


class Interpreter:
    def __init__(self):
        self.w = []
        for _ in range(32):
            self.w.append("0")
        self.a = 0
        self.b = 0
        self.c = 0

    def scan(self, line):
        try :
            first, second = line.split(" ")
        except :
            print("Usage: [x] [y]")
        else :
            if first in ["a", "b", "c", "w"]:
                self.set(first, second)
                self.output(first)
            if first in ["+", "-"]:
                self.operator(first, second)
                self.output(second)
            if first == "o":
                self.output(second)
            if first == "i":
                self.input(second)
                self.output(second)

    def operator(self, op, reg):
        match reg:
            case "a":
                if op == "+":
                    self.a += 1
                if op == "-":
                    self.a -= 1
            case "b":
                if op == "+":
                    self.b += 1
                if op == "-":
                    self.b -= 1
            case "c":
                if op == "+":
                    self.c += 1
                if op == "-":
                    self.c -= 1

    def input(self, reg):
        data = input()
        self.set(reg, data)

    def set(self, reg, data):
        match reg:
            case "a":
                self.a = int(data)
            case "b":
                self.b = int(data)
            case "w":
                for i, char in enumerate(data):
                    self.w[self.c+i] = char
            case "c":
                self.c = int(data)

    def output(self, reg):
        match reg:
            case "a":
                print(self.a)
            case "b":
                print(self.b)
            case "w":
                for i in self.w:
                    print(i, end="")
                print()
            case "c":
                print(self.c)


class Lan:
    def __init__(self):
        self.interpreter = Interpreter()
        if len(sys.argv) > 2:
            raise Exception("Usage : lan [script]")
        elif len(sys.argv) == 2:
            self.run_file(sys.argv[1])
        else:
            self.run_prompt()

    def run_file(self, lan_file):
        with open(lan_file, "r") as f:
            lines = f.readlines()
            for line in lines:
                self.run(line)

    def run_prompt(self):
        while True:
            line = input("lan> ")
            if line == None or line in ["exit", "quit", "q", "x"]:
                break
            self.run(line)

    def run(self, line):
        self.interpreter.scan(line)


lan = Lan()
