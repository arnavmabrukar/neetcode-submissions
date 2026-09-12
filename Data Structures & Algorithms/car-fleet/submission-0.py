class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # we will travel in reversed order
        # if the curr car we are at will collide with our previous car we viewed
        # then we want to pop it out and disregard it, since that it will end up traveling
        # at the same speed as the car ahead of it
        # otherwise we just append the car
        # then at the end the length of the stack should be = to the fleet of cars
        pairs = [[p, s] for p, s in zip(position, speed)]
        stack = []
        for p, s in sorted(pairs)[::-1]: # reversed traversal + sorted by position
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

        # time O(n log n)
            
