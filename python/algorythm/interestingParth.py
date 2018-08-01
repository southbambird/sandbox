class InterestingParth:
    def bestInvitation(first, second):
        ans = 0

        for i in range(0,len(first)):
            f = 0
            s = 0

            for j in range(0,len(first)):
                if(first[i]  == first[j] ):
                    f+=1
                if(first[i]  == second[j]):
                    f+=1
                if(second[i] == first[j] ):
                    s+=1
                if(second[i] == second[j]):
                    s+=1

            ans = max(f, ans)
            ans = max(s, ans)

        return ans
    
if __name__ == '__main__':
    interestingParth = InterestingParth()
    first  = ['snakes','programming','cobra','monty']
    second = ['python','python','anaconda','python']
    print(InterestingParth.bestInvitation(first,second))
