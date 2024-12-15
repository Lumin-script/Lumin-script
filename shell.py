import run as r


while True:
    text = input('basic >')
    result, err = r.run('<stdio>', text)
    if err:
        print(err.as_string())
    else:
        print(result)

