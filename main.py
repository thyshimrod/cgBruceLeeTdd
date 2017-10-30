class SolveChuckInverse():

    @staticmethod
    def grabfirstelement(_param):
        if _param == "0":
            return "1"
        elif _param == "00":
            return "0"
        else:
            return "INVALID"

    @staticmethod
    def checkPair(_param):
        if len(_param.split()) % 2 == 1:
            return False
        return True

    @staticmethod
    def checkValidCharacter(_param):
        for a in _param:
            if a not in (' ', '0'):
                return False
        return True

    @staticmethod
    def checkvalidity(_param):
        result = SolveChuckInverse.checkPair(_param)
        result = result and SolveChuckInverse.checkValidCharacter(_param)
        return result

    @staticmethod
    def unarytobinary(_param):
        tab = _param.split(" ")
        result = ""
        i = 0
        while i < len(tab):
            result += SolveChuckInverse.grabfirstelement(tab[i]) * len(tab[i+1])
            i += 2
        return result


    @staticmethod
    def binarytonumber(_param):
        result = 0
        i = 64
        for p in _param:
            result += int(p) * i
            i //= 2
        return result


    @staticmethod
    def solve(_param):
        result = ""
        if not SolveChuckInverse.checkvalidity(_param):
            return "INVALID"
        bina = SolveChuckInverse.unarytobinary(_param)
        if (len(bina) % 7) != 0:
            return "INVALID"
        else:
            for i in range((len(bina)//7)):
                result += chr(SolveChuckInverse.binarytonumber(bina[(i*7):(i*7)+7]))

        return result
