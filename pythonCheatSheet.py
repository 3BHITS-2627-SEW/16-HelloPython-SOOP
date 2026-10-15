##Datei: pythoncheatsheet.py
##ausfueren: python pythoncheatsheet.py
##BZW: py pythoncheatsheet.py

##Dies ist ein kleines Cheat-Sheet fuer die Verwendung von python fuer C und C++ Programmierer

#Variable
#int einezuahl = 43;
eineVariable = 13
print("eineVariable", eineVariable)
eineVariable = "blablabla"
print("eineVariable", eineVariable)
# typisierung in python: ducktyping
# daher: bitte immer nach möglichkeit typisieren
eineZweiteVariable : int = 14
print("eineZweiteVariable", eineZweiteVariable)
eineZweiteVariable = "Text"
print("eineZweiteVariable", eineZweiteVariable**3)
#erzeugtz leider erste den fehler zur laufzeit!
#print("einezweitevariable", einezweitevariable**3)

datenTyp = type(eineVariable)
print("datentyp von eineVariable: ", datenTyp)
eineVariable = 15

datenTyp = type(eineVariable)
print("Datentyp von eineVariable: " ,datenTyp)

#formatierte Ausgabe
#C: printf("zahl lautet %i und ist cool!\n", ineVariable);
print("Zahl lautet %i \n und ist Cool", eineVariable)
#formatiete strings
einText = f"Zahl lautet {eineVariable**2} \n und ist Cool"


alternativText = "Zahl lautet"+eineVariable*2+"\n und ist cool!"
print(einText)
print("alternativ-text: ", alternativText)

#eingabe von der kommandozeile
#int i = 0
#printf("bitte zuzahl eingeben\n");
#scanf("%i",&i);

einegeleesneZahl = int(input("Bitte Zahl eingeben: "))
print("zahl eingelesen vom Typ", type(einegeleesneZahl))

#Funtionen
#int main(void){
#printf("Hallo funktionen");
#}

def main():{
    print("hallo main!")
}

main()
