```cpp
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>

struct _4th{};
struct _3rd: _4th{};
struct _2nd: _3rd{};
struct _1st: _2nd{};
using overload_selector = _1st;

template<typename T>
auto print(std::ostream & os, T const & elem) -> void;

template<typename T>
auto print_impl(std::ostream & os, T const & elem, _1st _)
    -> decltype(os<<elem, void())
{
    os << elem; // final thing
}

template<typename IteratorCategory>
auto print_impl(std::ostream & os, IteratorCategory const & elem, _2nd _)
    -> decltype(elem.begin(), elem.end(), void())
{
    os << "[";
    for (auto const & item : elem) {
        print(os, item);
        os << ",";
    }
    os << "]";
}

template<typename T, typename U>
auto print_impl(std::ostream & os, std::pair<T, U> const & elem, _3rd _)
    -> decltype(elem.first, elem.second, void())
{
    os << "(";
    print(os, elem.first);
    os << ",";
    print(os, elem.second);
    os << ")";
}

template<typename T>
auto print(std::ostream & os, T const & elem)
    -> void
{
    print_impl(os, elem, overload_selector{});
}

// SFINAE -> Substitution Failure Is Not An Error
int main()
{
    print(std::cout, typeid(overload_selector{}).name()); std::cout << std::endl;
    
    print(std::cout, 23); std::cout << std::endl;
    print(std::cout, "23"); std::cout << std::endl;
    print(std::cout, 2.3); std::cout << std::endl;
    print(std::cout, 23l); std::cout << std::endl;
    print(std::cout, std::string{"abc"}); std::cout << std::endl;
    
    std::vector<int> nums {2, 3, 4, 5, 6, 7, 8 };
    print(std::cout, nums); std::cout << std::endl;

    std::array<int, 8> nums_a {2, 3, 4, 5, 6, 7, 8, 9};
    print(std::cout, nums_a); std::cout << std::endl;

    std::set<char> chars {'2', '3', 'a', 'b'};
    print(std::cout, chars); std::cout << std::endl;
    
    std::pair<int, int> square {3, 9};
    print(std::cout, square); std::cout << std::endl;
    std::vector<std::pair<int, int>> squares {{2, 4}, {3, 9}, {4, 16}};
    print(std::cout, squares); std::cout << std::endl;
    
    using vec_type = decltype(nums);
    std::pair<vec_type, vec_type> ranges {nums, nums};
    print(std::cout, ranges); std::cout << std::endl;
    
    std::map<int, std::string> mapping {{2, "second"}, {3, "three"}, {4, "four"}};
    print(std::cout, mapping); std::cout << std::endl;
}

```
