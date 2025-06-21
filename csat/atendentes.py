from faker import Faker
import pandas as pd
import random
import csv

fake = Faker(locale='pt-BR')

cpf = []
nome = []

for i in range(0, 20):
    cpf.append(fake.cpf())
    nome.append(fake.name())

    df = pd.DataFrame(
        {
            'CPF': cpf,
            'Atendente': nome
        }
    )

df.to_csv('./ATENDENTES_FAKES.CSV', index=False)