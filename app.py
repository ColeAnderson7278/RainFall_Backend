import hug
import records

db = records.Database()

app = hug.API(__name__)

app.http.add_middleware(hug.middleware.CORSMiddleware(app, max_age=10))


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

    @staticmethod
    def clear():
        db.execute('DELETE FROM scores;')


@hug.get('/high-scores')
def high_scores():
    formatted_scores = []
    for high_score in Database.high_scores():
        formatted_scores.append({
            'name': high_score.name,
            'number': high_score.number,
        })
    return formatted_scores


@hug.post('/new-score')
def new_score(name: str, number: int):
    Database.new_score(name=name, number=number)
