from fuzzing.fuzzer import FuzzExecutor

seed_file = ['seed_decoder.txt',
              #'seed_encoder.txt',
]

target = ['python & rle.py -d',
           #'python & rle.py -e',
]

def run_fuzzing():
    fuzz_runner = FuzzExecutor(target, seed_file)
    fuzz_runner.run_test(20)
    return fuzz_runner.stats

if __name__ == '__main__':
    print(run_fuzzing())