from fastapi import FastAPI

api = FastAPI(title="Mon API pour les Orange DE")


@api.get('/')
def get_index():
    return {
        "message": "Hello world!"
    }


@api.get(
    '/mon_endpoint',
    tags=["demo"],
    responses={
        200: {
            "description": "tout a marché comme sur des roulettes"
        },
        501: {
            "description": "tout va mal"
        }
    }
)
def get_mon_endpoint(nombre_entier: int):
    """Renvoie un modele de dictionnaire
    """
    return {
        "un_nombre": nombre_entier,
        "un_dictionnaire": {
            "une_clef": "une_valeur",
            "une_autre_clef": "une_autre_valeur"
        }
    }


@api.post('/mon_premier_post')
def post_mon_premier_post():
    return {
        "hello": "world"
    }


@api.get('/health')
def get_health():
    return {
        "status": 1
    }


@api.post('/')
def post_index():
    return {
        "status": 1
    }


@api.get("/bye")
def get_bye():
    return {
        "bye": "bye"
    }
