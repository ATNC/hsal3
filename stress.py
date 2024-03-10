import subprocess


def stress_test(url, num_requests, concurrency):
    command = f"ab -n {num_requests} -c {concurrency} {url}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    stdout = process.communicate()[0]

    print('STDOUT:{}'.format(stdout))


stress_test("http://localhost/time", 10000, 100)
