fn main() {
    let x = 5;
    println!("The variable is {}", x);
    let x = x + 6;
    println!("The variable is {}", x);

    // let guess: u32 = "42".parse().expect("Not a number!");
    let guess = "42".parse().expect("Not a number!");
}
