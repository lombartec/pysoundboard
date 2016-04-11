import yaml
import os
import logging
import sys
import pygame


class Soundboard(object):
    __profiles = list()
    __sounds = dict()
    __current_profile = None

    def __init__(self, profiles_folder: str):
        self.config = config
        self.__load_profiles(profiles_folder)
        self.__load_soundboard(self.__profiles)

        if self.__current_profile == None:
            raise FileNotFoundError("The soundboard cannot work without profiles")

    def __load_profiles(self, profiles_folder: str):
        """
        Loads the profile paths into memory.
        """
        self.__profiles = [os.path.join(profiles_folder, x) for x in next(os.walk(profiles_folder))[1]]
        if len(self.__profiles) == 0:
            logging.debug("No profiles available")

    def __load_soundboard(self, profile_list: list):
        """
        Loads all the sounds inside a 2D list:

        - C:/path/profiles/1
          - Loaded sound number 1
          - Loaded sound number 2
        - C:/path/profiles/2
          - Loaded sound number 5

        The number of the sound is the key that has to be pressed to play it.
        """
        self.__sounds = dict()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
        pygame.init()
        pygame.display.set_mode((100, 100))
        pygame.mixer.init()

        for folder in profile_list:
            profile_number = int(os.path.split(folder)[1])
            directory_tree = next(os.walk(folder))
            sound_list = dict()
            for sound_file in directory_tree[2]:
                sound_key = int(sound_file.split(".")[0])
                sound_list[sound_key] = pygame.mixer.Sound(os.path.join(folder, sound_file))

            self.__sounds[profile_number] = sound_list

        # Just get the "first" element of the dict
        for key, value in self.__sounds.items():
            self.__current_profile = key
            break

    def use_profile(self, profile_number: int):
        """
        Starts using the profile number passed.
        """
        if not profile_number in self.__sounds.keys():
            logging.debug("The profile number %d is not available" % (profile_number))
            return

        self.__current_profile = profile_number

        logging.debug("Using profile number %d" % (profile_number))

    def play(self, sound_key: int, loop: bool):
        """
        Plays the given sound key located in the given profile.
        """
        profile = self.__current_profile
        if sound_key in self.__sounds[profile]:
            sound = self.__sounds[profile][sound_key]
            sound.stop()
            should_loop = -1 if loop else 0
            sound.play(loops=should_loop)
            logging.debug("Playing sound %d in profile %d with loop = %d" % (sound_key, profile, should_loop))
        else:
            logging.debug("Either the profile number %d key or the sound key %d do not exist" % (profile, sound_key))

    def stop_all_sounds(self):
        """
        Stops all sounds
        """
        pygame.mixer.stop()

    def close(self):
        """
        Close the soundboard application
        """
        logging.debug("Exiting application")
        pygame.quit()
        sys.exit(0)


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    config = list()
    config_path = os.path.join(os.path.dirname(__file__), "config.yml")

    with open(config_path, "r") as stream:
        config = yaml.safe_load(stream)

    profiles_dir = os.path.join(os.path.dirname(__file__), config['profiles_folder'])

    soundboard = Soundboard(profiles_dir)

    file_map = {
        pygame.K_KP0: 0,
        pygame.K_KP1: 1,
        pygame.K_KP2: 2,
        pygame.K_KP3: 3,
        pygame.K_KP4: 4,
        pygame.K_KP5: 5,
        pygame.K_KP6: 6,
        pygame.K_KP7: 7,
        pygame.K_KP8: 8,
        pygame.K_KP9: 9,
    }

    multiply_modifier = False
    pressed_stop = False
    key_down_time = 0
    key_up_time = 0
    current_profile = 1

    while True:
        eventList = pygame.event.get()

        for event in eventList:
            if event.type == pygame.KEYDOWN:
                key_down_time = pygame.time.get_ticks()
                if event.key == pygame.K_ESCAPE:
                    soundboard.close()
                elif event.key == pygame.K_KP_DIVIDE:
                    profile_modifier = True
                elif event.key == pygame.K_KP_MULTIPLY:
                    multiply_modifier = True
                elif event.key == pygame.K_KP_PERIOD:
                    pressed_stop = True
            elif event.type == pygame.KEYUP:
                key_up_time = pygame.time.get_ticks()
                if event.key == pygame.K_KP_PERIOD:
                    pressed_stop = False
                elif event.key == pygame.K_KP_MULTIPLY:
                    multiply_modifier = False
                elif event.key == pygame.K_KP_DIVIDE:
                    profile_modifier = False

                # if holding key 1 second or more
                if key_up_time - key_down_time >= 1000:
                    if event.key in file_map:
                        soundboard.use_profile(file_map[event.key])
                elif event.key in file_map:
                    if multiply_modifier:
                        soundboard.play(file_map[event.key], loop=True)
                    else:
                        soundboard.play(file_map[event.key], loop=False)
            elif event.type == pygame.QUIT:
                soundboard.close()

            if multiply_modifier and pressed_stop:
                soundboard.stop_all_sounds()
