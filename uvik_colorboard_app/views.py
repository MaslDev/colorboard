from django.http import JsonResponse
from django.shortcuts import render
from .models import History


def home(request):
    return render(request, 'uvik_colorboard_app/page_home.html')


def play(request):
    response_data = {}
    number_of_players = int(request.POST['number_of_players'])
    number_of_squares = int(request.POST['number_of_squares'])
    number_of_cards = int(request.POST['number_of_cards'])
    characters_on_board = str(request.POST['characters_on_board']).upper()
    cards_in_deck = str(request.POST['cards_in_deck']).split(',')
    winner = 0
    cards_used = 0
    player_board_position = [-1] * number_of_players
    for card_index in range(number_of_cards):
        card = cards_in_deck[card_index]
        cards_used += 1
        player = card_index % number_of_players
        for card_character in card:
            for k in range(player_board_position[player] + 1, number_of_squares):
                if (card_character in characters_on_board[k]):
                    player_board_position[player] = k
                    break
            else:
                winner = player + 1
            if (player_board_position[player] == number_of_squares - 1):
                winner = player + 1
        if (winner != 0):
            break
    if (winner == 0):
        response_data['result'] = 'No​ ​player​ ​won​ ​after​ {} cards'.format(cards_used)
    else:
        response_data['result'] = 'Player​ ​{} ​won​ ​after​ ​{}​ ​cards'.format(winner, cards_used)
    History.objects.create(number_of_players=number_of_players, number_of_squares=number_of_squares,
                           number_of_cards=number_of_cards, characters_on_board=characters_on_board,
                           cards_in_deck=request.POST['cards_in_deck'], winner=winner, cards_used=cards_used)
    return JsonResponse(response_data)


def history(request):
    return render(request, 'uvik_colorboard_app/page_history.html', {'history': History.objects.all()})
