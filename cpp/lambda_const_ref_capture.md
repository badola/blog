### lambda links and thoughts

C++ Standard Committee:
 - http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2012/n3424.pdf
 - http://en.cppreference.com/w/cpp/language/lambda
 

Stackoverflow:
 - https://stackoverflow.com/questions/50779049/should-we-capture-by-const-reference-in-lambda
 - http://en.cppreference.com/w/cpp/language/lambda
 
 Related Emails:
  - https://groups.google.com/a/isocpp.org/forum/#!topic/std-proposals/0UKQw9eo3N0
  - 
 
Proposed Solution -
```cpp
int x = 10;
auto c = [const & x](){ std::cout << x << std::endl; }; 
```

Current(C++17) implementation workaround -
```cpp
int x = 10;
auto c = [ &x = std::as_const(x) ] () { std::cout << x << std::endl; };
```

C++11/C++14 implementation workaround -
```cpp 
int x = 10;
auto const & crx = x;
auto c = [ &crx ] () { std::cout << crx << std::endl; };
```
