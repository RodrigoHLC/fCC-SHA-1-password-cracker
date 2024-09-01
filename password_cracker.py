import hashlib

def crack_sha1_hash(hash, use_salts = False):
    # READ top-10000-passwords.txt FILE
    with open("top-10000-passwords.txt", "r") as file:
        pass_list = file.read().split("\n")

    if use_salts:
        # READ known-salts.txt FILE
        with open("known-salts.txt", "r") as file:
            salt_list = file.read().split("\n") 

    for password in pass_list:
        if use_salts:
            for salt in salt_list:
                # === CHECKING FOR PREPENDED SALT ===
                prepended_salt = salt + password
                hashed_password = hashlib.sha1(f'{prepended_salt}'.encode("utf-8")).hexdigest()
                if hashed_password == hash:
                    return password
                # === CHECKING POR APPENDED SALT ===
                appended_salt = password + salt
                hashed_password = hashlib.sha1(f"{appended_salt}".encode("utf-8")).hexdigest()
                if hashed_password == hash:
                    return password

        else: # IF use_salts == False
            hashed_password = hashlib.sha1(f"{password}".encode("utf-8")).hexdigest()
            if hashed_password == hash:
                return password
            
    # === IF NO LOOP RETURNS A MATCH
    return "PASSWORD NOT IN DATABASE"
