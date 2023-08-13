# afact
Calculates the original number from any given factorial

## Installation
Just put the executable in some folder you like and add that folder to the Environment Variables and boom: You got yourself some command line factorial reversal.

### Alternatively...
#### ...for the python file...
...you'll need ![python](python.org/downloads) put the .py file in some folder, open a powershell/cmd window in that folder and type:
```
pip install pyinstaller
pyinstaller --onefile install afact.py
```
After some time there should be a dist folder in said directory where the executable should have appeared.

#### ...for the rust file...
...you'll obviously need ![rust](https://www.rust-lang.org/tools/install) installed.
Open a terminal window in the afact-rust folder and type the following:
```
cargo build
```
The output should look something like this:
```
username@example-os:path/to/afact-rust$ cargo build
    Updating crates.io index
  Downloaded autocfg v0.1.8
  Downloaded num-iter v0.1.43
  Downloaded num v0.4.1
  Downloaded rand_core v0.4.2
  Downloaded num-traits v0.2.16
  Downloaded num-rational v0.2.4
  Downloaded rand v0.5.6
  Downloaded num-complex v0.4.3
  Downloaded num-bigint v0.4.3
  Downloaded rand_core v0.3.1
  Downloaded rand_pcg v0.1.2
  Downloaded num-integer v0.1.45
  Downloaded num-bigint v0.2.6
  Downloaded num-rational v0.4.1
  Downloaded algebraics v0.1.2
  Downloaded simple-soft-float v0.1.0
  Downloaded 16 crates (1.2 MB) in 1.96s
   Compiling autocfg v1.1.0
   Compiling rand_core v0.4.2
   Compiling libc v0.2.147
   Compiling lazy_static v1.4.0
   Compiling bitflags v1.3.2
   Compiling rand_core v0.3.1
   Compiling autocfg v0.1.8
   Compiling num-traits v0.2.16
   Compiling num-integer v0.1.45
   Compiling num-bigint v0.2.6
   Compiling num-rational v0.2.4
   Compiling rand_pcg v0.1.2
   Compiling num-bigint v0.4.3
   Compiling num-rational v0.4.1
   Compiling num-iter v0.1.43
   Compiling rand v0.5.6
   Compiling num-complex v0.4.3
   Compiling algebraics v0.1.2
   Compiling num v0.4.1
   Compiling simple-soft-float v0.1.0
   Compiling afact-rust v0.1.0 (/home/terryblejokes/Downloads/afact-main/afact-rust)
    Finished dev [unoptimized + debuginfo] target(s) in 9.31s
```
And that should do it. Pretty easy innit? also the compiled rust executable is a lot smaller than the python one.

