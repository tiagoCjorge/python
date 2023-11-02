n1 = float(input("Introduza o primeiro numero do calculo - "))
o = input("Introduza a operação a fazer - ")
n2 = float(input("Introduza o segundo numero do calculo - "))


match o:
    case "*":
        print("Resultado : ", round(n1 * n2, 2))
    case "/":
        print("Resultado : ", round(n1 / n2, 2))
    case "+":
        print("Resultado : ", round(n1 + n2, 2))
    case "-":
        print("Resultado : ", round(n1 - n2, 2))
