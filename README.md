#pysoundboard :sound: :notes:
A little soundboard system that lets you use it as a meme machine gun or use it as helper to get a quick mix.

##Features
- Playing sounds (don't you say!).
- Loop sounds.
- Stop everything that is playing.
- Profiles.

##Set up
- I'm running this project from a windows machine with **python 3.4.4**, what I did to get it running was:
  - `pip install wheel`
  - [Download](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame) a pre released binary of pygame (you can see more info in [pygame download page](http://www.pygame.org/download.shtml))
    - In my case I downloaded the `pygame-1.9.2a0-cp34-none-win_amd64.whl` file
  - `pip install pygame-1.9.2a0-cp34-none-win_amd64.whl`
  - Put your profiles in place
    - Create a folder with name `0` then paste `.ogg` files inside with the number you want them bind to as the name of the file. E.G: `profiles/0/1.ogg`
  - Run `python Soundboard.py`

##Key bindings
####Everything is controlled from the numpad!
- To play a sound press the number assigned to it.
- To loop a sound hold multiply key (*) and press the number assigned to it.
  - To stop looping the sound just play it again pressing they key assigned to it.
- To switch to another profile hold the divide key (/) and press the number assigned to the profile.
- To stop all sounds that are playing hold the multiply key (*) and press the period key (.)

##Why this?
In the last company christmas dinner I got a cool gift from my boss, a meme soundboard,
it is very fun, but the amount of sounds you can use is limited to 8 sounds. My aim here
is to put together this software with some hardware like a **RaspberryPi** + **USB Numpad** + **USB Speaker**
and maybe a little **LCD Screen**.

In any case I also take this as a little training in Python and pygame which I was already interested in.

##Things I would like to achieve with this project
- [ ] Learn enough to be able to distribute a Python application
- [ ] Learn how to unit test Python applications
- [ ] Put together the hardware

##Collaborating
Any kind of collaboration, code, pointing me in the right direction, suggestions, is much appreciated.
