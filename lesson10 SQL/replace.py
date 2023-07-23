import psycopg2

def replace(email: str, new_age: int):
    try:
        connection = psycopg2.connect(
            host='ep-empty-sea-524845.eu-central-1.aws.neon.tech',
            port='5432',
            database='neondb',
            user='op663246',
            password='5ELlvIaWx3JK'
        )

        cursor = connection.cursor()

        query = 'SELECT * FROM students WHERE email = %s'
        cursor.execute(query, (email,))

        user = cursor.fetchone()

        if user:
            user_id = user[0]
            update_query = 'UPDATE students SET age = %s WHERE id = %s'
            cursor.execute(update_query, (new_age, user_id))
            connection.commit()
            print('Знайдено користувача та змінено вік.')
        else:
            print('Незнайдено такого користувача.')

        cursor.close()
        connection.close()

    except Exception as error:
        print('Виникла помилка при вході в систему:', error)


if __name__ == "__main__":
    email = input('Email: ')
    new_age = int(input('New age: '))
    replace(email, new_age)

