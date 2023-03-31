# class Operador(str, Enum):
_operator_list = (
    'Grupo LATAM',
    'Sky Airline',
    'Aerolineas Argentinas',
    'Copa Air',
    'Latin American Wings',
    'Avianca',
    'JetSmart SPA',
    'Gol Trans',
    'American Airlines',
    'Air Canada',
    'Iberia',
    'Delta Air',
    'Air France',
    'Aeromexico',
    'United Airlines',
    'Oceanair Linhas Aereas',
    'Alitalia',
    'K.L.M.',
    'British Airways',
    'Qantas Airways',
    'Lacsa',
    'Austral',
    'Plus Ultra Lineas Aereas',
)

operators = tuple(x.lower() for x in _operator_list)
