import time
import urllib.request
import generate_dictionary


# rules to be followed: https://internetstiftelsen.se/domaner/registrera-ett-domannamn/regler-och-beskrivning-av-domannamnssokningar/
# max 34 queries per s

delay_in_sec = 1 / 34


def check_two_letter_list():
    letter_list = generate_dictionary.get_two_letter_list()
    check_list(letter_list)


def check_three_letter_list_with_digits():
    letter_list = generate_dictionary.get_three_letter_list_with_digits()
    check_list(letter_list)


def check_three_letter_list():
    letter_list = generate_dictionary.get_three_letter_list()
    check_list(letter_list)


def check_four_letter_word_list():
    letter_list = generate_dictionary.get_four_letter_word_list()
    check_list(letter_list)


def check_five_letter_word_list():
    letter_list = generate_dictionary.get_five_letter_word_list()
    check_list(letter_list)


def check_list(letter_list):
    domains = []
    for domain in letter_list:
        new_domain = []
        new_domain.append(domain + ".se")
        domains.append(new_domain)

    for item in domains:
        page = urllib.request.urlopen('http://free.iis.se/free?q=' + item[0])
        result = page.read().decode('utf8').split(" ")[0]
        item.append(result)
        time.sleep(delay_in_sec)
        if result == 'free':
            print(item)


if __name__ == '__main__':
    check_five_letter_word_list()
