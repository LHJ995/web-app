#적등장 시 행동할 때
def enemy(play):
    if play == '1':
        print("적이 사망했습니다.")
    else:
        print("당신은 사망하였습니다.")

def idpw_ck(id, pw):
    if id == "id" and pw == "1234":
        return "로그인 되었습니다."
    else:
        return "ERROR"