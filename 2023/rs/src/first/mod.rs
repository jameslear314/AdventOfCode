use std::fs::File;
use std::io::Read;
use std::io::Error;
use std::time::Instant;

const A_DIR: &str = "/source/self/AdventOfCode/2023/rs/src/first/";
const A_EXMPL_PTH: &str = "a.example.txt";
const A_PTH: &str = "a.txt";
const A_RSLT: i32 = 142;

pub fn a() {
    print!("Checking validity of example a1... ");
    let start = Instant::now();
    match calibrate(&(A_DIR.to_owned() + A_EXMPL_PTH)){
        Ok(check) => if check != A_RSLT {
            println!("Found inappropriate calculation; expected {} to equal {}", check, A_RSLT);
        },
        Err(e) => eprintln!("Error reading file at {}: {}", A_EXMPL_PTH, e),
    }
    print!("valid in {:?}\nCalibrating input... ", start.elapsed());
    match calibrate(&(A_DIR.to_owned() + A_PTH)){
        Ok(val) => println!(":\n\t{}\n\t\tafter {:?}\n", val, start.elapsed()),
        Err(e) => eprintln!("Error reading file at {}: {}", A_EXMPL_PTH, e),
    }
}

fn calibrate(input: &str) -> Result<i32, Error> {
    let amendment = read_file(input)?;
    return Ok(demend(amendment))
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
