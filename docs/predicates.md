## Predicates
[Home Index](../README.md)  
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

