# currency2words - Convierte valores monetarios a palabras en muntiples idiomas y monedas

Esta libreria esta inspirada y utiliza num2words para convertir numeros en palabras y extiende las funcionalidades del
metodo to_currecy de  dicha libria, esto permite tener  mas formatos de salida

to_currency de num2words es muy limitada por ello la necesidad de generar esta clase

### Uso

```python
from currency2words import Currency2Words
a = Currency2Words(42.5)
print(a) # cuarenta y dos soles con cincuenta céntimos
```

Se incluyen 2 formatos de salida (texto y factura) se incluye tambien un metodo para customizar la salida, por defecto 
es el formato texto **text**

```python
from currency2words import Currency2Words
a = Currency2Words(42.5, format='text')
print(a) # cuarenta y dos soles con cincuenta céntimos

a = Currency2Words(42.5, format='invoice')
print(a) # cuarenta y dos con 50/100 soles
```

Es posible llamar ambos metodos desde sus clases de renderizado

```python
from currency2words import Currency2Words
a = Currency2Words(42.5)
print(a.format_text()) # cuarenta y dos soles con cincuenta céntimos
print(a.format_invoice()) # cuarenta y dos con 50/100 soles
```

Personalizar la salida

```python
from currency2words import Currency2Words
a = Currency2Words(42.5)
# ejemplo para simular el formato invoice
print(a.format_custom('{iw} {s} {d}/100 {ic}')) #cuarenta y dos con 50/100 soles
print(a.format_custom('{integer_word} {separator} {decimal_part}/100 {integer_currency}')) #cuarenta y dos con 50/100 soles

```

Formato en palabra | Formato en caracter | Descripción | Ejemplo de salida
------------------ | ------------------- | ----------- | -----------------
{number} | {n} | número ingresado | 42.5
{negword} | {ng} | palabra si es negativo | menos
{integer_part} | {i} | parte entera del numero | 42
{integer_word} | {iw} | parte entera en palabra | cuarenta y dos
{integer_currency} | {ic} | moneda de la parte entera | soles
{separator} | {s} | separador | con
{decimal_part} | {d} | parte decimal del numero | 50
{decimal_word} | {dw} | parte decimal en palabra | cincuenta
{decimal_currency} | {dc} | moneda de la parte decimal | céntimos
