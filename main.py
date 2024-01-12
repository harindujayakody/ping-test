import ping3
import time
import os
from colorama import init, Fore

# Initialize colorama for colored output
init(autoreset=True)

def format_response_time(response_time):
    return f'{response_time:.2f} ms'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        try:
            clear_screen()
            total_response_time = 0
            total_packets_sent = 0
            total_packets_received = 0
            minimum_time = float('inf')
            maximum_time = 0

            print(Fore.GREEN + "Ping Tool")
            print(Fore.YELLOW + "Enter the URL to ping (or 'q' to quit):")
            website_url = input(Fore.CYAN)

            if website_url.lower() == 'q':
                break

            for _ in range(4):
                response_time = ping3.ping(website_url, timeout=2)  # Adjust the timeout as needed
                if response_time is not None:
                    total_response_time += response_time
                    total_packets_sent += 1
                    total_packets_received += 1
                    minimum_time = min(minimum_time, response_time)
                    maximum_time = max(maximum_time, response_time)
                    print(Fore.GREEN + f'Response time for {website_url}: {format_response_time(response_time)}')
                else:
                    total_packets_sent += 1
                    print(Fore.RED + f'Packet loss for {website_url}')

            if total_packets_sent > 0:
                packet_loss_percentage = ((total_packets_sent - total_packets_received) / total_packets_sent) * 100
                print(Fore.GREEN + f'\nPing statistics for {website_url}:')
                print(Fore.GREEN + f'    Packets: Sent = {total_packets_sent}, Received = {total_packets_received}, Lost = {total_packets_sent - total_packets_received} ({packet_loss_percentage:.2f}% loss),')
                print(Fore.GREEN + f'Approximate round trip times in milli-seconds:')
                print(Fore.GREEN + f'    Minimum = {format_response_time(minimum_time)}, Maximum = {format_response_time(maximum_time)}, Average = {format_response_time(total_response_time / total_packets_received)}')

            input(Fore.YELLOW + "Press Enter to continue...")
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(Fore.RED + f'Error: {e}')

if __name__ == '__main__':
    main()
