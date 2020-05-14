C++17 comes with fold-expressions, and we need to learn to wield it.

    #include <iostream>
    #include <vector>
    #include <iterator>

    template<typename T>
    void print_vec(std::vector<T> const & v) {
        std::copy(v.begin(), v.end(), std::ostream_iterator<T>(std::cout, " "));
    }

    template<typename Container, typename... Args>
    void push_back_11(Container && con, Args && ... args)
    {
        auto unpack = { (con.push_back(std::forward<Args>(args)), 0)... };
        static_cast<void>(unpack);
    }

    template<typename Container, typename... Args>
    void push_back_17(Container && con, Args && ... args)
    {
        (con.push_back(std::forward<Args>(args)), ...);
    }

    int main()
    {
        auto v = std::vector<int>{};
        push_back_17(v, 8, 9, 3, 45, 1, -9, 0);
        push_back_11(v, 8, 9, 3, 45, 1, -9, 0);
        print_vec(v);
        return 0;
    }
