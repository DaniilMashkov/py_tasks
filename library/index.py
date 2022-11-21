import json


def save_file(data):
    with open('data/library.json', 'w') as file:
        file.write(json.dumps(data))


def check_user(func):
    with open('data/users.json', 'r') as users_file:
        users_json = users_file.read()
        users = json.loads(users_json)

        def wrapper(args):
            for user in users:
                if user['token'] == args['token']:
                    print(f'Привет, {user["name"]}')
                    return func(args['data'])
            return "Неверные данные пользователя\n"

    return wrapper


@check_user
def request_book(dct):
    with open('data/library.json', 'r') as lib_file:
        books = json.loads(lib_file.read())
        for book in books:
            if dct['id'] == book['id'] and book['availability']:
                book['availability'] = False
                save_file(books)
                return f'Выдана книга {book}\n'
        return "Книга не найдена или занята\n"


print(request_book({
    "token": "testtoken",
    "action": "getbook",
    "data": {
        "id": 2
    }
}))
print(request_book({
    "token": "abrakadabra",
    "action": "getbook",
    "data": {
        "id": 2
    }
}))
print(request_book({
    "token": "abraka",
    "action": "getbook",
    "data": {
        "id": 1
    }
}))
print(request_book({
    "token": "abrakadabra",
    "action": "getbook",
    "data": {
        "id": 1
    }
}))
