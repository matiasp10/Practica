# =============================================
# Ejercicio: L1 - Set Alarm
# Plataforma: Codewars
# Enlace: https://www.codewars.com/kata/568dcc3c7f12767a62000038/train/python
# Autor: Mati
# Fecha: 2025-06-19
# Descripción:
# Write a function named setAlarm/set_alarm/set-alarm/setalarm (depending on language) which receives two parameters. The first parameter, employed, is true whenever you are employed and the second parameter, vacation is true whenever you are on vacation.

# The function should return true if you are employed and not on vacation (because these are the circumstances under which you need to set an alarm). It should return false otherwise. Examples:

# employed | vacation 
# true     | true     => false
# true     | false    => true
# false    | true     => false
# false    | false    => false
# =============================================


def set_alarm(employed, vacation):
    return employed and not vacation

set_alarm(True, True)
set_alarm(True, False)
set_alarm(False, True)
set_alarm(False, False)