use std::fs::File;
use std::io::Read;
use std::io::Error;
use std::time::Instant;
use std::collections::HashMap;

lazy_static! {static ref NUMBER_MAP: HashMap<&'static str, char> = {
    let mut map = HashMap::new();
    // map.insert("zero", '0'); // Zero is not a valid number in this problem
    map.insert("one", '1');
    map.insert("two", '2');
    map.insert("three", '3');
    map.insert("four", '4');
    map.insert("five", '5');
    map.insert("six", '6');
    map.insert("seven", '7');
    map.insert("eight", '8');
    map.insert("nine", '9');
    map
};}
const DIR: &str = "/source/self/AdventOfCode/2023/rs/src/first/";
const EXMPL_SFX: &str = ".example.txt";
const INPUT_SFX: &str = ".txt";
const A_RSLT: i32 = 142;
const B_RSLT: i32 = 281;

pub fn a() {
    print!("Checking validity of example a1's calibration... ");
    let prefix = &(DIR.to_owned() + "a");

    let start = Instant::now();
    let example = read_file(&(prefix.to_owned() + EXMPL_SFX));
    let mut cont = true;
    let mut val: i32 = -1;
    match example {
        Ok(amendment) => {val = demend(amendment); if val != A_RSLT {cont = false; }},
        Err(e) => {eprintln!("Error reading file at {}: {}", &(prefix.to_owned() + EXMPL_SFX), e); cont = false},
    };
    if !cont {
        println!("invalid in {:?};\n\texpected {} but calculated {}", start.elapsed(), A_RSLT, val);
        return;
    }
    println!("valid in {:?}\nCalibrating input...", start.elapsed());
    
    let input = read_file(&(prefix.to_owned() + INPUT_SFX));
    match input {
        Ok(amendment) => println!("Found:\n\t{}\n\t\tafter {:?}\n", demend(amendment), start.elapsed()),
        Err(e) => eprintln!("Error reading file at {}: {}", &(prefix.to_owned() + INPUT_SFX), e),
    }
}

fn read_file(path: &str) -> Result<String, Error> {
    let mut file = File::open(path)?;
    let mut contents = String::new();

    file.read_to_string(&mut contents)?;
    Ok(contents)
}

fn demend(amendment: String) -> i32 {
    amendment.lines()
        .map(|line| {
            let digits: Vec<char> = line.chars().filter(|c| c.is_digit(10)).collect();
            match digits.len() {
                0 => 0,
                _ => {
                    let tens = digits.first().unwrap().to_digit(10).unwrap();
                    let ones = digits.last().unwrap().to_digit(10).unwrap();
                    (tens * 10 + ones) as i32
                }
            
            }
        }).sum::<i32>()
}

pub fn b() {
    print!("Checking validity of example a1's calibration... ");
    let prefix = &(DIR.to_owned() + "b");

    let start = Instant::now();
    let example = read_file(&(prefix.to_owned() + EXMPL_SFX));
    let mut cont = true;
    let mut val: i32 = -1;
    let mut contents: String = "".to_string();
    match example {
        Ok(amendment) => {contents = amendment.clone(); val = demend(digitify(&amendment)); if val != B_RSLT {cont = false; }},
        Err(e) => {eprintln!("Error reading file at {}: {}", &(prefix.to_owned() + EXMPL_SFX), e); cont = false},
    };
    if !cont {
        println!("invalid in {:?};\n\texpected {} but calculated {}", start.elapsed(), B_RSLT, val);
        println!("Had\n{}\nbut expected\n{}", contents, digitify(&contents));
        return;
    }
    println!("valid in {:?}\nCalibrating input...", start.elapsed());
    
    let input = read_file(&(prefix.to_owned() + INPUT_SFX));
    match input {
        Ok(amendment) => println!("Found:\n\t{}\n\t\tafter {:?}\n", demend(digitify(&amendment)), start.elapsed()),
        Err(e) => eprintln!("Error reading file at {}: {}", &(prefix.to_owned() + INPUT_SFX), e),
    }
}

fn digitify(superstring: &str) -> String {
    let mut result = superstring.to_ascii_lowercase();
    for (word, digit) in NUMBER_MAP.iter() {
        loop {
            let option = result.find(word);

            if Option::is_some(&option) {
                let word_index = Option::unwrap(option);
                // Break word instances by inserting their value as the second digit
                result.insert(word_index + 1, *digit)
            } else {
                break;
            }
        };
    }
    result
}
