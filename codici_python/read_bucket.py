from google.cloud import storage

# Crea il client Google Cloud Storage
client = storage.Client()

# Recupera il bucket
bucket = client.bucket("its-ict-andrea-sassi-docs")

# Recupera il file
blob = bucket.blob("Prova.txt")

# Legge il contenuto e lo stampa
contenuto = blob.download_as_text()

print(contenuto)