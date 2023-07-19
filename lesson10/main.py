import psycopg2
from getpass import getpass


def check_existing_user(email):
    try:
        connection = psycopg2.connect(
            host='ep-empty-sea-524845.eu-central-1.aws.neon.tech',
            port='5432',
            database='neondb',
            user='op663246',
            password='5ELlvIaWx3JK'
        )

        cursor = connection.cursor()

        query = 'SELECT * FROM users WHERE email = %s'
        cursor.execute(query, (email,))
        existing_user = cursor.fetchone()

        cursor.close()
        connection.close()

        return existing_user

    except Exception as error:
        print('Виникла помилка при перевірці існуючого користувача: ', error)
        return None


def registration():
    username = input('Username: ')
    password = getpass()
    email = input('Email: ')

    existing_user = check_existing_user(email)
    if existing_user:
        print('Користувач з вказаним email уже існує! Спробуйте використати інший email.')
        return

    try:
        connection = psycopg2.connect(
            host='ep-empty-sea-524845.eu-central-1.aws.neon.tech',
            port='5432',
            database='neondb',
            user='op663246',
            password='5ELlvIaWx3JK'
        )

        cursor = connection.cursor()

        query = 'INSERT INTO users (username, password, email) VALUES (%s, %s, %s)'
        cursor.execute(query, (username, password, email))
        connection.commit()

        print('Користувача успішно зареєстровано!')
    except Exception as error:
        print('Виникла помилка при перевірці існуючого користувача: ', error)


def login():
    email = input('Email: ')
    password = getpass()

    try:
        connection = psycopg2.connect(
            host='ep-empty-sea-524845.eu-central-1.aws.neon.tech',
            port='5432',
            database='neondb',
            user='op663246',
            password='5ELlvIaWx3JK'
        )

        cursor = connection.cursor()

        query = 'SELECT * FROM users WHERE email = %s AND password = %s'
        cursor.execute(query, (email, password))

        user = cursor.fetchone()
        print(user)

        if user:
            print('Ви увійшли в систему!')
        else:
            print('Невірні облікові дані для входу.')

    except Exception as error:
        print('Виникла помилка при вході в систему: ', error)



if __name__ == '__main__':
    action = input('Виберіть дію: (login/register): ')

    if action == 'login':
        login()
    elif action == 'register':
        registration()
    else:
        print('Неправильна дія')