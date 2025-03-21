class BrowserHistory:

    def __init__(self, homepage: str):
        self.pagelist = [homepage]
        self.index = 0
        self.len = 1


    def visit(self, url: str) -> None:
        self.pagelist = self.pagelist[:self.index+1]
        self.len = len(self.pagelist)
        self.pagelist.append(url)
        self.index = self.len
        self.len += 1

    def back(self, steps: int) -> str:
        if steps > self.index:
            self.index = 0
        else:
            self.index -= steps
        return self.pagelist[self.index]

    def forward(self, steps: int) -> str:
        if steps > self.len-1 - self.index:
            self.index = self.len - 1
        else:
            self.index += steps
        return self.pagelist[self.index]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
