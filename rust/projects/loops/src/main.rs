fn main() {
    let mut count = 0;
    loop {
        println!("again! {}", count);
        count = count + 1;
        if count == 10000 {
            break;
        }
    }
    println!("finish loop!");

    let mut count = 3;
    while count != 0 {
        println!("{}!", count);

        count = count - 1;
    }

    println!("LIFTOFF!!!!!!!");

    let a = [10, 20, 30, 40, 50];
    let mut index = 0;

    while index < 5 {
        println!("the value is: {}", a[index]);
        index = index + 1;
    }

    for element in a.iter() {
        println!("the value is: {}", element);
    }

    for number in (1..4) {
        println!("the value is: {}", number);
    }
    println!("done!!!!!");
}
