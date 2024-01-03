mod first;
mod second;

mod util;

use std::{env, collections::HashMap};

#[macro_use]
extern crate lazy_static;



fn main() {
    let args: Vec<String> = env::args().collect();
    let def_usage: bool;
    if args.len() <= 1 {
        def_usage = true;
    } else {
        def_usage = false;
    }
    let mut map = HashMap::new();
    let days: [i32;2] = [1,2];
    days.iter().for_each(|i| {map.insert(*i, def_usage);});

    println!("~-*-~-*-~-*-~ Hello, advent! ~-*-~-*-~-*-~\n");

    if args.len() > 1 {
        args.iter().skip(1).for_each(|arg| {
            let key_r = arg.parse::<i32>();
            match key_r
            {
                Ok(key) => {*map.entry(key).or_insert(!def_usage) = !def_usage;},
                Err(e) => eprintln!("Failed to process arg {} as int32: {}\n", arg, e)
            }
        })
    }

    // I'd like to dynamically call functions based on which argument was referenced... but instead I'll do an explicit check.
    if map.get(&1).is_some() {
        call(1, &day1, &map);
    }
    if map.get(&2).is_some() {
        call(2, &day2, &map);
    }
}

fn call(i: i32, f: &dyn Fn()->(), map: &HashMap<i32, bool>) {
    let v = map.get(&i);
    if Option::is_some(&v) && *v.unwrap() == true {
        f()
    }
}

fn day1() {
    println!("~~~ day the first ~~~");
    first::a();
    first::b();
}

fn day2() {
    println!("~~~ day the second ~~~");
}
