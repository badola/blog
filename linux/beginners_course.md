[Linux Home Index](/linux/index.md)

## The Linux Beginner's Course 

The purpose of these lectures is to instill in the candidate practical knowledge and a better understanding of the tools/commands that a linux user would encounter on daily basis. 
Special focus should be provided on strengthening of concepts, so that the candidates are in a better position to debug their problems.


**The following topics should be covered within this course, and in the order mentioned -**  
1. What is linux and how is it useful for industries.  
1. The directory structure of a standard linux distro, and a brief description of the role of each directory  
1. Relative and absolute paths  
1. Linux command structure  
    1. command-name [options] <source> <target>  
1. An overview of the various linux commands (list attached in the Appendix 1)  
1. ls -l     # long listing of ls command, the most useful command
    1. types of files, and its identification
    1. Everything is a file in linux
    1. hard-link count of file
    1. user
    1. group
    1. file size
    1. Modification timestamp
    1. Last access timestamp
    1. finding most recently modified file in a directory
1. Permissions - 
    1. What is user/owner, group, others, all
    1. read - 4 / write - 2 / execute - 1 / none - 0
    1. Primary Group / Secondary Group
    1. permissions are only given via groups, a resource(file) can only be associated with one group
    1. A user is a part of multiple groups
    1. chmod
        1. chmod a+rx   # textual representation
        1. chmod 655    # numerical representation
    1. chown
    1. chgrp
    1. id
    1. groups (command)
    1. Difference between Authentication and Authorization
    1. umask 
    1. sticky bit
1. Redirection and Piping
    1. what is stdin, stdout, stderr
    1. how to redirect one buffer to another
    1. what is /dev/null
    1. redirecting output of one command into another using pipe
    1. chaining of commands using pipes
1. Environment
    1. What is an environment variable
    1. use some common env variables (PATH, LD_LIBRARY_PATH, PWD, USER, SHELL, etc)
    1. What is an environment? Why do we use them?
    1. How to switch between environments
1. Aliasing
    1. How is it useful
    1. How to detect if a command is an alias
    1. Using underlying command, instead of alias
    1. Storing alias
1. Links -
    1. Hard Links 
    1. Soft Links and their uses
    1. When does an operating system delete a file (when its hard-link count turns to 0)
1. User personalization configuration files
    1. .cshrc
    1. .bashrc
1. Vim
    1. Modes - command and edit
    1. commands : copy, cut, paste, visual selection, search and replace, etc
    1. .vimrc
1. Chaining of Commands -
    1. Generators - 
        1. selection commands - find, ls, grep, cat, etc.
        1. projection commands - cut, awk, etc.
        1. transformation commands - sort, tr, rev, xargs, etc.
    1. Actions - mv, cp, rm, mkdir, kill, etc.
    1. Generators can be chained infinitely with pipe, actions cannot
    1. Actions can only be used at the end of chain.
    1. Suppose there is a file employee.txt with data in format=> name,address,phone_number
        1. get all distinct tuples of (name,phone_number)
        1. get all the names sorted alphabetically
        1. get the number of duplicate entries
        1. Show details of duplicate entries
    1. In a given directory, get all the files that begin with letter ‘D’ and have been created by user ‘Y’


### Schedule
1. The topics will be divided into 4 lectures of 1.5 hours each
    1. Lecture 1  
	  Topics 1 - 4 from the list provided above
    1. Lecture 2  
    Topics 5 - 7 from the list provided above
    1. Lecture 3  
    Topics 8 -12 from the list provided above
    1. Lecture 4  
    Topics 13 and 14 from the list provided above















### Appendix 1
**List of commands, basic usage should be studied by the candidate -**
1. ls
1. wc
1. ssh 
1. cd
1. pwd
1. grep (Usage with regular expression) 
1. find
1. ack (similar to grep but better)
1. cat
1. echo
1. date
1. chmod
1. chown
1. chgrp
1. cp
1. mv
1. ln
1. rm
1. mkdir
1. rmdir
1. touch
1. head
1. tail
1. more
1. less
1. id
1. du
1. df
1. ps
1. man
1. info
1. whatis
1. whereis
1. locate
1. apropos
1. whoami
1. hostname


### Appendix 2
**Supplemental Reading Materials**

1. The Linux Documentation Project (Chapters => 1, 2, 3, 4, 7, 8, 9)  
http://www.tldp.org/LDP/Bash-Beginners-Guide/html/

1. Shells: how are they different from kernel and OS, their use  
http://ecomputernotes.com/fundamental/disk-operating-system/what-is-shell-and-kernel

1. Directory Structure  
http://www.tecmint.com/linux-directory-structure-and-important-files-paths-explained/

1. Relative and absolute path

1. Simple commands (what are arguments and options, a basic non-exhaustive list in Appendix 1)  

1. commands for getting help (man, info, whatis, whereis, apropos, locate, etc)

1. Redirection and piping  
(what is stdin, stdout, stderr and how to redirect one buffer to another, what is /dev/null)  
http://wiki.bash-hackers.org/howto/redirection_tutorial  

1. vim : modes, commands (copy, cut, paste, visual selection, search and replace, etc)  
http://www.radford.edu/~mhtay/CPSC120/VIM_Editor_Commands.htm

1. Aliasing  
http://www.cyberciti.biz/tips/bash-aliases-mac-centos-linux-unix.html

1. Env Variables: use some common env variables (PATH, LD_LIBRARY_PATH, PWD, USER, SHELL, etc)  
https://help.ubuntu.com/community/EnvironmentVariables

1. root and non-root user : similarities and difference  
http://www.linfo.org/root.html


1. User personalization configuration files: .cshrc/.bashrc  
http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_01.html

1. File permissions

1. Basic commands (including their various usage)  
http://searchenterpriselinux.techtarget.com/tutorial/77-useful-Linux-commands-and-utilities

1. ssh  
http://support.suso.com/supki/SSH_Tutorial_for_Linux

1. grep (Usage with regular expression)  
http://www.linfo.org/grep.html

1. find  
https://www.digitalocean.com/community/tutorials/how-to-use-find-and-locate-to-search-for-files-on-a-linux-vps

1. ack (similar to grep but better)  
https://beyondgrep.com/

1. echo  
http://www.linfo.org/echo.html

1. ps  
https://access.redhat.com/sites/default/files/attachments/processstates_20120831.pdf
