class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # we can use an ascending  monotonic stack to track the head of the fleet
        # but the position array must be sorted first while also keeping in mind the 
        # speed index in the array 
        # we can calculate the time by doing (Target - position)/speed
        compined_speed_position =  list(zip(position,speed))
        def quick_sort_with_index(arr):
            if not arr:
                return []
            if len(arr) <2 :
                return [arr[0]]
            pivot = arr[0]
            greater = [i for i in arr[1:] if i[0] >= pivot[0]]
            smaller = [i for i in arr[1:] if i[0]< pivot[0]]
            return quick_sort_with_index(smaller) + [pivot] + quick_sort_with_index(greater)
        # will cause a stackover flow on the browser IDE
        # compined_speed_position= quick_sort_with_index(compined_speed_position)
        compined_speed_position= sorted(compined_speed_position)
        monotonic_time_stack = []
        ans= len(position)
        for p,s in compined_speed_position:
            time = (target - p)/s
            while monotonic_time_stack and monotonic_time_stack[-1] <= time:
                monotonic_time_stack.pop()
                ans -=1
            monotonic_time_stack.append(time)
        return ans
            
test = Solution()

target = 10
position = [4,1,0,7]
speed = [2,2,1,1]

print(test.carFleet(target=target,position=position,speed=speed))