
A `transform_if` implementation along with test harness.  
As can be read from this [stack_overflow answer](https://stackoverflow.com/a/23579922/2303176), there are several reasons why `transform_if` is not provided by the standard library in C++.  
But nevertheless, we should implement our versions of this algorithm, for better abstractions.

    #include <chrono>
    #include <numeric>
    #include <iostream>
    #include <vector>
    #include <algorithm>
    #include <boost/iterator/transform_iterator.hpp>
    #include <boost/iterator/function_output_iterator.hpp>
    #include <boost/optional.hpp>
    #include <boost/lexical_cast.hpp>

    namespace nitul
    {
        template<typename UnderlyingType>
        auto from_optional(boost::optional<UnderlyingType> const & source)
            -> UnderlyingType
        {
            if( source ) {
                return source.get();
            } else {
                throw std::runtime_error{"Cannot extract value from boost::none"};
            }
        }

        template<typename InputIt, typename OutputIt, typename UnaryPredicate, typename SourceToIntermediateConverter, typename IntermediateToTargetConverter>
        void transform_if(InputIt                          first
                         ,InputIt                          last
                         ,OutputIt                         d_first
                         ,UnaryPredicate                && pred
                         ,SourceToIntermediateConverter && from_source
                         ,IntermediateToTargetConverter && to_target)
        {
            using intermediate_value_type = decltype(from_source(*first));

            auto const to_target_wrapper = [d_first, to_target](intermediate_value_type const & value) mutable {
                *d_first = to_target(value);
            };

            std::copy_if(boost::make_transform_iterator(first, from_source)
                        ,boost::make_transform_iterator(last, from_source)
                        ,boost::make_function_output_iterator(to_target_wrapper)
                        ,pred);
        }

        template< class T > struct remove_optional;
        template< class T > struct remove_optional                      {typedef T type;};
        template< class T > struct remove_optional<boost::optional<T>>  {typedef T type;};

        template<typename InputIt, typename OutputIt, typename TransformOptional>
        void transform_if(InputIt              first
                         ,InputIt              last
                         ,OutputIt             d_first
                         ,TransformOptional && trans_opt)
        {
            using option_type = decltype(trans_opt(*first));
            using output_type = typename remove_optional<option_type>::type;

            transform_if(first
                        ,last
                        ,d_first
                        ,[](option_type const & data) { return (data); }
                        ,trans_opt
                        ,from_optional<output_type>);
        }

        auto call_transform(std::vector<std::string> const & input, std::vector<int> & output)
            -> void
        {
            auto const transform_optional = [](std::string const & src) -> boost::optional<int> {
                try {
                    return boost::lexical_cast<int>(src);
                } catch(...) {
                    return boost::none;
                }
            };
    #if 1
            transform_if(input.begin(), input.end(), std::back_inserter(output), transform_optional);
    #else
            transform_if(input.begin()
                        ,input.end()
                        ,std::back_inserter(output)
                        ,[](boost::optional<int> const & data) {
                            return ( data ) ? true : false;
                         }
                        ,transform_optional
                        ,from_optional<int>);
    #endif
        }
    }

    namespace abhinav
    {
        template<typename InputIt, typename OutputIt, typename TransformOptional>
        void transform_if(InputIt              first
                         ,InputIt              last
                         ,OutputIt             d_first
                         ,TransformOptional && trans_opt)
        {
            using option_type = decltype(trans_opt(*first));
            auto optional_target = std::vector<option_type>{};

            std::copy_if(boost::make_transform_iterator(first, trans_opt)
                        ,boost::make_transform_iterator(last , trans_opt)
                        ,std::back_inserter(optional_target)
                        ,[](option_type const & data) {
                            return (data);
                        }
                );

            std::transform(std::make_move_iterator(optional_target.begin())
                          ,std::make_move_iterator(optional_target.end())
                          ,d_first
                          ,[](option_type && data) {
                            return data.get();
                        }
                );
        }

        auto call_transform(std::vector<std::string> const & input, std::vector<int> & output)
            -> void
        {
            auto const transform_optional = [](std::string const & src) -> boost::optional<int> {
                try {
                    return boost::lexical_cast<int>(src);
                } catch(...) {
                    return boost::none;
                }
            };

            transform_if(input.begin(), input.end(), std::back_inserter(output), transform_optional);
        }
    }

    auto generate_input()
        -> std::vector<std::string>
    {
        auto result = std::vector<std::string>{};
        auto init = std::vector<int>(10000000);
        std::iota(init.begin(), init.end(), -5000000);
        std::transform(init.begin()
                      ,init.end()
                      ,std::back_inserter(result)
                      ,[](int t) { return std::to_string(t); });
        return result;
    }

    int main()
    {
        auto input = generate_input();
        std::cout << "\nTest => converting [" << input.size() << "] strings to numbers\n";

        auto a_output = std::vector<int>{};
        auto n_output = std::vector<int>{};

        auto n_begin = std::chrono::steady_clock::now();
        nitul::call_transform(input, n_output);
        auto n_end = std::chrono::steady_clock::now();
        std::cout << "[nitul  ] time elapsed => [" << std::chrono::duration_cast<std::chrono::microseconds>(n_end - n_begin).count() << "] microseconds\n";

        auto a_begin = std::chrono::steady_clock::now();
        abhinav::call_transform(input, a_output);
        auto a_end = std::chrono::steady_clock::now();
        std::cout << "[abhinav] time elapsed => [" << std::chrono::duration_cast<std::chrono::microseconds>(a_end - a_begin).count() << "] microseconds\n";


        return 0;
    }
