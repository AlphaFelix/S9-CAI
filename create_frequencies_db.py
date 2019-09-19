import sqlite3


sql_create_freq_table = """ CREATE TABLE frequencies (
                                octave INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                C float,
                                CSharp float,
                                D float,
                                DSharp float,
                                E float,
                                F float,
                                FSharp float,
                                G float,
                                GSharp float,
                                A float,
                                ASharp float,
                                B float
                            ); """

connect = sqlite3.connect("frequencies.db")
cursor  = connect.cursor()

cursor.execute("DROP TABLE IF EXISTS frequencies")
cursor.execute(sql_create_freq_table)

f0          = 440.0
frequencies = []
octave      = []

octave.append(3)

for j in range (-9, 3):     # les frequences des 12 notes de la gamme de degre 3 referencees par rapport au LA (A) 440 Hz
    frequency = f0*2**(j/12)
    octave.append(frequency)

frequencies.append(octave)

cursor.executemany("INSERT INTO frequencies VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?);", frequencies)
connect.commit()