class StudentResult:
    def __init__(self):
        self.__score = 0
    
    def update_score(self, new_score):
        if new_score > self.__score:
            self.__score = new_score
            result = f"Score updated to {self.__score}"
            print(result)
            return result
        else:
            result = f"New score is lower. Score remains: {self.__score}"
            print(result)
            return result

res = StudentResult()
res.update_score(78)
res.update_score(65)
res.update_score(88)
