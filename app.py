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
    def high_scores():
        return db.query(
            'SELECT name, number FROM scores ORDER BY number DESC LIMIT 5')

    @staticmethod
    def new_score(name, number):
        return db.query(
            'INSERT INTO scores (name, number) VALUES (:name, :number);',
            name=name,
            number=number)


@app.get('/high-scores')
def high_scores():
    formatted_scores = []
    for high_score in Database.high_scores():
        formatted_scores.append({
            'name': high_score.name,
            'number': high_score.number,
        })
    return formatted_scores


@app.post('/new-score')
def new_score(name: str, number: int):
    Database.new_score(name=name, number=number)
