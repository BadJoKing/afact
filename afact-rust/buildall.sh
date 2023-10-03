sudo apt install -y gcc-multilib mingw*
cargo build --target x86_64-pc-windows-gnu
cargo build --target x86_64-unknown-linux-gnu
cargo build --target i686-unknown-linux-gnu
cargo build --target i686-pc-windows-gnu
read a
