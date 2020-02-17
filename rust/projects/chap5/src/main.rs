#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
}

struct Color(i32, i32, i32);
struct Point(i32, i32, i32);

fn main() {
    let rectangle = Rectangle {
        width: 30,
        height: 50,
    };

    println!(
        "The area of the rectangle is {} square pixels.",
        rectangle.area()
    );

    println!("rect is {:?}", rectangle);

    let black = Color(0, 0, 0);
    let mut origin = Point(0, 0, 0);
    // origin = black;
}
