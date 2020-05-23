> A programmer without rotate is like a handyman without a screwdriver.  
> It is quite surprising how few people know about rotate and how few know why and how to use it.  
> 
> Reverse, rotate and random shuffle are the most important examples of index-based permutations, that is, permutations that rearrange a sequence according to the original position of the elements without any consideration for their values.  
>  
> Alexander Stepanov (http://stepanovpapers.com/notes.pdf, Lecture 19. Rotate)

In this article we would introduce a simple trick to identify when rotate can be useful and how to use it.  

Unfortunately the return value was not returned by `std::rotate` until C++11. 

    template< class ForwardIt >
    void rotate( ForwardIt first, ForwardIt n_first, ForwardIt last );      // (until C++11)
    
    template< class ForwardIt >
    ForwardIt rotate( ForwardIt first, ForwardIt n_first, ForwardIt last ); // (since C++11)

 > I also observed that in many cases when I used rotate I would immediately need to compute the position of the new rotation point, that is, the position where the beginning of the first sub-range ended. Assuming that we are dealing with random-access iterators, after rotate(f, m, l), I would frequently need f + (l – m). Computing it for random-access iterators is trivial, but it is really slow for linked structures. By the way, if we return such an iterator we obtain that
rotate(f, rotate(f, m, l), l) is an identity permutation. While we cannot use it as a definite proof, the existence of such a property makes me comfortable that we are on the right path. Because of this property, I will call m the old rotation point and the result of rotate – the new rotation point.

The one-liner to remember `std::rotate` is :
> If you see cut-paste, it is std::rotate.

So if you see any use case, where you have to cut the data and paste it somewhere, it can be easily achieved by `std::rotate`.  

In short, we can re-interpret it as :

    std::rotate(new_paste_location, cut_start_location, cut_end_location) -> cursor_current_location

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

    // std::rotate(new_paste_location, cut_start_location, cut_end_location) -> cursor_current_location
    // std::rotate(0                 , 7                 , 14              ) -> 7
    ____________________________________________________________________
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14   |
    ____________________________________________________________________
    | , | B | A | D | O | L | A | A | B | H |  I |  N |  A |  V | end()|
    ____________________________________________________________________
    // It returns 7 since cursor would be after 6 and before 7, which is 7 in our case.

Finally, we will cut the comma `,` and place it after `BADOLA`.  
Which can also be said as => we will cut `BADOLA` and paste it before the `,`

    // std::rotate(new_paste_location, cut_start_location, cut_end_location) -> cursor_current_location
    // std::rotate(0                 , 1                 , 7               ) -> 6
    ____________________________________________________________________
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14   |
    ____________________________________________________________________
    | B | A | D | O | L | A | , | A | B | H |  I |  N |  A |  V | end()|
    ____________________________________________________________________
    // It returns 6 since cursor would be after 5 and before 6, which is 6 in our case.

Which in code would look like -

    #include <iostream>
    #include <string>
    #include <algorithm>
    
    int main()
    {
        std::string name = "ABHINAV,BADOLA";
        std::cout << "name before rotate => " << name << "\n";
        
        auto comma_position = std::find(name.begin(), name.end(), ',');
        auto last_cursor = std::rotate(name.begin(), comma_position, name.end());
        std::rotate(name.begin(), std::next(name.begin()), last_cursor);
        
        std::cout << "name after  rotate => " << name << "\n";
        return 0;
    }

Output :

    name before rotate => ABHINAV,BADOLA
    name after  rotate => BADOLA,ABHINAV
    
    
> A few years back I was astonished when a leading STL expert told me that they discovered that they could use rotate to speed up a quadratic implementation of the insert member function. I assumed that it was self-evident.  
>   
> Alexander Stepanov
