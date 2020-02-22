fn main() {
    let news = NewsArticle {
        headline: String::from("hoge_headline!"),
        location: String::from("here"),
        author: String::from("dareka"),
        content: String::from("naiyou-dayo!"),
    };

    println!("news desu! -> {}", news.summarize());

    notify(news);

    let tweet = Tweet {
        username: String::from("horse_ebooks"),
        content: String::from("of course, as you probably already know, people"),
        reply: false,
        retweet: false,
    };

    //println!("1 new tweet: {}", tweet.summarize());

    notify(tweet);
}

pub trait Summary {
    fn summarize(&self) -> String;
}

pub struct NewsArticle {
    pub headline: String,
    pub location: String,
    pub author: String,
    pub content: String,
}

impl Summary for NewsArticle {
    fn summarize(&self) -> String {
        format!("{}, by {} ({})", self.headline, self.author, self.location)
    }
}

pub struct Tweet {
    pub username: String,
    pub content: String,
    pub reply: bool,
    pub retweet: bool,
}

//impl Summary for Tweet {
//    fn summarize(&self) -> String {
//        format!("{}: {}", self.username, self.content)
//    }
//}

pub fn notify<T: Summary>(item: T) {
    println!("Breaking new!! {}", item.summarize());
}
