ass Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #return
        result = []
        
        #corner cases
        if n < 3:
            result = [str(i+1) for i in range(n)]
        
        #main logistic
        else:
            for j in range(n):
                if (j+1)%15 == 0:
                    ele = "FizzBuzz"
                elif (j+1)%5 == 0:
                    ele = "Buzz"
                elif (j+1)%3 == 0:
                    ele = "Fizz"
                else:
                    ele = str(j+1)
                result.append(ele)

        return result
