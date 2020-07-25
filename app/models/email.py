import uuid
from datetime import datetime

from django.db import models
from enumfields import Enum, EnumField

from .game import Game

class EmailRule(Enum):
    HUMAN = 'H'
    ZOMBIE = 'Z'
    ALL = 'A'


class EmailManager(models.Manager):
    def create_email(self, name: str, data : str, rule: EmailRule, game: Game) -> 'Email':
        email = self.model(name=name, data=data, rule=rule, game=game)
        email.save()
        return signup_location


class Email(models.Model):
    id: uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    game: Game = models.ForeignKey(Game, on_delete=models.PROTECT)
    name: str = models.CharField()
    data: str = models.CharField()
    rule: Enum = EnumField(enum=EmailRule, max_length=1)

    created_at: datetime = models.DateTimeField(auto_now_add=True)
    modified_at: datetime = models.DateTimeField(auto_now=True)

    objects = EmailManager()

    def __str__(self):
        return self.name
