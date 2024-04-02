class FuzzyGasController:
    """
    # emtiazi todo
    write all the fuzzify,inference,defuzzify method in this class
    """

    def __init__(self):
        pass

    def membership_center_close(self, x):
        if 0 <= x <= 50:
            return -x / 50 + 1
        return 0

    def membership_center_moderate(self, x):
        if 40 <= x <= 50:
            return x / 10 - 4
        if 50 <= x <= 100:
            return -x / 50 + 2
        return 0

    def membership_center_far(self, x):
        if 90 <= x <= 200:
            return x / 110 - 9 / 11
        if x >= 200:
            return 1
        return 0

    def membership_gas_low(self, x):
        if 0 <= x <= 5:
            return x / 5
        if 5 <= x <= 10:
            return -x / 5 + 1
        return 0

    def membership_gas_medium(self, x):
        if 0 <= x <= 15:
            return x / 15
        if 15 <= x <= 30:
            return -x / 15 + 2
        return 0

    def membership_gas_high(self, x):
        if 25 <= x <= 30:
            return x / 5 - 5
        if 30 <= x <= 90:
            return -x / 60 + 3 / 2
        return 0

    def max_gas(self, x, gas_low, gas_medium, gas_high):
        gas_low = min(self.membership_gas_low(x), gas_low)
        gas_medium = min(self.membership_gas_medium(x), gas_medium)
        gas_high = min(self.membership_gas_high(x), gas_high)
        return max(gas_low, gas_medium, gas_high)

    def linspace(self, start, end, count):
        dif = (end - start) / count
        res=[]
        x = start
        while x < end:
            res.append(x)
            x = x + dif

        return res

    def decide(self, center_dist):
        """
        main method for doin all the phases and returning the final answer for gas
        """
        gas_low = self.membership_center_close(center_dist)
        gas_medium = self.membership_center_moderate(center_dist)
        gas_high = self.membership_center_far(center_dist)

        soorat = makhraj = 0.0
        x = self.linspace(0, 90, 1000)
        delta = x[1] - x[0]
        for i in x:
            u = self.max_gas(i, gas_low, gas_medium, gas_high)
            soorat += u * delta * i
            makhraj += u * delta
        gas = 0.0
        if makhraj:
            gas = soorat / makhraj
        return gas
