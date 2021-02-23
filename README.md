# private

_Private_ allows you to make your module functions or class methods private. The private methods, when called would raise NameError exception.

## Installation
You need to clone the repo.
```
> git clone git@github.com:justcli/private.git
```
Then run the install script from the repot directory.

```
> cd private
> bash install.sh
Files copied to /usr/local/lib/python3.9/site-packages/private/:
  __init__.py
Installation done!.
```

## Usage

You need to import it in your module file.
```
# mymodule.py
from private import *
```
Then you call the apply_on function before writing your code as shown below
```
# mymodule.py
from private import *

apply_on(__file__)

@private
def a_local_function():
  pass

class foo:
  @private
  def local_method():
    pass

  def can_be_exported():
    pass
```
Every function or class method with _@private_ decorator become uncallable for any external code.

It also works with Python shell, Python debugger and iPython.

