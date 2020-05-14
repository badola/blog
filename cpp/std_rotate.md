# std::rotate
[Home Index](/README.md)  
[C++ Home Index](/cpp/index.md)  

The way to remember `std::rorate` is :
> If you see cut-paste, it is std::rotate.

So if you see any use case, where you have to cut the data and paste it somewhere, it can be easily achieved by `std::rotate`.  

In short, we can re-interpret it as :  
`std::rotate(new_paste_location, cut_start_location, cut_end_location) -> cursor_current_location` 

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

First we will cut `,BADOLA` and paste it in front of `ABHINAV`

    // std::rotate(new_paste_location, cut_start_location, cut_end_location) -> cursor_current_location
    // std::rotate(0                 , 7                 , 14              ) -> 7
    ____________________________________________________________________
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14   |
    ____________________________________________________________________
    | , | B | A | D | O | L | A | A | B | H |  I |  N |  A |  V | end()|
    ____________________________________________________________________
    // It returns 7 since cursor would be after 6 and before 7, which is 7 in our case.

Now we will cut the comma `,` and place it after `BADOLA`.  
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
        
        auto last_cursor = std::rotate(name.begin(), name.begin() + 7, name.end());
        std::rotate(name.begin(), name.begin() + 1, last_cursor);
        
        std::cout << "name after  rotate => " << name << "\n";
        return 0;
    }

Output :

    name before rotate => ABHINAV,BADOLA
    name after  rotate => BADOLA,ABHINAV
