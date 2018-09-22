# currency2words - Convierte valores monetarios a palabras en muntiples idiomas y monedas

Esta libreria esta inspirada y utiliza num2words para convertir numeros en palabras y extiende las funcionalidades del
metodo to_currecy de  dicha libria, esto permite tener  mas formatos de salida

to_currency de num2words es muy limitada por ello la necesidad de generar esta clase

### Uso

```python
from currency2words import Currency2Words
a = Currency2Words(42.5)
print(a) # cuarenta y dos soles con cincuenta centimos
```

Se incluyen 2 formatos de salida texto y factura, por defecto se incluye el formato texto **text**

```python
from currency2words import Currency2Words
a = Currency2Words(42.5, format='text')
print(a) # cuarenta y dos soles con cincuenta centimos

a = Currency2Words(42.5, format='invoice')
print(a) # cuarenta y dos con 50/100 centimos
```

Es posible llamar ambos metodos desde sus clases de renderizado

```python
from currency2words import Currency2Words
a = Currency2Words(42.5)
print(a.format_text()) # cuarenta y dos soles con cincuenta centimos
print(a.format_invoice()) # cuarenta y dos con 50/100 centimos
```
