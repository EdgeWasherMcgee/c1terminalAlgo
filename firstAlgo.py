import gamelib
import math
import random

class algo(gamelib.AlgoCore):

    def __init__(self):
        super().__init__()
        random.seed()

    def on_game_start(self, config):
        self.config = config
        gamelib.debug_write('Configuring your custom algo strategy...')
        global FILTER, ENCRYPTOR, DESTRUCTOR, PING, EMP, SCRAMBLER
        FILTER = config["unitInformation"][0]["shorthand"]
        ENCRYPTOR = config["unitInformation"][1]["shorthand"]
        DESTRUCTOR = config["unitInformation"][2]["shorthand"]
        PING = config["unitInformation"][3]["shorthand"]
        EMP = config["unitInformation"][4]["shorthand"]
        SCRAMBLER = config["unitInformation"][5]["shorthand"]

    def on_turn(self, turn_state):
        game_state = gamelib.GameState(self.config, turn_state)
        gamelib.debug_write('Performing turn %d of your custom algo strategy' % game_state.turn_number)
        self.starterstrategy(game_state)

        game_state.submit_turn()

    def starter_strategy(self, game_state):
        self.build_setup(game_state)
        game_state.submit_turn()


    def build_setup(self, game_state):
        priority_firewall_locations = [[14,1],[13,2],[13,3],[26,12],[25,12],[23,12],[22,12],[21,12],[20,12],
                [18,12],[17,12],[16,12],[15,12],[13,12],[12,12],[11,12],[10,12],[4,12],[2,12],[1,12]]
        destructor_locations = [[3,12],[90,12],[14,12],[19,12],[24,12]]
        firewall_locations = [[10,3],[11,4],[12,5],[13,6],[14,7],[15,8],[16,9],[17,10],[18,10],[19,10],[20,10],[21,10]]
        emp_locations = [[12,1],[12,1]]
        scrambler_locations = [11,2]
        game_state.attempt_spawn(FILTER, priority_firewall_locations)
        game_state.attempt_spawn(DESTRUCTOR, destructor_locations)
        game_state.attempt_spawn(FILTER, firewall_locations)
        game_state.attempt_spawn(SCRAMBLER, scrambler_locations)
        game_state.attempt_spawn(EMP, emp_locations)
