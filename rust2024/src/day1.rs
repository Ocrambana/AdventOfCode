use std::io::BufRead;

use crate::utils;

pub fn day1()
{
    let reader = utils::create_buffer_reader(String::from("./data/testData.txt"));

    for wrapped_line in reader.lines()
    {
        let line = wrapped_line.unwrap();
        print!("{line}\n");
    }

}