use std::{io::BufRead};

use crate::utils::create_buffer_reader;

static MIN_DIFFERENCE : i16 = 1;
static MAX_DIFFERENCE : i16 = 3;

pub fn day2()
{
    let reader = create_buffer_reader(String::from("./data/day2Data.txt"));
    let mut report : Vec<i16>;
    let mut safe_reports : i16 = 0;
    for line_wrapped in reader.lines()
    {
        let line = line_wrapped.unwrap();
        println!("{}", line);
        report = parse_string(&line);
        if is_safe_report(&report)
        {
            safe_reports = safe_reports + 1;
            println!("{line} is SAFE");
        }
        else {
            println!("{line} is SAFE");
        }
    }
    println!("Number of safe reports {}", safe_reports);
}

fn parse_string(str : &str) -> Vec<i16>
{
    let mut vec = Vec::new();
    for iter in str.split(' ')
    {
        vec.push(iter.parse::<i16>().expect("Unable to parse {iter}"));
    }
   return vec;
}

fn is_safe_report(report : &Vec<i16>) -> bool
{
    let mut is_safe = true;
    let mut mode = ReportType::Increasing;
    let mut problem_dapner = true;
    if report[0] > report[1]
    {
        mode = ReportType::Decreasing;
    }
    
    let mut last_report:i16;
    match mode
    {
        ReportType::Decreasing => last_report = report[0] + MIN_DIFFERENCE,
        ReportType::Increasing => last_report = report[0] - MIN_DIFFERENCE,
    };

    for rep in report
    {
        let mut difference : i16  = 0;
        match mode
        {
            ReportType::Decreasing => difference = last_report - rep,
            ReportType::Increasing => difference = rep - last_report,
        };

        let report_res = difference >= MIN_DIFFERENCE && difference <= MAX_DIFFERENCE;
        is_safe = is_safe && ( problem_dapner || report_res);
        last_report = *rep;
        if problem_dapner
        {
            problem_dapner = report_res;
        } 
    }
    
    return is_safe;
}

enum ReportType
{
    Increasing,
    Decreasing
}