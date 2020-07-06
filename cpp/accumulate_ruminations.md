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
Better. That satisfies all the constraints (assuming `concat` is just there because of the missing constructor).
We implemented both versions (mutating and non-mutating), so please tell us your experience...what did you feel about going from mutating solution to non-mutating one.. 
as in how your brain was forced to rethink the structure of the solution..

Now, are you able to see the general structure of the solution which applies to hundreds of other problems which may seen unrelated at first? There is one function in C++ stdlib that does it. Identify it!

 `u_copy` is modified. So it fits the constraint that everything should be `const`?  

The `concat` function is just there to fill the gap of the missing constructor. Else, we could have used things like:
`vector<double> item_N_plus_1(item, items_N);`


The constraints were added to guide us to see the general structure of the problem.. **std::accumulate**

So lets now try to remodel the attempt at solving this problem using `std::accumulate`
And finally - 
```cpp
auto getRandoms(int N, R r)-> std::pair<std::vector<double>, R>
{
    std::vector<int> _(N);
    return std::accumulate(_.begin(), _.end(), std::make_pair(std::vector<double>{}, r), [](auto acc, auto _) {
        auto [v, r] = acc;
        auto [d, r1] = r.next();
        v.push_back(d); // this step is mutating, as we dont have the required constructor support: imagine it to be: vector<double> v1 { v, d };
        return std::make_pair(v, r1);
    });
}
```
It's completely natural. **std::accumulate** is the function which solves **all such problems**.

But we have not discussed the *properties* of the problems which can be solved by this function. *How* exactly do we identify other problems which is similar to this problem. Summing or multiplying are easier to identify, as we often see those examples. However, this random number problem appeared so *different* in the beginning, yet turned out to be similar to *summing* problems. 

So basically any operation that takes a seed value?  
Yes. That's the crux, though *seed* seems to be a very specific term, often used in the context of random number generators. But in general, yes, anything that *depends* on the previous sub-solution. That is, if you compute something which depends on the result of the computation of the same *smaller* problem... more like... *(N + 1)th step* depends on *Nth step*.

Is this basically the trick used to make a recursive call, tail recursive?  
Yes. Recursion is one structure that satisfies this. An astute observer will see that `std::accumulate` (or something similar) can be used to solve all recursive problems.

`std::accumulate` can be used to -
1. Find the nth fibonacci number
1. Get all cpp files given a directory or a list of directories
1. Reverse a string
1. Join a list of string
1. Any data transformation that requires left-fold or right-fold

We are **not** implying that you should use accumulate for all such problems simply because it can solve it. There are more specific algorithms designed to solve things efficiently. But knowing it as one possible solution is helpful, so you can choose it if no other easy solution available in the sight.
