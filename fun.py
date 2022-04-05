import datetime
import wikipedia

def horas():
    hora = datetime.datetime.now().strftime('%H:%M')
    return hora

def dia():
    dia_sem = datetime.datetime.now().strftime("%A")
    match dia_sem:
        case "Monday":
            d_s = "Segunda-feira"
        case "Tuesday":
            d_s = "Terça-feira"
        case "Wednesday":
            d_s = "Quarta-feira"
        case "Thursday":
            d_s = "Quinta-feira"
        case "Friday":
            d_s = "Sexta-feira"
        case "Saturday":
            d_s = "Sábado"
        case "Sunday":
            d_s = "Domingo"

    mes = datetime.datetime.now().strftime("%B")
    match mes:
        case "January":
            ms = "Janeiro"
        case "February":
            ms = "Fevereiro"
        case "March":
            ms = "Março"
        case "April":
            ms = "Abril"
        case "May":
            ms = "Maio"
        case "June":
            ms = "Junho"
        case "July":
            ms = "Julho"
        case "August":
            ms = "Agosto"
        case "September":
            ms = "Setembro"
        case "October":
            ms = "Outubro"
        case "November":
            ms = "Novembro"
        case "December":
            ms = "Dezembro"


    dia = datetime.datetime.now().strftime("%d")
    if dia[0] == "0":
        dia = dia.replace("0","")

    ano = datetime.datetime.now().strftime("%Y")

    hoje = d_s + ". " + dia + " de " + ms + " de " + ano
    return hoje

def wiki(comando):
    if 'quem foi' in comando:
        comando = comando.replace('quem foi ', '')
    elif 'quem é' in comando:
        comando = comando.replace('quem é ', '')
    elif 'você conhece' in comando:
        comando = comando.replace('você conhece ', '')
    elif 'o que é' in comando:
        comando = comando.replace('o que é ', '')

    wikipedia.set_lang('pt')
    comando = wikipedia.summary(comando, 1)
    return comando
