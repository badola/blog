It is mandated that you should derive `!=` (not equal to) from `==` (equal to).
But most of the times it is not explained why.
This small post tries to capture the essense of it.

In general, the guiding principle is - Given an *expression* and its *negation*, both should not be *True* at the same time.
This leads to contradiction. And - once a contradiction has been asserted, any proposition (including their negations) can be inferred from it. This is known as deductive explosion.

As a demonstration of the [Principle of Explosion](https://en.wikipedia.org/wiki/Principle_of_explosion) (excerpt taken from Wikipedia), consider two contradictory statements – "All lemons are yellow" and "Not all lemons are yellow", 
and suppose that both are true. If that is the case, anything can be proven, e.g., the assertion that "unicorns exist", 
by using the following argument:
1. We know that "All lemons are yellow", as it has been assumed to be true.
1. Therefore, the two-part statement "All lemons are yellow OR unicorns exist” must also be true, since the first part is true.
1. However, since we know that "Not all lemons are yellow" (as this has been assumed), the first part is false, and hence the second part must be true, i.e., unicorns exist.

In C++, we define `!=` and `==` this as - 
```cpp
inline bool operator==(const X& lhs, const X& rhs){ /* do actual comparison */ }
inline bool operator!=(const X& lhs, const X& rhs){ return !(lhs == rhs); }
```
Notice, how we use the `==` in computing `!=`. This approach is important to avoid contradictions.
