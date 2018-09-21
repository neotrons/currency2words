# currency2words - Convierte valores monetarios a palabras en muntiples idiomas y monedas

Esta libreria esta inspirada y utiliza num2words para convertir numeros en palabras y extiende las funcionalidades del
metodo to_currecy de  dicha libria, esto permite tener  mas formatos de salida

to_currency de num2words es muy limitada por ello la necesidad de generar esta clase

### Uso

```python
from currency2words import Currency2Words
a = Currency2Words(42.5)
print(a) # curenta y dos soles con cincuenta centimos
```