def response(input_message):
    message = input_message.lower()

    if message == 'nice':
        return 'Very nice'
    elif message == 'hello':
        return 'Hello there'
    elif message == 'hi':
        return 'hey'
    elif message == 'sup':
        return 'nm'
    elif message == 'thanks':
        return 'np:)'
    elif message == 'how are you':
        return 'fine and u?'
    else:
        return 'gtg, will chat later'
