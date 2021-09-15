# nonlocal - Python 3.0+

To rebind variables found outside of the innermost scope, the nonlocal statement can be used;
if not declared nonlocal, those variables are read-only (an attempt to write to such a variable 
will simply create a new local variable in the innermost scope, leaving the identically named 
outer variable unchanged).

More information about nonlocal:
 - https://www.python.org/dev/peps/pep-3104/
 - https://docs.python.org/3.5/reference/simple_stmts.html#nonlocal
 - https://docs.python.org/3/tutorial/classes.html#scopes-and-namespaces-example
 - https://stackoverflow.com/questions/1261875/python-nonlocal-statement
