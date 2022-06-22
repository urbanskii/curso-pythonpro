"""

4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.


"""


letra = input('Informe a letra: ')

vogais = ["a","e","i","o","u"]
y =0

for x in vogais:
    if letra == x:
        print(f'Letra digitada é vogal! {letra}')
        break;
    y = y+1
    if len(vogais) == y:
        print(f'Letra digitada é consoante! {letra}')
        break;
    
