UMich Lecture Recording URL Guesser
======

Made this and currently using this for a course where my professor does not release lecture recordings on leccap until right before the exams.

My professor "leaked" one video to leccap (the first lecture), and from the url I got for that one (which I got from inspecting element enough times), I found the parts of the recording urls which correspond to the class and to the room in which the lecture was recorded in. Take a look in the `research/` folder if you want to see my "research."

The rest of the url is just a timestamp (corresponding to the start time of the lecture, but may be off by ~10 seconds) and a random 3-digit code, so my script just generates all possible URLs and sends HEAD requests until it hits something.

Feel free to send a pull request to edit the script to make it more generalizable. Right now a lot of things are hard-coded in guesser.py. 

To run the script, download this repo, create a python virtual environment, and change the constants in guesser.py (for now), run the script, and wait :)


