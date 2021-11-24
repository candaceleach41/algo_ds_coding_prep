"""
You have a browser of one tab where you start on the homepage and you can visit another url,
get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
void visit(string url) Visits url from the current page. It clears up all the forward history.
string back(int steps) Move steps back in history. If you can only return x steps in the
history and steps > x, you will return only x steps. Return the current url after moving
back in history at most steps.
string forward(int steps) Move steps forward in history. If you can only forward x steps
in the history and steps > x, you will forward only x steps. Return the current url after
forwarding in history at most steps.

Example:

Input:
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
Output:
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

Explanation:
BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return
                                             "facebook.com"
browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to
                                             "google.com". return "google.com"
browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com".
                                             return "leetcode.com"

Constraints:

1 <= homepage.length <= 20
1 <= url.length <= 20
1 <= steps <= 100
homepage and url consist of  '.' or lower case English letters.
At most 5000 calls will be made to visit, back, and forward.
"""


# Using stack approach
class BrowserHistory:
    def __init__(self, homepage):
        self.history = []
        self.future = []
        self.history.append(homepage)

    def visit(self, url):
        self.history.append(url)
        self.future = []

    def back(self, steps):
        while steps > 0 and len(self.history) > 1:
            self.future.append(self.history[-1])
            self.history.pop()
            steps -= 1
        return self.history[-1]

    def forward(self, steps):
        while steps > 0 and self.future:
            self.history.append(self.future[-1])
            self.future.pop()
            steps -= 1
        return self.history[-1]


# ------------------ Using Doubly Linked List-----------------------------
class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class BrowserHistoryDLL:
    def __init__(self, homepage: str):
        self.root = Node(homepage)

    def visit(self, url: str) -> None:
        node = Node(url)
        node.prev = self.root
        self.root.next = node
        self.root = self.root.next

    def back(self, steps: int) -> str:
        while steps and self.root.prev:
            self.root = self.root.prev
            steps -= 1
        return self.root.data

    def forward(self, steps: int) -> str:
        while steps and self.root.next:
            self.root = self.root.next
            steps -= 1
        return self.root.data


if __name__ == "__main__":
    bh = BrowserHistoryDLL("http://www.bloomberg.com/articles/123")
    bh.visit("http://www.bbc.com")
    bh.visit("http://www.cnn.com")
    print(bh.back(1))
    print(bh.forward(1))
    bh.visit("http://www.google.com?search=hello")


