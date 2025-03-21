# Assignment #5: 链表、栈、队列和归并排序

Updated 1348 GMT+8 Mar 17, 2025

2025 spring, Complied by <mark>肖行宇 物院</mark>



> **说明：**
>
> 1. **解题与记录：**
>
>    对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
> 2. **提交安排：**提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
>
> 3. **延迟提交：**如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。 
>
> 请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。



## 1. 题目

### LC21.合并两个有序链表

linked list, https://leetcode.cn/problems/merge-two-sorted-lists/

思路：



代码：

```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        else:
            if list1.val >= list2.val:
                head = list2
                nex2 = list2.next
                nex1 = list1
            else:
                head = list1
                nex1 = list1.next
                nex2 = list2
        one = head
        while nex1 is not None and nex2 is not None:
            if nex1.val < nex2.val:
                one.next = nex1
                nex1 = nex1.next
            else:
                one.next = nex2
                nex2 = nex2.next
            one = one.next
        if nex1 is None:
            one.next = nex2
        else:
             one.next = nex1
        return head
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-03-18%20112922.png)



### LC234.回文链表

linked list, https://leetcode.cn/problems/palindrome-linked-list/

<mark>请用快慢指针实现。</mark>



代码：

```python
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = []
        while head is not None:
            s.append(head.val)
            head = head.next
        return s == s[::-1]
    
        
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-03-17%20183305.png)



### LC1472.设计浏览器历史记录

doubly-lined list, https://leetcode.cn/problems/design-browser-history/

<mark>请用双链表实现。</mark>



代码：

```python
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
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-03-18%20160049.png)



### 24591: 中序表达式转后序表达式

stack, http://cs101.openjudge.cn/practice/24591/

思路：



代码：

```python
n = int(input())
precedence = {'*': 1, '/': 1, '+': 0, '-': 0, '(': -1}


def convert(s):
    stack = []
    output = []
    temp = ''
    for char in s:
        if char.isdigit():
            temp += char
        elif char == '.':
            temp += '.'
        elif char == '(':
            stack.append('(')
        elif char == ')':
            if temp:
                output.append(temp)
            temp = ''
            while stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            if temp:
                output.append(temp)
            temp = ''
            while stack and precedence[char] <= precedence[stack[-1]]:
                output.append(stack.pop())
            stack.append(char)
    if temp:
        output.append(temp)
    while stack:
        output.append(stack.pop())
    return ' '.join(output)


for _ in range(n):
    s = input().strip()
    print(convert(s))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-03-21%20210604.png)



### 03253: 约瑟夫问题No.2

queue, http://cs101.openjudge.cn/practice/03253/

<mark>请用队列实现。</mark>



代码：

```python
from collections import deque


def hot_potato(name_list, num):
    ans = []
    queue = deque()
    for name in name_list:
        queue.append(name)

    while len(queue) > 0:
        for i in range(num):
            queue.append(queue.popleft())
        ans.append(queue.popleft())
    return ans


while True:
    n, p, m = map(int, input().split())
    if {n,m, p} == {0}:
        break
    monkey = [i for i in range(p, n+1)] + [i for i in range(1, p)]
    print(','.join(map(str, hot_potato(monkey, m-1))))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-03-17%20191825.png)



### 20018: 蚂蚁王国的越野跑

merge sort, http://cs101.openjudge.cn/practice/20018/

思路：



代码：

```python
import bisect
n = int(input())
s = [int(input()) for _ in range(n)]
temp = [0]*n


def sort_arr(arr, left, mid, right):
    i, j, k = left, mid+1, left
    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        temp[j] = arr[j]
        j += 1
        k += 1
    for i in range(left, right+1):
        arr[i] = temp[i]


def count(arr, left, mid, right):
    num = 0
    left_arr = arr[left:mid+1]
    for x in arr[mid+1: right+1]:
        num += bisect.bisect_left(left_arr, x)
    return num


def merge(arr, left, right):
    if left >= right:
        return 0
    num = 0
    mid = (left + right) // 2
    num += merge(arr, left, mid)
    num += merge(arr, mid + 1, right)
    num += count(arr, left, mid, right)
    sort_arr(arr, left, mid, right)
    return num


print(merge(s, 0, n-1))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-03-21%20115753.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

约瑟夫问题NO.2中，我尝试使用循环链表代替队列,本地测试的结果表明，构造链表所需的时间比队列长，但遍历链表删除特定节点所需的时间要短与队列。

新学会了归并排序。









