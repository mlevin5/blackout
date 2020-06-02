this script uses [instapy](https://github.com/timgrossmann/InstaPy) to automate commenting on people's blackout photos, asking them to please stop clogging the blacklivesmatter hashtag so useful info for the movement can be more easily spread!

i created this because i was told by people involved in the movement that this would be a useful tool. 

#how to use

1. install python

2. install instapy
`pip install instapy` or `pip3 install instapy` for python3

3. clone the repo

4. navigate to the repo folder in the command line, and run the script with `python quickstart.py` or `python3 quickstart.py` for python3

#comment customization

go into your local comments.txt file and edit the possible comments that can be made, if you want to change wording or whatever. just make sure there's space between each comment so it is parsed correctly.

#help

if you want to add to this, please feel free to fork or make a pull request or whatever. 

ideally, people wouldn't have to worry about installing the dependencies themselves or messing with the commandline.

also, right now the blackout images are being identified using a very rudimentary AI algorithm i trained using Clarifai, just because instapy already has easy integration with that third party tool. But, it doesn't work perfectly. I'd much rather not use AI at all, and just check that every pixel in the photo is black, or something more straightforward like that, but I haven't figured out how to integrate that with instapy.




