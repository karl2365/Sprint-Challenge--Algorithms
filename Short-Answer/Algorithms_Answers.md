#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I



a) O(n) because we are incrementing a 2n times until we break, and O(n) is a subset of O(2n)

b) O(n^2) because we are using a nested loop

c) O(n) because O(n^1) is reduced to linear time since we're only making one recursive call
Exercise II

Great candidate for Binary Search. A building is essentially a sorted list and we are trying to find a "target" such that we can drop an egg without it breaking.

   1. Pick a middle point in the stairs
   2. Drop an egg
   3. If the egg breaks from the halfway point, let's say floor 50
        Drop the egg again from floor 25
        Egg breaks? Drop the egg from 38, if it breaks, halve the difference again where the difference is approximately half way between the last point.

The runtime of this algorithm would be O(log n) because we're halving the number of elements we check, essentially to check 16 elements it requires 4 steps.