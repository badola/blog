# Regular Types

This post is inspired from Alexander Stepanov's lectures and papers.  
Paper => http://stepanovpapers.com/DeSt98.pdf  
Talks => https://www.youtube.com/playlist?list=PLHxtyCq_WDLXryyw91lahwdtpZsmo4BGD  

By default the datatype defined in C++ is a **semi-regular** type.  
Properties of **semi-regular** type -  
1. construtor
1. destructor
1. copy constructor
1. copy assignment operator

    struct T
    {
        T() = default;
        T(int data) : _data(data) {}
        ~T() = default;
        T(const & T) = default;
        T(T&&) = default;

        T& operator =(T const &) = default;
        T& operator =(T&&) = default;

        // semi- regular

        friend bool operator == (T const & lhs, T const & rhs)
        {
            return lhs._data == rhs._data;
        }

        friend bool operator != (T const & lhs, T const & rhs)
        {
            return !(lhs == rhs);
        }
        // regular type

        friend bool operator < (T const & lhs, T const & rhs)
        {
            return lhs._data < rhs._data;
        }

        friend bool operator >= (T const & lhs, T const & rhs)
        {
            return !(lhs < rhs);
        }

        friend bool operator > (T const & lhs, T const & rhs)
        {
            return rhs < lhs;
        }

        friend bool operator <= (T const & lhs, T const & rhs)
        {
            return !(lhs > rhs);
        }
        // totally ordered

        private:
            int _data;
    };
    
