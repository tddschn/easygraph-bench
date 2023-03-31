import timeit
import statistics

# try:
#     from utils_db import insert_bench_results
# except ImportError:
#     print(f'Could not import insert_bench_results from utils_db.py')


def benchmark(stmt, n, globals):
    print('Function:', stmt)
    times = timeit.repeat(stmt, number=1, globals=globals, repeat=n)
    print('  --------------')
    print(f'  Min:      {min(times)}')
    print(f'  Median:   {statistics.median(times)}')
    print(f'  Mean:     {statistics.mean(times)}')
    print(f'  Stdev:    {statistics.stdev(times) if len(times) > 1 else "N.A."}')
    print(f'  Max:      {max(times)}')
    print('  --------------')
    print(f'  samples:  {len(times)}')
    print()


def benchmark_autorange(stmt: str, globals: dict, n: int | None = None) -> float:
    timer = timeit.Timer(stmt, globals=globals)
    print('Function:', stmt)
    if n is None:
        count, total_time = timer.autorange()
    else:
        count = n
        total_time = timer.timeit(number=n)
    print('  --------------')
    print(f'  Total time: {total_time}')
    print(f'  Count:      {count}')
    print(f'  Mean:       {(avg_time := total_time / count)}')
    return avg_time
