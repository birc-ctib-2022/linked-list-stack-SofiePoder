"""A linked list implementation of a stack."""

from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, TypeVar, Optional

T = TypeVar('T')


@dataclass
class Link(Generic[T]):
    """A link in a linked list."""

    head: T
    tail: List[T]


List = Optional[Link[T]]


class Stack(Generic[T]):
    """A stack of elements of (generic) type T."""

    def __init__(self) -> None:
        """Create a new stack of values of type T."""
        self.stack = None

    def push(self, x: T) -> None: 
        """Push x on the top of this stack."""
        self.stack = Link(x,self.stack)
        return self.stack

    def top(self) -> T:
        """Return the top of the stack."""
        return self.stack.head

    def pop(self) -> T: #not working
        """Pop the top element off the stack and return it."""
        
        if self.stack.head == None:
            return None
        else:
            self.stack.head = self.stack.tail
        return self.stack.head
        

    def is_empty(self) -> bool:
        """Test if the stack is empty."""
        if self.stack == None:
            return "stack is empty"
        else:
            return "stack is not empty"



my_stack = Stack()
my_stack.push(1)
print(my_stack.push(2))

print(my_stack.top())

print(my_stack.pop())

print(my_stack.pop())

new_stack = Stack()
print(new_stack.is_empty())




