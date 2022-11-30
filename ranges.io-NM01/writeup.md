### My code is inefficient garbage and my method isn't so refined either, but here's what I did.

Method/Spoiler free solution:

- Figured out how to export netcat output into a text file
- Based on what the output was, I modified a shell script accordingly
- Shell script does the math and outputs result
- Figured out how to pipe bash script results into netcat






Spoiler solution:

If you're really struggling, here's step by step what I did:

- Do the netcat connection:

> netcat nc ggcs-nm01.allyourbases.co 6167

Results in:

> 1337 * 42 =

- Write a bash script to solve the problem:

` #!/bin/bash `

`var=$((1337 * 42)) `

`echo $var `

- Do the netcat connection, but this time run the bash script at the same time, and have it output the results (questions) into a text file

> ./bash.sh | nc ggcs-nm01.allyourbases.co 6167 > qs.txt

- Modify shell script to solve the next question

`sleep 0.5`

`var=$((42 * 42))`

`echo $var`

The sleep just waits for the next question to come  up. 

- Save the program and run the command again:

> ./bash.sh | nc ggcs-nm01.allyourbases.co 6167 > qs.txt

That should get your flag.

- Check qs.txt (or your netcat result text file) and the flag should be there, under the math problems.