## Predicates
[Home Index](/README.md)  
[C++ Home Index](/cpp/index.md)  

As [wikipedia](https://en.wikipedia.org/wiki/Predicate_(mathematical_logic)) states :
> In mathematical logic, a predicate is commonly understood to be a Boolean-valued function P: X→ {true, false}, called the predicate on X.  
>
> Informally, a predicate is a statement that may be true or false depending on the values of its variables.  
> It can be thought of as an operator or function that returns a value that is either true or false.  
>
> For example, predicates are sometimes used to indicate set membership: when talking about sets, it is sometimes inconvenient or impossible to describe a set by listing all of its elements.  
> Thus, a predicate P(x) will be true or false, depending on whether x belongs to a set.

So for the programming literates, who don't understand mathematics much(just like me) -   
We will assume **predicate** is a **function** which returns a **boolean** value.

So based on this assumption let us create our first predicate : `is_even(int)`

```cpp
// is_even predicate
bool is_even(int num) 
{ 
    return !(num % 2); 
}
```
`is_even` is a predicate, that takes an integer and tell whether it is even or not.

A predicate is used in decision making.  
A powerful system needs to have well designed **atomic** predicates.  
We will observe it soon why atomicity is important, and how composition is going to be our best friend in future.

#### Why predicates are important?
[Higher Order Functions](/cpp/higher_order_functions.md) love predicates.  
Higher order fundtions have more utility when their interface accepts a predicate.

By doing so, the responsibility is segregated, hence we are able to write better generic components.  
Responsibility of predicate : _decision making_  
Responsibility of higher order function : _do some work based on the decision taken by the predicate_  

[`std::sort`](https://en.cppreference.com/w/cpp/algorithm/sort) takes a `<`(less than) operator as a predicate.  

A lot of C++ [algorithms](https://en.cppreference.com/w/cpp/header/algorithm) work on predicates.  
Such as-  
[`std::count_if`](https://en.cppreference.com/w/cpp/algorithm/count)  
[`std::all_of, std::any_of, std::none_of`](https://en.cppreference.com/w/cpp/algorithm/all_any_none_of)  
[`std::find_if, std::find_if_not`](https://en.cppreference.com/w/cpp/algorithm/find)  
[`std::is_partitioned`](https://en.cppreference.com/w/cpp/algorithm/is_partitioned)

There are many more and by now we are starting to realise that powerful systems require predicates to work in a generic fashion.
