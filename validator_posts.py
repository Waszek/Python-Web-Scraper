
def validate_post_title(title):
    if len(title) < 5:
        raise ValueError("Title is too short!")
    else:
        return True

if __name__ == "__main__":
    validate_post_title("abv")