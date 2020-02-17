struct Rectangle {
    width: u32,
    height: u32,
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
        area(&rectangle)
    );

    let black = Color(0, 0, 0);
    let mut origin = Point(0, 0, 0);
    origin = black;
}

fn area(rectangle: &Rectangle) -> u32 {
    rectangle.width * rectangle.height
}
