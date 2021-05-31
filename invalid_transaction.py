"""
A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name
in a different city.
You are given an array of strings transaction where transactions[i] consists of
comma-separated values representing the name, time (in minutes), amount, and city of
the transaction.

Return a list of transactions that are possibly invalid. You may return the answer
in any order.

Example 1:
Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs
within a difference of 60 minutes, have the same name and is in a different city.
Similarly the second one is invalid too.

Example 2:
Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]

Example 3:
Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]


Constraints:

transactions.length <= 1000
Each transactions[i] takes the form "{name},{time},{amount},{city}"
Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
Each {time} consist of digits, and represent an integer between 0 and 1000.
Each {amount} consist of digits, and represent an integer between 0 and 2000.
"""
from typing import List


# This is a brute force approach
# Time: O(n^2)
# Space: O(n)
def invalid_transaction(transactions) -> List[str]:
    result = []
    name, time, amount, city = [], [], [], []

    if not len(transactions):
        return result

    add = [1] * len(transactions)

    for transaction in transactions:
        t = transaction.split(",")
        name.append(t[0])
        time.append(eval(t[1]))
        amount.append(eval(t[2]))
        city.append(t[3])

    for i in range(len(transactions)):
        if amount[i] > 1000:
            add[i] = False

        for j in range(i + 1, len(transactions)):
            if name[i] == name[j] and abs(time[i] - time[j]) <= 60 and city[i] != city[j]:
                add[i] = False
                add[j] = False

    for idx, value in enumerate(add):
        if not value:
            result.append(transactions[idx])

    return result


if __name__ == "__main__":
    print(invalid_transaction(["alice,20,800,mtv", "alice,50,100,beijing"]))
    print(invalid_transaction(["alice,20,800,mtv", "alice,50,1200,mtv"]))
    print(invalid_transaction(["alice,20,800,mtv", "bob,50,1200,mtv"]))
