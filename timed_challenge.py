# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Question 3: Remove Duplicates (Keep Order)
#
# Return the values in the order they first appeared, without duplicates.
#
# Input: ["apple", "banana", "apple", "kiwi", "banana"]
# Output: ["apple", "banana", "kiwi"]
# Set a timer for 30 minutes and complete the question!
def remove_duplicates(values):
    result = []
    seen = set()

    for value in values: 
        if value not in seen: 
            result.append(value)
            seen.add(value)

    return result

# # Reflection:

#

# For this challenge, I used both a list and a set because each structure served a different purpose. I used a set called "seen" to keep track of values that had already appeared. Sets are useful for this problem because checking whether a value is already present can be done in O(1) time on average. I also used a list called "result" because the problem required me to keep the values in the same order in which they first appeared. The final algorithm therefore checks each value once and adds it to the result only if it has not already been seen.

#

# The 30-minute time limit influenced my decision to use a simple approach that I already understood rather than trying to create a more complicated data structure. Since the problem was based on removing duplicates while preserving order, using a set for tracking and a list for the final result was straightforward and efficient. The time limit encouraged me to focus on getting a working solution first and then testing it with several different inputs.

#

# Under time pressure, I prioritized clarity and correctness over trying to make the solution more advanced. One trade-off is that the solution uses additional memory for both the result list and the seen set, giving it O(n) additional space. However, this was a reasonable compromise because it allowed the algorithm to run in O(n) time on average instead of repeatedly searching through the result list. I also tested normal inputs, an empty list, a list containing only duplicates, and a list with no duplicates to make sure the solution handled different cases.
