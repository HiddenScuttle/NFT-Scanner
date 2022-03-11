import libreria

print("Il seguente programa salva le transazioni in ERC-721 per il contratto "+libreria.get_contractaddress()+" utilizzando l'API key "+libreria.get_apikey())
print("Il blocco di partenza è il n° "+libreria.get_startblock())
lastblock=libreria.get_number_block()
print("L'ultimo blocco di etherscan è il n° "+lastblock)
print("Inizio a fare le query e memorizzarle")
libreria.query_request(lastblock)
print("Ho finito tutto le richieste")
print("Adesso salvo il file json")
libreria.write_json()
print("File json salvato")