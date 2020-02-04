struct User {
    username: &str,
    email: &str,
    sign_in_count: u64,
    active: bool,
}

fn main() {
    let user1 = User {
        email: "someone@gmail.com",
        username: "someone",
        active: true,
        sign_in_count: 1,
    };
}
