fn main() {
    println!("Hello, world!");
}

pub trait Summary {
    fn summarize(&self) -> String;
}
