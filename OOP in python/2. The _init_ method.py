
class Computer:
    def __init__(self, cpu, ram):
        # when we initial computer, it's called automatically !
        self.cpu = cpu
        self.ram = ram

    def config(self):
        # from this self we can retrive the data, so we use self !
        print(f"config is {self.cpu} with {self.ram} gb ram")


# __int__ called [check by print a statement on init]
comp1 = Computer(cpu="i5", ram=16)  # best practice with name
comp2 = Computer("Amd ryzen", 8)

comp1.config()
comp2.config()
# config is i5 with 16 gb ram
# config is Amd ryzen with 8 gb ram
