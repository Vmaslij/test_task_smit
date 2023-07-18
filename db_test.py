from tortoise import fields
from tortoise.models import Model
from tortoise import Tortoise
from tortoise import run_async


class Rates(Model):
    id = fields.IntField(pk=True)
    data = fields.DateField()
    cargo_type = fields.CharField(max_length=255, default="Other")
    rate = fields.FloatField(default=0.04)

    def __str__(self):
        return f'date {self.data} type {self.cargo_type} rate = {self.rate}'


async def init():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['__main__']}
    )
    await Tortoise.generate_schemas()

if __name__ == '__main__':
    run_async(init())
