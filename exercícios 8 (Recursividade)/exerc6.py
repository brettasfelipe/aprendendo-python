"""
Crie um programa que chama uma função de nome simples, que lê uma string a digitada pelo usuário.

Se a string a for "repete", é impressa a mensagem "Olá! Vamos repetir!" e é feita uma chamada recursiva para a função simples.
"""

def simples(a):
    if a != "repete": # Caso base
        return
    elif a == "repete":
        print("Olá! Vamos repetir!")
        return simples(input()) # Chama a função esperando um input que talvez se aproxime do caso base

simples(input())