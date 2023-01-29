import bcrypt

def hashPsw(psw: str) -> bytes:
    return bcrypt.hashpw(
        psw.encode('utf-8'),
        bcrypt.gensalt(rounds=12)
    )
    
def validatePsw(psw: str, hPsw: bytes) -> bool:
    return str(psw.encode('utf-8')) == hPsw