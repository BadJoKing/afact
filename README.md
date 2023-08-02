# afact
Calculates the original number from any given factorial

## Installation
Just put the executable in some folder you like and add that folder to the Environment Variables and boom: You got yourself some command line factorial reversal.

### Alternatively...
#### ...for the python file...
...put the .py file in some folder, open a powershell/cmd window in that folder and type:
```
pip install pyinstaller
pyinstaller --onefile install afact.py
```
After some time there should be a dist folder in said directory where the executable should have appeared.

#### ...for the rust file...
You obviously need ![rust](https://www.rust-lang.org/tools/install) installed.
Open a terminal window in the afact-rust folder and type the following:
```
cargo build
```
And that should do it. Pretty easy innit? also the compiled rust executable is a lot smaller than the python one.

### Requirements
Yeah, if you're running the released executable, you pretty much only need Windows.
For the manual build instead you gotta have python or rust installed.
