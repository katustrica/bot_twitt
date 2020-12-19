from marshmallow import Schema, fields, post_load
import configparser
from pathlib import Path
from datetime import datetime


class User():
    def __init__(self, name: str, id: int, score: int = 0):
        """
        Класс пользователя

        Parameters
        ----------
        name : str
            Имя пользователя
        score : int, optional
            Количество очков пользователя, by default 0
        """
        self.name = name
        self.score = score
        self.id = id

    def add_score(self):
        """
        Добавляет пользователю 1 балл
        """
        self.score += 1

    @property
    def result(self) -> str:
        """
        Отправляет результат администратору
        """
        return f'Пользователь {self.name} набрал {self.score} очков.'


class UserSchema(Schema):
    name = fields.Str()
    score = fields.Int()
    id = fields.Int()

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)

class MessageSchema(Schema):
    title = fields.Str()
    author = fields.Str()
    url = fields.Str()
    create_date = fields.Int()

    @post_load
    def make_message(self, data, **kwargs):
        return (
            _('Title') + f": {data['title']}\n"
            _('Author') + f": {data['author']}\n"
            _('Url') + f": {data['url']}\n"
            _('Create_date') + f": {datetime.fromtimestamp(data['create_date']).strftime('%I:%M, %d %B, %Y')}"
        )

config = configparser.ConfigParser()
config.read('config.ini')
path = Path(config['paths']['users'])
if not path.exists():
    path.mkdir(parents=True, exist_ok=False)

def get_all_users():
    """
    Возвращает всех пользователей
    """
    users_path = path / config['paths']['users_json']
    with(users_path.open('r+')) as outfile:
        all_users = UserSchema(many=True).loads(outfile.read())
    return {user.id: user for user in all_users}


def set_all_users(all_users):
    """
    Устанавливает всех пользователей по значению value

    Parameters
    ----------
    value :
        Список пользователей
    """
    users_path = path / config['paths']['users_json']
    with(users_path.open('w+')) as outfile:
        outfile.write(UserSchema(many=True).dumps(all_users))
