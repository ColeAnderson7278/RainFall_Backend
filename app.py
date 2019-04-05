import hug
import records

db = records.Database()

app = hug.http(
    response_headers={
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'OPTIONS, GET, POST',
    })


class Database:
    @staticmethod
    def high_score():
        return db.query(
            'SELECT name, number FROM scores ORDER BY number DESC LIMIT 5')

    @staticmethod
    def new_score(name, number):
        return db.query(
            'INSERT INTO scores (name, number) VALUES (:name, :number);',
            name=name,
            number=number)


@app.get('/high-score')
def high_score():
    high_score_from_db = Database.high_score()
    return {
        'name': high_score_from_db.name,
        'number': high_score_from_db.number,
    }


@app.post('/new-score')
def new_score(name: str, number: int):
    Database.new_score(name=name, number=number)
