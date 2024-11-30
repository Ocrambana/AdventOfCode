use std::io::BufReader;
use std::fs::{self, File};

pub fn read_file(path: String) -> String
{
    let contents = fs::read_to_string(path)
        .expect("Should have been able to read the file");

    return contents;
}

pub fn create_buffer_reader(path:String) -> BufReader<File>
{
    let f = File::open(path)
        .expect("Should have been to read file in {path}");
    let reader = BufReader::new(f);

    return reader;
}