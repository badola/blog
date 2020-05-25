> A programmer without rotate is like a handyman without a screwdriver.
> It is quite surprising how few people know about rotate and how few know why and how to use it.
>
> Reverse, rotate and random shuffle are the most important examples of index-based permutations, that is, permutations that rearrange a sequence according to the original position of the elements without any consideration for their values.
>
> Alexander Stepanov (http://stepanovpapers.com/notes.pdf, Lecture 19. Rotate)

In this article we will learn about a simple trick to identify when rotate can be useful and how to use it. But first, let us have a look at the signature of `std::rotate`

```cpp
template<class ForwardIt>
void rotate(ForwardIt first, ForwardIt n_first, ForwardIt last);      // (until C++11)

template<class ForwardIt>
ForwardIt rotate(ForwardIt first, ForwardIt n_first, ForwardIt last); // (since C++11)
```
Unfortunately, the return type of `std::rotate` was `void` until C++11. This shortcoming was noticed and addressed by Stepanov.  

In the book *From Mathematics to Generic Programming*, **Alexander Stepanov** and **Daniel Rose** describe a very simple yet powerful rule called **Law of Useful Return** :

> If you’ve already done the work to get some useful result, don’t throw it away.
> Return it to the caller.
> This may allow the caller to get some extra work done “for free”.

Therefore, since C++11, `std::rotate` returns an iterator to the new location of the element earlier pointed to by `first`, as it was already computed as a result of carrying out its main task &mdash; even though the return value may eventually be ignored by the caller if not needed.
```
Initial orientation:
(first, .. , n_first, .., last-1, |last|)

Final orientation:
(n_first, .., last-1, first, .., |last|) # note that last, as it isn't dereferenceable, is special and does not change its position
```    

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
```
rotate(ForwardIt first, ForwardIt n_first, ForwardIt last) -> ForwardIt
```
as
```
rotate(paste_begin, cut_begin, cut_end) -> paste_end
```
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
    paste_begin                 cut_begin                       cut_end

    // std::rotate(paste_begin, cut_begin, cut_end) -> paste_end
    // std::rotate(0          , 7        , 14     ) -> 7
    ____________________________________________________________________
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14   |
    ____________________________________________________________________
    | , | B | A | D | O | L | A | A | B | H |  I |  N |  A |  V | end()|
    ____________________________________________________________________
                                ↑
                                paste_end
    // The paste_end returned would be 7 since it would be after 6 and before 7
    // at the end of step #2.

Finally, we will cut the comma `,` and paste it after `BADOLA`  (step #3).  
We may rephrase this as => cut `BADOLA` and paste it before the `,`

    ↓ paste_begin
    ____________________________________________________________________
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14   |
    ____________________________________________________________________
    | , | B | A | D | O | L | A | A | B | H |  I |  N |  A |  V | end()|
    ____________________________________________________________________
        ↑                       ↑
        cut_begin               cut_end / paste_end(step #2)

    // std::rotate(paste_begin, cut_begin, cut_end) -> paste_end
    // std::rotate(0          , 1        , 7      ) -> 6
    ____________________________________________________________________
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14   |
    ____________________________________________________________________
    | B | A | D | O | L | A | , | A | B | H |  I |  N |  A |  V | end()|
    ____________________________________________________________________
                            ↑
                            paste_end

**Notice how we used the value returned by the rotate of (step #2) in the rotate of (step #3)**

In code this would look like -
```cpp
void swap_firstname_lastname(std::string & name) // in-place swap
{
    auto const comma_position = std::find(name.begin(), name.end(), ',');         // step #1
    auto const paste_end = std::rotate(name.begin(), comma_position, name.end()); // step #2
    std::rotate(name.begin(), std::next(name.begin()), paste_end);                // step #3
}

void test()
{
    auto name = std::string{"ABHINAV,BADOLA"};
    std::cout << name << '\n';    // ABHINAV,BADOLA
    swap_firstname_lastname(name);
    std::cout << name << '\n';    // BADOLA,ABHINAV
}
```
The application of `std::rotate` is not only limited to string permutations, it may also be used with all the sequenced containers.
The discussion above applies to `std::vector`, `std::list`, `std::array`, etc. as well.

Want to move an element (or a group of elements) to the start of a vector, say `v`?
Let's start by visualizing this in terms of the trick applied in the previous example.

    _____________________________________________________
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11   |
    _____________________________________________________
    | A | B | C | D | E | F | G | H | I | J |  K | end()|
    _____________________________________________________
    ↑               ↑                       ↑
    paste_begin     cut_begin               cut_end
```cpp
auto const paste_begin = v.begin();
auto const cut_begin = std::next(v.begin(), 4);
auto const cut_end = std::next(v.begin(), 10);
auto const paste_end = std::rotate(paste_begin, cut_begin, cut_end);
```
    _____________________________________________________
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11   |
    _____________________________________________________
    | E | F | G | H | I | J | A | B | C | D |  K | end()|
    _____________________________________________________
                            ↑
                            paste_end    

`std::rotate` can also be used to move elements to the back of a vector.

    _____________________________________________________
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11   |
    _____________________________________________________
    | A | B | C | D | E | F | G | H | I | J |  K | end()|
    _____________________________________________________
        ↑                       ↑                ↑
        cut_begin               cut_end          paste_begin
        
    which needs to be reinterpreted as follows(since std::rotate is, by default, a left rotate):
    
    _____________________________________________________
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11   |
    _____________________________________________________
    | A | B | C | D | E | F | G | H | I | J |  K | end()|
    _____________________________________________________
        ↑                       ↑                ↑
        paste_begin             cut_begin        cut_end

```cpp
auto const paste_begin = std::next(v.begin());
auto const cut_begin = std::next(v.begin(), 7);
auto const cut_end = v.end();
auto const paste_end = std::rotate(paste_begin, cut_begin, cut_end);
```
    _____________________________________________________
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11   |
    _____________________________________________________
    | A | H | I | J | K | B | C | D | E | F |  G | end()|
    _____________________________________________________
                        ↑
                        paste_end    

Using rotate as our *cut-paste* algorithm has a limitation. It only works if the `paste_begin` is towards the left of `cut_begin`.  
Essentially, `std::rotate` is a *left-rotate*.
```cpp
auto const paste_end = std::rotate(paste_begin, cut_begin, cut_end);
```

We can create a high level abstration of the cut-paste algorithm using rotate which would be independent of the relative-positioning of `paste_begin` and `[cut_begin, cut_end)`. This algorithm would, however, increase the requirement on the `Iterator` from `LegacyForwardIterator` to `LegacyRandomAccessIterator`.
```cpp
template<typename It>              // It models LegacyRandomAccessIterator
auto cut_paste(It cut_begin, It cut_end, It paste_begin)
    -> std::pair<It, It>           // return the new location of the range [cut_begin, cut_end)
{
    if (paste_begin < cut_begin)   // handles left-rotate(case #1)
    {
        auto const updated_cut_begin = paste_begin;
        auto const updated_cut_end = std::rotate(paste_begin, cut_begin, cut_end);
        return { updated_cut_begin, updated_cut_end };
    }

    if (cut_end < paste_begin)     // handles right-rotate(case #2)
    {
        // Reinterpreting the right-rotate as a left rotate
        auto const updated_cut_begin = std::rotate(cut_begin, cut_end, paste_begin);
        auto const updated_cut_end = paste_begin;
        return { updated_cut_begin, updated_cut_end };
    }

    // else - no-operation required, there will be no change in the relative arrangement of data
    return { cut_begin, cut_end };(case #3)
}

Does this piece of code seem familiar?  
Exactly!  
This is the **slide** algorithm by Sean Parent, presented in his famous C++ Seasoning talk given at GoingNative 2013.  
You can read more about the slide algorithm at https://www.fluentcpp.com/2018/04/20/ways-reordering-collection-stl/

```
Let's explore the working of this algorithm visually, focussing in particular, on the return value.

    Case #1 (left rotate)
    _____________________________________________________
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11   |
    _____________________________________________________
    | A | B | C | D | E | F | G | H | I | J |  K | end()|
    _____________________________________________________
        ↑               ↑                   ↑
        paste_begin     cut_begin           cut_end

    Clearly, paste_begin < cut_begin
    Thus, the new location of the range [cut_begin, cut_end) is given by:

    auto const updated_cut_begin = paste_begin;
    auto const updated_cut_end = std::rotate(paste_begin, cut_begin, cut_end);

    _____________________________________________________
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11   |
    _____________________________________________________
    | A | F | G | H | I | J | B | C | D | E |  K | end()|
    _____________________________________________________
        ↑                   ↑
        updated_cut_begin   updated_cut_end

    Case #2 (right rotate)
    _____________________________________________________
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11   |
    _____________________________________________________
    | A | B | C | D | E | F | G | H | I | J |  K | end()|
    _____________________________________________________
        ↑               ↑                   ↑
        cut_begin       cut_end             paste_begin

    Clearly, cut_end < paste_begin
    We begin by reinterpreting this case in terms of a left rotate whereby,

    auto const l_paste_begin = cut_begin;
    auto const l_cut_begin = cut_end;
    auto const l_cut_end = paste_begin;

    _____________________________________________________
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11   |
    _____________________________________________________
    | A | B | C | D | E | F | G | H | I | J |  K | end()|
    _____________________________________________________
        ↑               ↑                   ↑
        cut_begin       cut_end             paste_begin
        l_paste_begin   l_cut_begin         l_cut_end

    In terms of a left-rotate, the paste_end(l_paste_end) is given by:
    auto const l_paste_end = std::rotate(l_paste_begin, l_cut_begin, l_cut_end);

    _____________________________________________________
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11   |
    _____________________________________________________
    | A | F | G | H | I | J | B | C | D | E |  K | end()|
    _____________________________________________________
        ↑                   ↑               ↑
        l_paste_begin       l_paste_end     paste_begin

    What we wish to return is the updated position of the range [cut_begin, cut_end)
    This is given by:

    { l_paste_end, paste_begin } or more simply by substituting for l_ variables
    auto const updated_cut_begin = std::rotate(cut_begin, cut_end, paste_begin);
    auto const updated_cut_end = paste_begin;

    Case #3
    _____________________________________________________
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11   |
    _____________________________________________________
    | A | F | G | H | I | J | B | C | D | E |  K | end()|
    _____________________________________________________
        ↑                   ↑               ↑
        cut_begin           paste_begin     cut_end
    This is a no-op as it does not change the relative arrangement of the elements
