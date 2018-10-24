# Regular Types

This post is inspired from Alexander Stepanov's lectures and papers.  
Paper => http://stepanovpapers.com/DeSt98.pdf  
Talks => https://www.youtube.com/playlist?list=PLHxtyCq_WDLXryyw91lahwdtpZsmo4BGD  

By default the datatype defined in C++ is a **semi-regular** type.  

Properties of **semi-regular** type -  
- construtor
- destructor
- copy constructor
- copy assignment operator
- move constructor (since C++11)
- move assignment operator (since C++11)

        struct T  
        {
            T() = default;                      // constructor
            T(int data) : _data(data) {}        // constructor
            ~T() = default;                     // destructor
            T(const & T) = default;             // copy constructor
            T(T&&) = default;                   // move constructor
            T& operator =(T const &) = default; // copy assignment
            T& operator =(T&&) = default;       // move assignment
            
            // above are the properties of semi-regular type
            
            private:
                int _data;
        };

Properties of **regular** type - 
 - All properties of **semi-regular** type
 - equality operator
 - inequality operator

        struct T  
        {
            T() = default;                      // constructor
            T(int data) : _data(data) {}        // constructor
            ~T() = default;                     // destructor
            T(const & T) = default;             // copy constructor
            T(T&&) = default;                   // move constructor
            T& operator =(T const &) = default; // copy assignment
            T& operator =(T&&) = default;       // move assignment
            
            // above are the properties of semi-regular type
            
            friend bool operator == (T const & lhs, T const & rhs) // equality operator
            {
                return lhs._data == rhs._data;
            }

            friend bool operator != (T const & lhs, T const & rhs) // inequality operator
            {
                return !(lhs == rhs);
            }
            
            // above are the properties of regular type
            
            private:
                int _data;
        };

Properties of **totally ordered** type - 
 - All properties of **regular** type
 - less-than operator
 - less-than-or-equal operator
 - greater-than operator
 - greater-than-or-equal operator

        struct T  
        {
            T() = default;                      // constructor
            T(int data) : _data(data) {}        // constructor
            ~T() = default;                     // destructor
            T(const & T) = default;             // copy constructor
            T(T&&) = default;                   // move constructor
            T& operator =(T const &) = default; // copy assignment
            T& operator =(T&&) = default;       // move assignment
            
            // above are the properties of semi-regular type
            
            friend bool operator == (T const & lhs, T const & rhs) // equality operator
            {
                return lhs._data == rhs._data;
            }

            friend bool operator != (T const & lhs, T const & rhs) // inequality operator
            {
                return !(lhs == rhs);
            }
            
            // above are the properties of regular type

            friend bool operator < (T const & lhs, T const & rhs) // less-than operator
            {
                return lhs._data < rhs._data;
            }

            friend bool operator >= (T const & lhs, T const & rhs) // greater-than-or-equal operator
            {
                return !(lhs < rhs);
            }

            friend bool operator > (T const & lhs, T const & rhs) // greater-than operator
            {
                return rhs < lhs;
            }

            friend bool operator <= (T const & lhs, T const & rhs) // less-than-or-equal operator
            {
                return !(lhs > rhs);
            }
            // totally ordered

            private:
                int _data;
        };
    
