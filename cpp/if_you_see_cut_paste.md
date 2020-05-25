> A programmer without rotate is like a handyman without a screwdriver.
> It is quite surprising how few people know about rotate and how few know why and how to use it.
>
> Reverse, rotate and random shuffle are the most important examples of index-based permutations, that is, permutations that rearrange a sequence according to the original position of the elements without any consideration for their values.
>
> Alexander Stepanov (http://stepanovpapers.com/notes.pdf, Lecture 19. Rotate)

In this article we will learn about a simple trick to identify when rotate can be useful and how to use it. But first, let us have a look at the signature of `std::rotate`

```cpp
template< class ForwardIt >
void rotate( ForwardIt first, ForwardIt n_first, ForwardIt last );      // (until C++11)

template< class ForwardIt >
ForwardIt rotate( ForwardIt first, ForwardIt n_first, ForwardIt last ); // (since C++11)
```
Unfortunately, the return type of `std::rotate` was `void` until C++11. This shortcoming was noticed and addressed by Stepanov.  

In the book *From Mathematics to Generic Programming*, **Alexander Stepanov** and **Daniel Rose** describe a very simple yet powerful rule called **Law of Useful Return** :

> If you’ve already done the work to get some useful result, don’t throw it away.
> Return it to the caller.
> This may allow the caller to get some extra work done “for free”.

Therefore, since C++11, `std::rotate` returns an iterator to the new location of the element earlier pointed to by `first`, as it was already computed as a result of carrying out its main task &mdash; even though the return value may eventually be ignored by the caller if not needed.

    Initial orientation:
    (first, .. , n_first, .., last-1, |last|)

    Final orientation:
    (n_first, .., last-1, first, .., |last|) # note that last, as it isn't dereferenceable, is special and does not change its position
    

The element pointed to by `first` eventually ends up next to the element pointed to by `last-1`.
Therefore its new location is:

    first + ( (last - 1) - n_first + 1 )
    
    or, in simpler terms
    first + ( last - n_first )
`first + (last - n_first)` is the value returned by rotate since C++11.  
The examples below will show, how critical this **Law of Useful Return** can be.

So here is a one-liner to remember when `rotate` can be useful:
> **If you see cut-paste, it is rotate.**

(repeat it 3 times - "If you see cut-paste, it is rotate." - and you have already mastered rotate)

For ease of use, we can re-interpret rotate as:

    rotate(ForwardIt first, ForwardIt n_first, ForwardIt last) -> ForwardIt
as

    rotate(paste_location, cut_start_location, cut_end_location) -> cursor_location(after pasting)

So, if you have a use case where you have to **cut** data and **paste** it somewhere, it can be easily achieved by `rotate`.  
This power of `rotate` comes from the fact that all the elements cut, move together.

Let's strengthen our learning by taking an example.  
Suppose you are given a name in the format => `FirstName,LastName`  
You are required to transform it into => `LastName,FirstName`  

How would you go about doing it using cut and paste on a text editor?  
For our example, we will use the name => `ABHINAV,BADOLA`  

To make things simpler, lets index the data as well:

    ____________________________________________________________________
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14   |
    ____________________________________________________________________
    | A | B | H | I | N | A | V | , | B | A |  D |  O |  L |  A | end()|
    ____________________________________________________________________

First we will have to find the location of the comma (step #1).

    auto const comma_position = std::find(name.begin(), name.end(), ',');
    ____________________________________________________________________
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14   |
    ____________________________________________________________________
    | A | B | H | I | N | A | V | , | B | A |  D |  O |  L |  A | end()|
    ____________________________________________________________________
                                ↑
    // comma_position now points to 7th location

Then we will cut `,BADOLA` and paste it in front of `ABHINAV` (step #2).

    ____________________________________________________________________
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14   |
    ____________________________________________________________________
    | A | B | H | I | N | A | V | , | B | A |  D |  O |  L |  A | end()|
    ____________________________________________________________________
    ↑                           ↑                               ↑
    paste_location              cut_start_location              cut_end_location

    // std::rotate(paste_location, cut_start_location, cut_end_location) -> cursor_location
    // std::rotate(0             , 7                 , 14              ) -> 7
    ____________________________________________________________________
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14   |
    ____________________________________________________________________
    | , | B | A | D | O | L | A | A | B | H |  I |  N |  A |  V | end()|
    ____________________________________________________________________
                                ↑
                                cursor_location
    // The cursor_location returned would be 7 since the cursor would be after 6 and before 7
    // at the end of step #2.

Finally, we will cut the comma `,` and place it after `BADOLA`  (step #3).  
We may rephrase this as => cut `BADOLA` and paste it before the `,`

    ↓ paste_location
    ____________________________________________________________________
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14   |
    ____________________________________________________________________
    | , | B | A | D | O | L | A | A | B | H |  I |  N |  A |  V | end()|
    ____________________________________________________________________
        ↑                       ↑
        cut_start_location      cut_end_location/cursor_location

    // std::rotate(paste_location, cut_start_location, cut_end_location) -> cursor_location
    // std::rotate(0             , 1                 , 7               ) -> 6
    ____________________________________________________________________
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14   |
    ____________________________________________________________________
    | B | A | D | O | L | A | , | A | B | H |  I |  N |  A |  V | end()|
    ____________________________________________________________________
                            ↑
    // The cursor_location returned would be 6 since the cursor would be after 5 and before 6
    // at the end of step #3.

**Notice how we used the value returned by the rotate of (step #2) in the rotate of (step #3)**

In code this would look like -

    void swap_firstname_lastname(std::string & name) // in-place swap
    {
        auto const comma_position = std::find(name.begin(), name.end(), ',');               // step #1
        auto const cursor_location = std::rotate(name.begin(), comma_position, name.end()); // step #2
        std::rotate(name.begin(), std::next(name.begin()), cursor_location);                // step #3
    }

    void test()
    {
        auto name = std::string{"ABHINAV,BADOLA"};
        std::cout << name << '\n';    // ABHINAV,BADOLA
        swap_firstname_lastname(name);
        std::cout << name << '\n';    // BADOLA,ABHINAV
    }

The application of `std::rotate` is not only limited to string permutations, it may also be used with all the sequenced containers.
The discussion above applies to `std::vector`, `std::list`, `std::array`, etc. as well.

Want to move an element (or a group of elements) to the back of a vector, say `v`?
Let's start by visualizing this in terms of the trick applied in the previous example.

                                                 ↓ paste_location
    _____________________________________________________
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11   |
    _____________________________________________________
    | A | B | C | D | E | F | G | H | I | J |  K | end()|
    _____________________________________________________
        ↑                       ↑
        begin_of_items_to_move  end_of_items_to_move

    std::rotate(begin_of_items_to_move, end_of_items_to_move   , paste_location);
    i.e.
    std::rotate(std::next(v.begin())  , std::next(v.begin(), 7), v.end()       );
    _____________________________________________________
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11   |
    _____________________________________________________
    | A | H | I | J | K | B | C | D | E | F |  G | end()|
    _____________________________________________________
                        ↑
                        cursor_location    

`std::rotate` can also be used to move elements to the start of a vector.

    ↓ paste_location
    _____________________________________________________
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11   |
    _____________________________________________________
    | A | B | C | D | E | F | G | H | I | J |  K | end()|
    _____________________________________________________
                    ↑                       ↑
                    begin_of_items_to_move  end_of_items_to_move

    std::rotate(paste_location, begin_of_items_to_move, end_of_items_to_move     );
    i.e.
    std::rotate(v.begin()     , std::next(v.begin(), 4), std::next(v.begin(), 10));
    _____________________________________________________
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11   |
    _____________________________________________________
    | E | F | G | H | I | J | A | B | C | D |  K | end()|
    _____________________________________________________
                            ↑
                            cursor_location    

Using rotate as our *cut-paste* algorithm has a limitation.
It only works if the *paste_location* is towards the left of *cut_start_location*.

Essentially, `std::rotate` is a *left-rotate*.

    std::rotate(paste_location, cut_start_location, cut_end_location);
If you need a *right-rotate*, just reorder the arguments:

    std::rotate(cut_start_location, cut_end_location, paste_location);


We can create a high level abstration of the cut-paste algorithm using rotate which would be independent of the paste_location. This algorithm would, however, increase the requirement on the `Iterator` from `LegacyForwardIterator` to `LegacyRandomAccessIterator`.

    template<typename Iter>                  // Iter models LegacyRandomAccessIterator
    Iter cut_paste(Iter cut_start_location, Iter cut_end_location, Iter paste_location)
    {
        if (paste_location < cut_start_location)   // handles left-rotate
            return std::rotate(paste_location, cut_start_location, cut_end_location);

        if (cut_end_location < paste_location)     // handles right-rotate
            return std::rotate(cut_start_location, cut_end_location, paste_location);

        // else - no-operation required, there will be no change in the arrangement of data
        // return the cut_end_location, cause that is where our cursor should be if the operation was done
        return cut_end_location;
    }

Does this piece of code seem familiar?  
Exactly!  
This is the `slide` algorithm by Sean Parent, presented in his famous C++ Seasoning talk given at GoingNative 2013.  
You can read more about the slide algorithm at https://www.fluentcpp.com/2018/04/20/ways-reordering-collection-stl/
