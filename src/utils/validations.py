import re


class Validations():
    def valide_str_dct(self, dct: dict) -> bool:
        ans = True
        for keys in dct:
            if type(dct[keys]) is not str:
                ans = False
                break
        return ans

    def valide_void_dct(self, dct: dict) -> bool:
        ans = False
        for keys in dct:
            if dct[keys] == '':
                ans = True
                break
        return ans

    def valide_keys_in(self, dct: dict, required: list) -> bool:
        ans = True
        for keys in required:
            if keys not in dct:
                ans = False
                break
        return ans

    def valide_email(self, email):
        # Validar longitud
        min_len = 6
        max_len = 50
        if len(email) < min_len or len(email) > max_len:
            return False

        # Validar formato de correo electrónico
        rex_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(rex_email, email):
            return False

        return True

    def valide_password(self, password):
        # Validar longitud
        min_len = 8
        max_len = 20
        if len(password) < min_len or len(password) > max_len:
            return False

        # Validar caracteres especiales
        chars = ['!', '#', '$', '%', '^', '&', '*',
                 '(', ')', '-', '_', '+', '=', '/', '\\',
                 ',', '.', ':', ';', '?']
        if any(char in password for char in chars):
            return False

        return True
