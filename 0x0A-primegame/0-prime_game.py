#!/usr/bin/python3
"""
    Prime Game
"""


def is_prime(num):
    """
        If the number was prime number
        return True otherwise False.
    """
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0 and i != num:
            return False
    return True


def prime_left(nums):
    """
        Check if there any prime number
        in a list of numbers.
    """
    for num in nums:
        if is_prime(num):
            return True

    return False

def isWinner(x, nums):
    """
        Return name of the player that won
        the most rounds.
    """
    FIRST_PLAYER = 'Maria'
    SECOND_PLAYER = 'Ben'
    FIRST_PLAYER_SCORE = 0
    SECOND_PLAYER_SCORE = 0

    for i in range(x):
        # for each round FIRST_PLAYER start play first.
        turn = FIRST_PLAYER
        round_list = [i for i in range(1, nums[i] + 1)]
        num = 0
        while num < len(round_list):
            if is_prime(round_list[num]):
                # FIRST_PLAYER picks prime number and its multiple
                if turn == FIRST_PLAYER:
                    turn = SECOND_PLAYER
                    # Check if the multiple of prime number exists
                    if round_list[num] ** 2 in round_list:
                        index = round_list.index(round_list[num] ** 2)
                        del round_list[index]
                    
                    del round_list[num]
                
                # SECOND_PLAYER picks prime number and its multiple
                elif turn == SECOND_PLAYER:
                    turn = FIRST_PLAYER

                    # Check if the multiple of prime number exists
                    if round_list[num] ** 2 in round_list:
                        index = round_list.index(round_list[num] ** 2)
                        del round_list[index]

                    # prime number
                    del round_list[num]
                num = 0
            else:
                num += 1

        if turn == FIRST_PLAYER:
            SECOND_PLAYER_SCORE += 1
        elif turn == SECOND_PLAYER:
            FIRST_PLAYER_SCORE += 1

    # Determine the winner of this game.
    if FIRST_PLAYER_SCORE > SECOND_PLAYER_SCORE:
        return FIRST_PLAYER
    elif SECOND_PLAYER_SCORE > FIRST_PLAYER_SCORE:
        return SECOND_PLAYER

    return None