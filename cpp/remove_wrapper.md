This is a very simple code to remove all wrappers on top of an object.  
This is a generic utility and can be specialized for types such as - `boost::optional`, `std::optional`, etc. to get the underlying type.  
This example only gets the first type, as can be seen from the example of `std::pair<int, std::string>{}` -> `int`.

    #include <iostream>
    #include <vector>
    #include <boost/optional.hpp>

    template <typename T> 
    struct remove_wrapper {
        using type = T;
    };

    template <typename First, 
              template <typename, typename ...> class Wrapper,
              typename ... Others>
    struct remove_wrapper<Wrapper<First, Others...>> {
        using type = typename remove_wrapper<First>::type;
    };

    template <typename check>
    auto cow(check a)
        -> void
    {
        using t = typename remove_wrapper<check>::type;
        t y = 5;
        std::cout << y;
    }

    int main()
    {
        cow ( boost::optional<boost::optional<int>>{});
        cow ( std::pair<int, std::string>{}          );
        cow ( std::vector<int>{}                     );
        return 0;
    }
