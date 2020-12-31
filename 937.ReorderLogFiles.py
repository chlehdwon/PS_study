# You have an array of logs.
# Each log is a space delimited string of words.
# For each log, the first word in each log is
# an alphanumeric identifier.
# Then, either:
# Each word after the identifier will consist only of lowercase letters,
# or; Each word after the identifier will consist only of digits.
# We will call these two varieties of logs letter-logs and digit-logs.
# It is guaranteed that each log has at least one word
# after its identifier.

# Reorder the logs so that all of the letter-logs come
# before any digit-log.
# The letter-logs are ordered lexicographically ignoring identifier,
# with the identifier used in case of ties.
# The digit-logs should be put in their original order.

# Return the final order of the logs.


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs, digits_logs = [], []
        for log in logs:
            # check whether log is letter-logs or digits-log
            if log.split(' ')[1].isdigit():
                