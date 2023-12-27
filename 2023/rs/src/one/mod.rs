const a_exmpl: &str = "1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet";
const a_rslt: i32 = 142;

pub fn a() {
    let check = calibrate(a_exmpl);
    if check != a_rslt {
        println!("Found inappropriate calculation; expected {} to equal {}", check, a_rslt);
    }
}

fn calibrate(input: &str) -> i32 {
    return -1
}
