import pygame


class EventHandler(object):
    __soundboard = None
    __file_map = dict()

    __multiply_modifier = False
    __profile_modifier = False
    __pressed_stop = False

    def __init__(self, soundboard, file_map: dict):
        self.__soundboard = soundboard
        self.__file_map = file_map

    def handle(self, event_list: list):
        """
        Handles the event contained in the passed event list
        """
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                self.__handle_key_down_event(event)
            elif event.type == pygame.KEYUP:
                self.__handle_key_up_event(event)
            elif event.type == pygame.QUIT:
                self.__soundboard.close()

    def __handle_key_down_event(self, event):
        """
        Handles the events of type keydown
        """
        if event.key == pygame.K_ESCAPE:
            self.__soundboard.close()
        elif event.key == pygame.K_KP_DIVIDE:
            self.__profile_modifier = True
        elif event.key == pygame.K_KP_MULTIPLY:
            self.__multiply_modifier = True
        elif event.key == pygame.K_KP_PERIOD:
            self.__pressed_stop = True

        if event.key in self.__file_map and not self.__profile_modifier:
            if self.__multiply_modifier:
                self.__soundboard.play(self.__file_map[event.key], loop=True)
            else:
                self.__soundboard.play(self.__file_map[event.key], loop=False)

        if self.__multiply_modifier and self.__pressed_stop:
            self.__soundboard.stop_all_sounds()

    def __handle_key_up_event(self, event):
        """
        Handles the events of type keyup
        """
        if self.__profile_modifier and event.key in self.__file_map:
            self.__soundboard.use_profile(self.__file_map[event.key])

        if event.key == pygame.K_KP_PERIOD:
            self.__pressed_stop = False
        elif event.key == pygame.K_KP_MULTIPLY:
            self.__multiply_modifier = False
        elif event.key == pygame.K_KP_DIVIDE:
            self.__profile_modifier = False
