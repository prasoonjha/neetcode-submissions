class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        delta_x = vt
        """
        xv = [(position, speed) for position, speed in zip(position, speed)]
        xv.sort()
        fleets = 0
        stack = deque([])
        for position, speed in xv:
            print(f"{speed=}{position=}")
            dist = target-position
            t = dist/speed
            print(f"{t=}")
            while len(stack) and stack[-1]<=t:
                #process
                n = stack.pop()
                print(f"popped {n=}")
            print(f"pushed {t=}")
            stack.append(t)
        print(stack)
        return len(stack)