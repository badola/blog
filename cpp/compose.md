A generic `compose` function, to compose 2 or more functions.

```cpp
#include <iostream>

template<typename First>
auto compose(First && f)
{
    return f;
}

template<typename First, typename ... Others>
auto compose(First && f, Others && ... others)
{
    return [=](auto && ...args) {
        return f(compose(others...)(args...));
    };
}

auto cow(int) -> char
{
    return 'a';
}

auto moo(char) -> double
{
    return 1.23;
}

int main()
{
    std::cout << moo(cow(5)) << std::endl;
    auto moo_cow = compose(moo, cow);
    std::cout << moo_cow(5) << std::endl;
    
    auto moo_cow2 = compose([](auto a) { return a * a; }, []() {return 5;});
    std::cout << moo_cow2() << std::endl;
}
```
