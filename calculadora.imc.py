
nome= input("escreva o seu nome?")
peso= float(input("qual é o seu peso?"))
altura = float(input("qual é sua altura?"))

resultado= peso/(altura* altura)

if resultado <= 18.5: 
    print("abaixo peso")
elif resultado <= 18.5:
    print("peso normal")
elif resultado <= 25.0:
    print(f"sobrepeso {resultado}⚠️ Cuidado com a Saúde")
elif resultado <= 30.0:
    print("obesidade grau 1")
elif resultado<= 35.0:
    print("obesidade grau 2")
else:
    print("peso invalido")

print(f"usuario {nome} seu estado é {resultado} ")
 

 
