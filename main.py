from passpal.passpal import PassPal

if __name__ == '__main__':
    p = PassPal(pass_len=12)
    print(p.generate_password())
