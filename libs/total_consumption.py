# 2. 총 소비액
def total_consumption(self):

    total_consumption = 0
    for consumption in self.df["Price(\)"]:
        if consumption < 0:
            total_consumption += consumption

    print("총 소비액(원): {}원".format(total_consumption))
