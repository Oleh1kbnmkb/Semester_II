import psycopg2


def create_students_table():
    try:
        connection = psycopg2.connect(
            host='ep-empty-sea-524845.eu-central-1.aws.neon.tech',
            port='5432',
            database='neondb',
            user='op663246',
            password='5ELlvIaWx3JK'
        )

        cursor = connection.cursor()

        create_table_query = '''
            CREATE TABLE IF NOT EXISTS students (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                age INTEGER NOT NULL,
                email VARCHAR(100) NOT NULL
            )
        '''

        cursor.execute(create_table_query)
        connection.commit()

        cursor.close()
        connection.close()

        print("Таблиця 'students' успішно створена!")

    except Exception as error:
        print('Виникла помилка при створенні таблиці: ', error)


def add_student(name, age, email):
    try:
        connection = psycopg2.connect(
            host='ep-empty-sea-524845.eu-central-1.aws.neon.tech',
            port='5432',
            database='neondb',
            user='op663246',
            password='5ELlvIaWx3JK'
        )

        cursor = connection.cursor()

        insert_query = '''
            INSERT INTO students (name, age, email)
            VALUES (%s, %s, %s)
        '''

        cursor.execute(insert_query, (name, age, email))
        connection.commit()

        cursor.close()
        connection.close()

        print(f"Студент {name} успішно доданий до таблиці 'students'!")

    except Exception as error:
        print('Виникла помилка при додаванні студента: ', error)
        
        
        
        
def get_students():
    try:
        connection = psycopg2.connect(
            host='ep-empty-sea-524845.eu-central-1.aws.neon.tech',
            port='5432',
            database='neondb',
            user='op663246',
            password='5ELlvIaWx3JK'
        )

        cursor = connection.cursor()

        query = '''
            SELECT email FROM students WHERE email LIKE '%k%'
        '''

        cursor.execute(query)
        students_k = cursor.fetchall()

        cursor.close()
        connection.close()

        if students_k:
            print("Електронні адреси студентів з літерою 'k':")
            for email in students_k:
                print(email[0])
        else:
            print("Не знайдено студентів з літерою 'k' у їх електронній адресі.")

    except Exception as error:
        print('Виникла помилка: ', error)


if __name__ == '__main__':

    # name = input('Введіть ім\'я студента: ')
    # age = int(input('Введіть вік студента: '))
    # email = input('Введіть електронну адресу студента: ')

    # add_student(name, age, email)
    get_students()


