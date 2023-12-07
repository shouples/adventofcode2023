#[macro_export]
macro_rules! timer {
    ($func_name:expr, $func_call:expr) => {{
        let start = std::time::Instant::now();
        let result = $func_call;
        let duration = start.elapsed();
        println!(
            "`{}` time: {:?} ({:.8} sec)",
            $func_name,
            duration,
            duration.as_secs_f64()
        );
        result
    }};
}
