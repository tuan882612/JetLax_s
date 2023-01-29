import bcrypt

def hashPsw(psw: str) -> str:
    return bcrypt.hashpw(
        psw.encode('utf-8'),
        bcrypt.gensalt(rounds=12)
    )