fn main() {
    let news = NewsArticle {
        headline: String::from("hoge_headline!"),
        location: String::from("here"),
        author: String::from("dareka"),
        content: String::from("naiyou-dayo!"),
    };

    println!("news desu! -> {}", news.summarize());
}

pub trait Summary {
    fn summarize(&self) -> String {
        String::from("(Read more...)")
    }
}

pub struct NewsArticle {
    pub headline: String,
    pub location: String,
    pub author: String,
    pub content: String,
}

//impl Summary for NewsArticle {
//    fn summarize(&self) -> String {
//        format!("{}, by {} ({})", self.headline, self.author, self.location)
//    }
//}

impl Summary for NewsArticle {}
