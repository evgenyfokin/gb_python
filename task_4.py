for origin in ['разработка', 'администрирование', 'protocol', 'standart']:
    enc = origin.encode('utf-8')
    dec = enc.decode('utf-8')
    print(f"Original: {origin}; Encoded: {enc}; Decoded: {dec}")
