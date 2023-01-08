age = input('Ile masz lat? ')
print("Masz", int(age) * 12, 'miesięcy')

km = int(input('Ile km przeszedłeś w tym tygodniu? '));
print('Okrążenie ziemi zajmie Ci', 40075 / km / 7, 'tygodni');

# wartość = wartość pocz. * (1 + procent / 100) ^ liczba lat
pocz = int(input("Podaj wartość początkową lokaty? "))
opr = int(input('Podaj oprocentowanie? '))
czas = int(input('Czas trwania w latach? '))
print('Wartość lokaty: ', (pocz * (1 + opr / 100) ** czas), ' zł')
