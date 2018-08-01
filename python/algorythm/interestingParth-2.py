class InterestingParty():
    def bestInvitation(first, second):
        dic = {}

        for i in range(0, len(first)):
            dic[first[i]]  = 0
            dic[second[i]] = 0

        for i in range(0, len(first)):
            dic[first[i]]  += 1
            dic[second[i]] += 1

        ans = 0
        for _, value in dic.items():
            if ans < value:
                ans = value

        return ans

if __name__ == '__main__':
    interestingParty = InterestingParty()
    first  = ['snakes','programming','cobra','monty']
    second = ['python','python','anaconda','python']
    print(InterestingParty.bestInvitation(first,second))

