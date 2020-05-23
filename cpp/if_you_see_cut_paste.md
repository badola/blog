> A programmer without rotate is like a handyman without a screwdriver.  
> It is quite surprising how few people know about rotate and how few know why and how to use it.  
> 
> Reverse, rotate and random shuffle are the most important examples of index-based permutations, that is, permutations that rearrange a sequence according to the original position of the elements without any consideration for their values.  
>  
> Alexander Stepanov (http://stepanovpapers.com/notes.pdf, Lecture 19. Rotate)

In this article we would introduce a simple trick to identify when rotate can be useful and how to use it.  
The article would be incomplete without the critical insights provided by Alex, when he was designing and teaching `rotate` to others.

But first, let us have a look at the signature of `std::rotate`

    template< class ForwardIt >
    void rotate( ForwardIt first, ForwardIt n_first, ForwardIt last );      // (until C++11)
    
    template< class ForwardIt >
    ForwardIt rotate( ForwardIt first, ForwardIt n_first, ForwardIt last ); // (since C++11)

Unfortunately, the return type of `std::rotate` was `void` until C++11.  
This shortcoming was also noticed and addressed by Alex. In his own words -  
> I also observed that in many cases when I used rotate I would immediately need to compute the position of the **new rotation point**, that is, the position where the beginning of the first sub-range ended.  
> Assuming that we are dealing with random-access iterators, after `rotate(f, m, l)`, I would frequently need `f + (l – m)`.  
> Computing it for random-access iterators is trivial, but it is really slow for linked structures.  
> By the way, if we return such an iterator we obtain that `rotate(f, rotate(f, m, l), l)` is an identity permutation.  
> While we cannot use it as a definite proof, the existence of such a property makes me comfortable that we are on the right path.  
> Because of this property, I will call `m` the *old rotation point* and the result of rotate – *the new rotation point*.  
> The problem was that while I knew what was needed, I did not know how to implement it without incurring a performance penalty for the three-reverses rotate.  
> This is why when I wrote the specification of rotate for STL in 1994, it was returning `void`.

In the book *From Mathematics to Generic Programming*, Alexander Stepanov and Daniel Rose then go on to describe the **Law of Useful Return** :  
> If you’ve already done the work to get some useful result, don’t throw it away.  
> Return it to the caller.  
> This may allow the caller to get some extra work done “for free”.  

Therefore, since C++11, `std::rotate` returns an iterator to the new position of the previously-last iterator.  
Maybe it won’t be used, but it was already computed anyway.  
As we will see now, in the below examples, how critical this "Law of Useful Return" can be.  
It also completes the interface of `std::rotate` by allowing identity permutation.

The one-liner to remember `std::rotate` is :
> **If you see cut-paste, it is std::rotate.**  

(repeat it 3 times - "If you see cut-paste, it is std::rotate." - and you have already mastered rotate)

So, if you see any use case where you have to cut the data and paste it somewhere, it can be easily achieved by `std::rotate`.  
The power of `rotate` comes from the fact that all elements move together.

In short, we can re-interpret rotate :

    std::rotate(ForwardIt first, ForwardIt n_first, ForwardIt last ) -> ForwardIt 
as

    std::rotate(paste_location, cut_start_location, cut_end_location) -> cursor_current_location

So lets learn by taking an example.  
Suppose you are given a name in the order => `FirstName,LastName`  
You are required to transform it into => `LastName,FirstName`  

How would you go about doing it using cut and paste on a text editor?  
For our example, we will use the name => `ABHINAV,BADOLA`   

For our ease of understanding, lets index the data as well:

    ____________________________________________________________________
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14   |
    ____________________________________________________________________
    | A | B | H | I | N | A | V | , | B | A |  D |  O |  L |  A | end()|
    ____________________________________________________________________

First we will have to find the location of comma.

    auto comma_position = std::find(name.begin(), name.end(), ',');
    // comma_position now points to 7th location

Then we will cut `,BADOLA` and paste it in front of `ABHINAV`

    // std::rotate(paste_location, cut_start_location, cut_end_location) -> cursor_current_location
    // std::rotate(0             , 7                 , 14              ) -> 7
    ____________________________________________________________________
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14   |
    ____________________________________________________________________
    | , | B | A | D | O | L | A | A | B | H |  I |  N |  A |  V | end()|
    ____________________________________________________________________
                                ↑
    // It returns 7 since cursor would be after 6 and before 7, which is 7 in our case.

Finally, we will cut the comma `,` and place it after `BADOLA`.  
Which can also be said as => we will cut `BADOLA` and paste it before the `,`

    // std::rotate(paste_location, cut_start_location, cut_end_location) -> cursor_current_location
    // std::rotate(0             , 1                 , 7               ) -> 6
    ____________________________________________________________________
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14   |
    ____________________________________________________________________
    | B | A | D | O | L | A | , | A | B | H |  I |  N |  A |  V | end()|
    ____________________________________________________________________
                            ↑
    // It returns 6 since cursor would be after 5 and before 6, which is 6 in our case.

Which in code would look like -
    
    void swap_firstname_lastname(std::string & name) // in-place swap
    {
        auto comma_position = std::find(name.begin(), name.end(), ',');
        auto cursor_current_location = std::rotate(name.begin(), comma_position, name.end());
        std::rotate(name.begin(), std::next(name.begin()), cursor_current_location);
    }
    
    void test()
    {
        auto name = std::string{"ABHINAV,BADOLA"};
        std::cout << name ;    // ABHINAV,BADOLA
        swap_firstname_lastname(name);
        std::cout << name ;    // BADOLA,ABHINAV
    }   

`std::rotate` is not only limited to string permutations but also to all sequenced containers alike.  
So all of our above discussion applies to `std::vector` as well.

> A few years back I was astonished when a leading STL expert told me that they discovered that they could use rotate to speed up a quadratic implementation of the insert member function. I assumed that it was self-evident.  
>   
> Alexander Stepanov


