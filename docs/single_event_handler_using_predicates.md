## single event handler
[Home Index](/README.md)  
Let us have a function, your event handler which will take a [`predicate`](/docs/predicates.md) and two functions namely `on_sucess` and `on_error`.

If the `test_predicate` returns true then `on_success` shall be invoked, else `on_error` would be invoked.

```cpp
// A generic single_event_handler
template<typename Predicate, typename OnSucess, typename OnError>
void single_event_handler (Predicate && test_predicate,
                           OnSucess  && on_success,
                           OnError   && on_error)
{
    if( test_predicate() )
        on_success();
    else
        on_error();
}
```

And now our caller side.  
Here we have 3 functions that we want to fit into this pattern.

```cpp
bool is_even(int num) { return !(num % 2); }                     // predicate
void on_even_found() { std::cout << "Number passed is even\n"; } // on_success
void on_odd_found() { std::cout << "Number passed is odd\n"; };  // on_error
```

But as you can see, the `is_even` function does not fit into the signature of `test_predicate`.  
`is_even(int)` takes a single argument, while `test_predicate()` takes none.

So how do we fix this ?

We wrap it into one more function and/or lambda, and then pass it.

> Guiding Principle : **Every problem can be solved by adding one more layer.**

```cpp
// wrap it in another function or lambda
auto is_5_even = []() { return is_even(5); };
auto is_4_even = []() { return is_even(4); };
```

And now once all the pieces of our puzzle is ready, we create our own event handler.
```cpp
// caller side - pair the final structure
single_event_handler(is_5_even, on_even_found, on_odd_found);
single_event_handler(is_4_even, on_even_found, on_odd_found);
```

Now this code can be implemented in pre-C++11, by using bind and function pointer.  
Sadly `std::bind` and `std::function` were introduced in C++11 and for pre-C++11 you would have to use other alternatives such as boost library.

Moreover, another wrapper can be written on top of `single_event_handler` which can manage multiple events at once.  
But we will have to create another function `register_event` so that it can be used effectively.  
We will cover it in some other lecture.

Here is the full working code (compiled using `g++ -std=c++11`)
```cpp
#include <iostream>

template<typename Predicate, typename OnSucess, typename OnError>
void single_event_handler (Predicate && test_predicate,
                           OnSucess  && on_success,
                           OnError   && on_error)
{
    if( test_predicate() )
        on_success();
    else
        on_error();
}

bool is_even(int num) { return !(num % 2); }
void on_even_found() { std::cout << "Number passed is even\n"; }
void on_odd_found() { std::cout << "Number passed is odd\n"; };

int main()
{
    // caller side
    auto is_5_even = []() { return is_even(5); };
    auto is_4_even = []() { return is_even(4); };

    single_event_handler(is_5_even, on_even_found, on_odd_found);
    single_event_handler(is_4_even, on_even_found, on_odd_found);

    return 0;
}
```
