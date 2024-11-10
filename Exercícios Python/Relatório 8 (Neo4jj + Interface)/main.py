from game import Game

def create_player(game):
    name = input("Digite o nome do jogador: ")
    player_id = input("Digite o ID do jogador: ")
    game.create_player(name, player_id)
    print("Jogador criado com sucesso!")

def update_player(game):
    player_id = input("Digite o ID do jogador que deseja atualizar: ")
    new_name = input("Digite o novo nome do jogador: ")
    game.update_player(player_id, new_name)
    print("Jogador atualizado com sucesso!")

def delete_player(game):
    player_id = input("Digite o ID do jogador que deseja excluir: ")
    game.delete_player(player_id)
    print("Jogador excluído com sucesso!")

def create_match(game):
    match_id = input("Digite o ID da partida: ")
    players = input("Digite os IDs dos jogadores participantes separados por vírgula: ").split(',')
    result = input("Digite o resultado da partida: ")
    game.create_match(match_id, players, result)
    print("Partida criada com sucesso!")

def get_player_matches(game):
    player_id = input("Digite o ID do jogador: ")
    player_matches = game.get_player_matches(player_id)
    print(f"Histórico de partidas do jogador {player_id}:")
    for match_id, result in player_matches:
        print(f"ID da partida: {match_id}, Resultado: {result}")

def get_match_info(game):
    match_id = input("Digite o ID da partida: ")
    match_info = game.get_match_info(match_id)
    print("Informações sobre a partida:")
    print("ID da partida:", match_info["match_id"])
    print("Resultado:", match_info["result"])
    print("Jogadores:")
    for player_id, name in match_info["players"]:
        print(f"ID do jogador: {player_id}, Nome do jogador: {name}")

def get_all_players(game):
    players = game.get_all_players()
    print("Lista de todos os jogadores:")
    for player_id, name in players:
        print(f"ID do jogador: {player_id}, Nome do jogador: {name}")

def main():
    uri = "neo4j+s://718f53be.databases.neo4j.io"
    user = "neo4j"
    password = "N4hGg_ynLcFvZJR99Y85aW0V2Ob75C-slQWSIQYzL88"
    game = Game(uri, user, password)

    while True:
        print("\nMenu:")
        print("1. Criar jogador")
        print("2. Atualizar jogador")
        print("3. Excluir jogador")
        print("4. Criar partida")
        print("5. Histórico de partidas de um jogador")
        print("6. Informações sobre uma partida")
        print("7. Listar todos os jogadores")
        print("8. Sair")

        choice = input("Escolha uma opção: ")

        switch = {
            "1": create_player,
            "2": update_player,
            "3": delete_player,
            "4": create_match,
            "5": get_player_matches,
            "6": get_match_info,
            "7": get_all_players,
            "8": lambda _: exit()
        }

        action = switch.get(choice)
        if action:
            action(game)
        else:
            print("Opção inválida. Tente novamente.")

    game.db.close()

if __name__ == "__main__":
    main()
