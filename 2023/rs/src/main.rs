mod first;
mod second;

mod util;

#[macro_use]
extern crate lazy_static;

fn main() {
    println!("Hello, advent!");
    day1();
}

fn day1() {
    println!("~~~ day the first ~~~");
    first::a();
    first::b();
}
