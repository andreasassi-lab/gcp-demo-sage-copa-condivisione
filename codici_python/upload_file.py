from google.cloud import storage

# Crea il client Google Cloud Storage
client = storage.Client()

# Recupera il bucket
bucket = client.bucket("its-ict-andrea-sassi-docs")

# Definisce il nome che avrà il file su Google Cloud Storage
blob = bucket.blob("prova_caricamento.txt")

# Carica il file locale su Cloud Storage
blob.upload_from_filename("prova_caricamento.txt")

print("File caricato con successo!")