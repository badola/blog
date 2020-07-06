Imagine that you have a pure random number generator... by pure, it is meant that if you have a random number generator R, you can use it to get the next random number..
and it'll return the same number every time you use the same R. So in order to get different next number, if you have to use a different R. So the API is that `R.next()*`
returns a pair `int, newR` .. `newR` is different from `R` so that if you use it, it'll return a different number..

The description of the random number generator is clear? I hope so.

Now the question is: how would you use it to generate a list of N random numbers? The question is not very hard, it can be done quickly.
So let's do that.. then we'll add more constraints..

Let me add an example to explain this..using python:
```py
   a, R1 = R.next()
   b, R2 = R.next()

   assert a == b     
   assert R1 == R2   
   assert R != R1
```
But:
```py   
   a, R1 = R.next()
   b, R2 = R1.next()

   assert a != b     
   assert R1 != R2
```

The python example is just for the illustration. But let's do the question in statically typed language.. to truly get the general picture.

So `R` is random number generator which takes seed to generate next R and random  number?  
It does not take seed as such. You can think it is a seed itself, as well as generator.  
Every time the same R will generate the same R1?  
Yes. It's *pure*.

A python implementation - 
```py
def get_randoms(R, nums, count):
if count==0:return
n,r=R.next()
nums.append(n)
get_randoms(r,nums,count-1)
```

If it forms series den it won't be random. Then it defines a constant series based on the first R, like a AP or GP?  
Yes. Constant but random series. Same R => Same series.  
Series as in a sequence of numbers, not necessarily that the numbers are related. You cannot find mathematically pattern in that..
R could generate like  3949, 2, -193, 494, 283, -993, -94884, 38484.. There is no pattern at all. 
If you use the same starting R, it'll give you same series everytime. That is how - it is pure.

R itself does not generate the series.. it generate just one number, and the next R' which you can use further  ... Anyone interested in the problem? 

One constraint is the static language (though it is not a constraint as such) and possibly can be ignored (will see if dynamic languages make it too dynamic), 
as the above given python solution will work for static languages as well, without any much difficult. However, it mutates states.  
So the other constraint is that.. you cannot modify any value at any time..
The python solution is mutating at this line: `nums.append(n)`

It is supposed to return a series of n random numbers without having any state?  
Yes. Generate n random numbers from the given R, so the function should return the a list of, say, double, and the last (new) R .

So the function signature will be this:
```haskell
getRandoms :: Int -> R -> ([Double], R)
```
In C++:
```cpp
auto getRandoms(R r, int N) -> std::pair<std::vector<double>, R>
```

First lets create the test harness - 
```cpp
#include <iostream>
#include <string>
#include <vector>

template<typename T>
std::ostream& operator<<(std::ostream& os, const std::vector<T>& vec)
{
    for (auto& el : vec)
        os << el << ',';
    return os;
}

template<typename Random>
auto next_impl(Random const & r) -> std::pair<double, Random>
{
    auto curr_val = r.val;
    return {curr_val, Random{curr_val + 1.098}};
}

struct R
{
    R(double val) : val(val) {}
    auto next() {
        return next_impl(*this);
    }
    double val;
};


int main()
{
    std::vector<std::string> vec = {
        "Hello", "from", "GCC", __VERSION__, "!" 
    };
    auto r = R(9.756);
    auto result = getRandoms(5, r);
    std::cout << result.first << std::endl;
    auto result2 = getRandoms(7, result.second);
    std::cout << result2.first << std::endl;
}
```

First naive attempt at **getRandoms**:
```cpp
auto getRandoms(int N, R r)
    -> std::pair<std::vector<double>, R>
{
    auto random_numbers = std::vector<double>{};
    auto r_last = r;
    while(N-- > 0)
    {
        auto [random_val, r_next] = r_last.next();
        random_numbers.push_back(std::move(random_val));
        r_last = r_next;
    }
    return {std::move(random_numbers), r_last};
}
```

This implementation of **getRandoms** modifies states... many states.
Now lets assume *everything* is `const`. LITERALLY everything in your sight.
If we try to do it assuming that.. then a lot of structural properties will come on the surface, we'll be able to see how general the solution is!

So lets try again, considering everything is `const`
```cpp
template<typename T>
auto concat(T const & t, std::vector<T> u_copy) -> std::vector<T> {
    u_copy.insert(u_copy.begin(), t);
    return u_copy;
}

auto getRandoms(int const & N, R const & r)
    -> std::pair<std::vector<double>, R>
{
    if (N <= 0)
        return {std::vector<double>{}, r};
        
    auto const [r_value, next_r] = r.next();
    auto const [init, next_r2] = getRandoms(N - 1, next_r);
    return { concat(r_value, init), next_r2};
}
```
