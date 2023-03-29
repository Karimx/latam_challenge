from enum import Enum

from pydantic import BaseModel

# class Operador(str, Enum):
_operator_list = ('Grupo LATAM', 'Sky Airline', 'Aerolineas Argentinas', 'Copa Air',
                  'Latin American Wings', 'Avianca', 'JetSmart SPA', 'Gol Trans',
                  'American Airlines', 'Air Canada', 'Iberia', 'Delta Air', 'Air France',
                  'Aeromexico', 'United Airlines', 'Oceanair Linhas Aereas', 'Alitalia',
                  'K.L.M.', 'British Airways', 'Qantas Airways', 'Lacsa', 'Austral',
                  'Plus Ultra Lineas Aereas')

operators = tuple(x.lower() for x in _operator_list)


def operator_index(index: int):
    try:
        return operators[index]

    except IndexError:
        return None


class TipoVuelo(str, Enum):
    """
        Tipo de vuelo raw input feature
    """
    nacional = 'N'
    internacional = 'I'

    def __str__(self):
        return str(self.value)


class Mes(str, Enum):
    """
         Mes feature from date operation
     """
    enero = "0"
    febrero = "1"
    marzo = "2"
    abril = "3"
    mayo = "4"
    junio = "5"
    julio = "6"
    agosto = "7"
    septiembre = "8"
    octubre = "9"
    noviembre = "10"
    diciembre = "11"

    def __str__(self):
        return str(self.value)

class PredictionInput(BaseModel):
    operator: str  # o poner int?
    flight_type: TipoVuelo
    month: Mes
    proba: bool = True


class PredictionOutput(BaseModel):
    delay_proba = str


delay_labels = {
    0: 'No Delay',
    1: 'Delay'
}
