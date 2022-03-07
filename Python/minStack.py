"""
https://leetcode.com/problems/min-stack/
Difficulty: Easy

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.


Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

Constraints:
-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
"""

class MinStack:
    """
    Stack works like plates on a barbell. 
    They follow the LIFO method. 
    """
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # append value into stack
        self.stack.append(val)
        return True

    def pop(self) -> None:
        # if len(stack) empty, there is nothing to pop
        if len(self.stack) < 0:
            print("Stack is empty!")
            return None
        # pop the last added element in the stack
        return self.stack.pop()

    def top(self) -> int:
        # if len(stack) empty, there is nothing to peek
        if len(self.stack) < 0:
            print("Stack is empty!")
            return None
        # return the top element in the stack
        return self.stack[-1]

    def getMin(self) -> int:
        # sort stack in ascending order (small -> big)
        return sorted(self.stack)[0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
