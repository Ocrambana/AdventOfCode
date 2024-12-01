use std::{collections::BinaryHeap, io::BufRead};

use crate::utils::create_buffer_reader;

pub fn day1()
{
    let reader = create_buffer_reader(String::from("./data/day1Data.txt"));

    
    // due binary heap da riempire
    let mut left_buffer: BinaryHeap<i32> = BinaryHeap::new();
    let mut right_buffer: BinaryHeap<i32> = BinaryHeap::new();
    for wrapped_line in reader.lines()
    {
        let line = wrapped_line.unwrap();
        let split : Vec<&str> = line.split_whitespace().collect();

        left_buffer.push(split[0].parse::<i32>().unwrap());
        right_buffer.push(split[1].parse::<i32>().unwrap());
    }

    let left = left_buffer.into_sorted_vec();
    let right = right_buffer.into_sorted_vec();
    let mut distance : i32 = 0;

    for (li,ri) in left.iter().zip(right.iter())
    {
        distance += (li-ri).abs();
    }

    println!("Total distance {distance}");

    let mut similarity = 0;
    for li in left
    {
        similarity += li * count_occurrency(&li, &right);
    }

    println!("Total Similarity {similarity}");
}

fn count_occurrency(val : &i32, list : &Vec<i32>) -> i32
{
    let mut result = 0;

    for item in list
    {
        if item == val
        {
            result += 1;
        }
    }

    return result;
}