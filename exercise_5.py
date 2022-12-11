import random


def rolls():
    """
    This function calculates the dice roll from a pattern of input in format xDy+z.
    :return: int
    """
    dice_string = input("Enter which roll you need in format xDy+z: ")
    allowed_dice_types = [3, 4, 6, 8, 10, 12, 20, 100]
    try:
        dice_list = [x for x in dice_string]
        number_of_rolls = int(dice_list[0])
        dice_type = int(dice_list[2])
        if dice_type not in allowed_dice_types or dice_list[1] != "D":
            return "Non-existent dice type!"
        increased_result_list = dice_list[4:]
        increase_result = int(''.join(increased_result_list))
    except ValueError:
        return "The roll format is incorrect!"
    one_roll = random.randint(1, dice_type)
    result = one_roll * number_of_rolls + increase_result
    return f"Your roll is: {result}"


if __name__ == '__main__':
    rolls()
