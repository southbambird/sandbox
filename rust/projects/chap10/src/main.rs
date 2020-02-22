fn main() {
    let number_list = vec![10, 20, 30, 40, 50];

    let mut largest = number_list[0];

    for number in number_list {
        if number > largest {
            largest = number;
        }
    }

    println!("The largest number is {}", largest);
    assert_eq!(largest, 50);
}
