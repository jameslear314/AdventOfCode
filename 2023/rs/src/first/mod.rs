const A_EXMPL: &str = "1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet";
const A_RSLT: i32 = 142;

pub fn a() {
    let check = calibrate(A_EXMPL);
    if check != A_RSLT {
        println!("Found inappropriate calculation; expected {} to equal {}", check, A_RSLT);
    }
}

fn calibrate(_input: &str) -> i32 {
    return -1
}
