def convbrail(text):
    code_point = ord(text)

    if not (0x2800 <= code_point <= 0x28FF):
        return None

    offset = code_point - 0x2800

    dots = [
        (offset & 0b00000001) != 0,  # 点1
        (offset & 0b00000010) != 0,  # 点2
        (offset & 0b00000100) != 0,  # 点3
        (offset & 0b00001000) != 0,  # 点4
        (offset & 0b00010000) != 0,  # 点5
        (offset & 0b00100000) != 0,  # 点6
    ]

    if code_point >= 0x2840:
        dots.append((offset & 0b01000000) != 0)  # 点7
        dots.append((offset & 0b10000000) != 0)  # 点8

    elif code_point >= 0x2800:
        pass 
    return dots
