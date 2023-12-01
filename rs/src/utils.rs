#[macro_export]
macro_rules! timer {
    ($x:expr) => {{
        let start = std::time::Instant::now();
        let result = $x;
        let duration = start.elapsed();
        println!("Time: {:.6}sec", duration.as_secs_f64());
    }};
}
