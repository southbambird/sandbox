fn main() {
    let mut count = 0;
    loop {
        println!("again! {}", count);
        count = count + 1;
        if count == 10000 {
            break;
        }
    }
    println!("finish!");
}
