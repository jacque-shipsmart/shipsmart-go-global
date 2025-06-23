import random
import json

def jogar_dado():
    return random.randint(1, 6)

def obter_proxima_casa(atual, dado, max_casas):
    nova = atual + dado
    return nova if nova < max_casas else max_casas - 1

def carregar_dados():
    with open("casas.json", "r") as f:
        casas = json.load(f)
    with open("cartas.json", "r") as f:
        cartas = json.load(f)
    return casas, cartas
