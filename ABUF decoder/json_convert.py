def format_json():#can also just use file_path as argument, then open that file
    json_file = open("data.json", "r")
    result_file = open("formatted_json.json", "w")
    result_file.truncate(0)

    result_file.write("[\n")
    all_text = json_file.readlines()
    joined_text = "".join(all_text)
    joined_text = joined_text.replace("}\n{\n", "},\n{\n", joined_text.count("}\n{\n"))
    result_file.write(joined_text)
    result_file.write("]")

    json_file.close()
    result_file.close()