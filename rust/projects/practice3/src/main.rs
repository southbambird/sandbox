fn main() {
    print_lyrics();
}

fn to_celsius(f: f32) -> f32 {
    (5.0 / 9.0) * (f - 32.0)
}

fn to_fahrenheit(c: f32) -> f32 {
    (c * 1.8) + 32.0
}

fn print_lyrics() {
    let lyrics = [
        "A partridge in a pear tree",
        "Two turtle doves",
        "Three French hens",
        "Four calling birds",
        "Five golden rings",
        "Six geese a-laying",
        "Seven swans a-swimming",
        "Eight maids a-milking",
        "Nine ladies dancing",
        "Ten lords a-leaping",
        "Eleven pipers piping",
        "Twelve drummers drumming",
    ];

    let number = [
        "first", "second", "third", "forth", "fifth", "sixth", "seventh", "eighth", "nineth",
        "tenth", "eleventh", "twelveth",
    ];

    for (index, num) in number.iter().enumerate() {
        println!("----------- {} lyric -----------", num);
        println!("On the {} day of Christmas,", num);
        println!("my true love sent to me");
        for i in (0..=index).rev() {
            println!("{}", lyrics[i]);
        }
    }
}
