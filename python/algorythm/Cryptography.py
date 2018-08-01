class Cryptography():
    def encrypt(self,numbers):
        ans = 0
        for i, _ in enumerate(numbers):
            seki = 1
            for j, value in enumerate(numbers):
                if(i == j):
                    seki *= (value + 1)
                else:
                    seki *= value

                if(seki > ans):
                    ans = seki

        return ans
            

if __name__ == '__main__':
    numbers = [1, 3, 2, 1, 1, 3]
    crypt = Cryptography()
    assert 36 == crypt.encrypt(numbers)

    numbers = [1000, 999, 998, 997, 996, 995]
    assert 986074810223904000 == crypt.encrypt(numbers)
