from subprocess import Popen, PIPE, STDOUT

expression = "4*3"

jar_return_values = Popen(
    ['java', '-jar', 'JavaCalculator.jar', expression],
    stdout=PIPE,
    stderr=STDOUT
)

for line in jar_return_values.stdout:
    print(line.decode('utf-8'))