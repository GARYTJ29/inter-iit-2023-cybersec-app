class PassCheck:
    lookup = [158, 152, 106, 153, 44, 139, 54, 67, 169, 156, 159, 192, 243, 88, 96, 189, 225, 33, 79, 3, 248, 100, 145, 14, 76, 126, 141, 224, 64, 74, 86, 55, 220, 49, 150, 71, 187, 22, 40, 162]

    @staticmethod
    def hash(n, n2):
        return chr(65 + ((n ^ n2) + n & (n + n2)) % 26)

    @staticmethod
    def nuh():
        print("Wrong password!")

    @staticmethod
    def yuh():
        print("Correct password!")

    @classmethod
    def check(cls, s):
        if len(s) * 2 != len(cls.lookup):
            cls.nuh()
            return

        for i in range(len(s)):
            if s[i] != cls.hash(cls.lookup[2 * i], cls.lookup[2 * i + 1]):
                cls.nuh()
                return

        cls.yuh()

# Example usage:
# PassCheck.check("your_string_here")
lookup = [158, 152, 106, 153, 44, 139, 54, 67, 169, 156, 159, 192, 243, 88, 96, 189, 225, 33, 79, 3, 248, 100, 145, 14, 76, 126, 141, 224, 64, 74, 86, 55, 220, 49, 150, 71, 187, 22, 40, 162]

a = PassCheck()
arrstr = []
for i in range(len(lookup)//2):
    arrstr.append(a.hash(lookup[2 * i], lookup[2 * i + 1]))
password = "".join(arrstr)
print("Password is","".join(arrstr))
PassCheck.check(password)
PassCheck.check("KXRPQQGZWSQQWAKDFRMA")
