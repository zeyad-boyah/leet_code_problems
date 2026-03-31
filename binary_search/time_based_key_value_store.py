from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # assuming they will be added in an orderly fashion 
        self.time_map[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in  self.time_map:
            return ""
        l,r= 0, len(self.time_map[key])-1
        ans =""
        while l <=r:
            m = (l+r)//2
            if self.time_map[key][m][0] <= timestamp:
                ans = self.time_map[key][m][1]
                l = m +1
            else:
                r = m -1
        return ans


test = TimeMap()
test.set("alice", "happy", 1)
test.get("alice", 1)
test.get("alice", 2)
test.set("alice", "sad", 3)
test.get("alice", 3)