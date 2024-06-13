modes = ["normal"] #Maybe this should be stored somewhere else at some point when many different modes exist
# Other modes: Christmas, Cowboy


def get_normal_prompt():
    with open("./src/backend/prompts/normal_info_prompt.txt", "r") as file:
        return file.read()


if __name__ == "__main__":
    print(get_normal_prompt())  