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

    for i in range(2, int(num / 2)):
        if num % i == 0 and i != num:
            return False
    return True


def isWinner(x, nums):
    """
        Return name of the player that won
        the most rounds.
    """
    if x < 1 or not nums:
        return None

    FIRST_PLAYER = 'Maria'
    SECOND_PLAYER = 'Ben'
    FIRST_PLAYER_SCORE = 0
    SECOND_PLAYER_SCORE = 0
    # Skipped multiply numbers.
    skiped_nums = []

    for i in range(x):
        # for each round FIRST_PLAYER start play first.
        turn = FIRST_PLAYER
        round_list = [i for i in range(1, nums[i] + 1)]

        for num in range(len(round_list)):
            if is_prime(round_list[num]):
                if round_list[num] in skiped_nums:
                    continue
                # FIRST_PLAYER picks prime number and its multiple
                if turn == FIRST_PLAYER:
                    turn = SECOND_PLAYER
                    # Check if the multiple of prime number exists
                    if round_list[num] ** 2 in round_list:
                        index = round_list.index(round_list[num] ** 2)
                        skiped_nums.append(round_list[index])

                # SECOND_PLAYER picks prime number and its multiple
                elif turn == SECOND_PLAYER:
                    turn = FIRST_PLAYER

                    # Check if the multiple of prime number exists
                    if round_list[num] ** 2 in round_list:
                        index = round_list.index(round_list[num] ** 2)
                        skiped_nums.append(round_list[index])

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
