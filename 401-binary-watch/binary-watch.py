class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:

        res = []
        for hour in range(12):
            for minute in range(60):
                if bin(hour).count("1") + bin(minute).count("1") == turnedOn:
                    minute = f"0{minute}" if minute < 10 else minute
                    r = f"{hour}:{minute}"
                    res.append(r)

        return res             
        