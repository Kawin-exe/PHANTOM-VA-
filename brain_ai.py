def ask_ai(prompt):

    if "who is" in prompt:
        return "He is a person, but I need internet to give full details."

    elif "hello" in prompt:
        return "Hello, how can I assist you?"

    elif "how are you" in prompt:
        return "I am operating perfectly."

    else:
        return "I am still learning."