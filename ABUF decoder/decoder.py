import base64
import dns.message
import json
import json_convert

#here need to have a list of dicts

#if you want to add more data to the existing
def no_clear(json_data, result_data):
    for result in json_data:
        dns_message = dns.message.from_wire(base64.b64decode("54KAAAABAAEAAAAACGhvc3RuYW1lBGJpbmQAABAAA8AMABAAAwAAAAAAFhVuczMubmwtYW1zLmsucmlwZS5uZXQ="))
        result_data.write(str(dns_message) + "\n" + "--------------------------------------------\n")

#if you want a fresh data set
def clear(json_data, result_data):
    result_data.truncate(0)
    for result in json_data:
        dns_message = dns.message.from_wire(base64.b64decode("54KAAAABAAEAAAAACGhvc3RuYW1lBGJpbmQAABAAA8AMABAAAwAAAAAAFhVuczMubmwtYW1zLmsucmlwZS5uZXQ="))
        result_data.write(str(dns_message) + "\n" + "--------------------------------------------\n")

if __name__ == "__main__":
    result_data = open("results.txt", "w")
    json_convert.format_json()
    json_data = json.load(open("formatted_json.json", "r"))
    choice = input("clear or no clear?").lower()
    if (choice == "clear"):
        clear(json_data, result_data)
    else:
        no_clear(json_data, result_data)
    result_data.close()