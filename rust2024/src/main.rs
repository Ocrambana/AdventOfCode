use day1::day1;
use day2::day2;

mod day1;
mod day2;
mod utils;

fn main() 
{
    println!("Hello, world!");
    day1(); 
    println!("========== day 1 end   ==========");
    println!("========== day 2 start ==========");
    day2();
    println!("========== day 2 end   ==========");
}
