import random
from math import floor

full_set = [[x, y] for y in range(7) for x in range(7) if x <= y]

while True:

    # Distribution of pieces
    random.shuffle(full_set)
    player = full_set[:7]
    computer = full_set[7:14]
    stock = full_set[14:]

    # Determining the first move
    for i in reversed(range(7)):
        if full_set.index([i, i]) < 7:
            snake = [[i, i]]
            player.remove([i, i])
            status = 0
            break
        elif full_set.index([i, i]) < 14:
            snake = [[i, i]]
            computer.remove([i, i])
            status = 1
            break
    else:
        continue
    break

while True:

    # Display interface
    print("=" * 70)
    print(f"Stock size: {len(stock)}")
    print(f"Computer pieces: {len(computer)}\n")
    if len(snake) < 6:
        print(*snake, sep="")
    else:
        print(*snake[:3], "...", *snake[-3:], sep="")
    print(f"\nYour pieces:")
    for x, y in enumerate(player, 1):
        print(f"{x}:{y}")

    # Analysis of game status
    draw = 0
    if len(computer) == 0:
        print("\nStatus: The game is over. The computer won!")
        break
    elif len(player) == 0:
        print("\nStatus: The game is over. You won!")
        break
    elif snake[0][0] == snake[-1][-1]:
        for i in range(1, 7):
            if len([y for x in snake for y in x if y == i]) >= 8:
                draw = 1
    if draw == 1:
        print("\nStatus: The game is over. It's a draw!")
        break
    elif status % 2 == 0:
        print("\nComputer is about to make a move. Press Enter to continue...")
    else:
        print("\nIt's your turn to make a move. Enter your command.")

    while True:

        # Computer move
        if status % 2 == 0:
            subject = computer
            input()
            numbers = [y for x in computer for y in x]
            snake_numbers = [y for x in snake for y in x]
            amounts = {}
            for i in range(7):
                if numbers.count(i) > 0:
                    amounts[i] = numbers.count(i) + snake_numbers.count(i)
            while len(amounts) > 0:
                current = max(amounts, key=amounts.get)
                if current == snake[-1][-1]:
                    number = floor(numbers.index(current) / 2) + 1
                    break
                elif current == snake[0][0]:
                    number = -abs(floor(numbers.index(current) / 2 + 1))
                    break
                else:
                    amounts.pop(current)
                    continue
            else:
                number = 0

        # Player move
        else:
            subject = player
            number = input()
            try:
                player[abs(int(number)) - 1]
            except (ValueError, IndexError):
                print("Invalid input. Please try again.")
                continue
            number = int(number)

        # Application of a move
        if number > 0:
            number -= 1
            if snake[-1][-1] == subject[number][0]:
                snake.append(subject[number])
                subject.pop(number)
                break
            elif snake[-1][-1] == subject[number][1]:
                snake.append(list(reversed(subject[number])))
                subject.pop(number)
                break
            else:
                print("Illegal move. Please try again.")
                continue
        elif number < 0:
            number = abs(number) - 1
            if snake[0][0] == subject[number][1]:
                snake.insert(0, subject[number])
                subject.pop(number)
                break
            elif snake[0][0] == subject[number][0]:
                snake.insert(0, list(reversed(subject[number])))
                subject.pop(number)
                break
            else:
                print("Illegal move. Please try again.")
                continue
        elif len(stock) > 0:
            piece = random.choice(stock)
            subject.append(piece)
            stock.remove(piece)
            break
        break

    status += 1
