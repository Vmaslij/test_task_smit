from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date
from typing import Union, List
from tortoise import run_async, Tortoise
from db_test import Rates
import uvicorn


class Rate(BaseModel):
    date: date
    cargo_type: Union[str, None] = "Other"
    price: Union[int, float, None] = 0


class DataFields(BaseModel):
    cargo_type: Union[str, None] = "Other"
    rate: Union[float, None] = 0.04


class DateRates(BaseModel):
    date: date
    data: List[DataFields]


class AllDateRates(BaseModel):
    description: List[DateRates]


app = FastAPI()


async def connect_db():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['db_test']}
    )


@app.get("/")
async def check_connection():
    return "Connected"


@app.post("/set_rates")
async def upload_data(data: AllDateRates):
    await connect_db()
    for daterates in data.description:
        for rates in daterates.data:
            await Rates.get_or_create(data=daterates.date, cargo_type=rates.cargo_type, rate=rates.rate)
    await Tortoise.close_connections()
    return "Rates data is loaded"


@app.post("/get_price")
async def calc_price(item: Rate):
    await connect_db()
    q = await Rates.filter(data=item.date, cargo_type=item.cargo_type)
    await Tortoise.close_connections()
    if not q:
        return "Rate for specified date and cargo type not found"
    return item.price * q[0].rate


if __name__ == '__main__':
    uvicorn.run("main_smit:app")
    run_async(Tortoise.close_connections())
