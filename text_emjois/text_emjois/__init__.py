from colorama import init, Fore

init(autoreset=True)

class TextEmjoi:
  def __init__(self):
      self.emjois = {
        "smile": ":)",
        "hello": "",
      }
  
  def print_emjoi(self, emjoi: str):
    emjoitoprint = self.emjois.get(emjoi, f"{Fore.RED} Error: Invaild Emjoi!")
    print(emjoitoprint)

  def create_emjoi(self, emjoi_name: str, emjoi_vaule: str):
    if emjoi_name in self.emjois:
      print(f"{Fore.RED} Error: Emjoi Name Already exitis!")
      exit()
    self.emjois[emjoi_name] = emjoi_vaule

  def delete_emjoi(self, emjoi_name: str):
    try:
      self.emjois.pop(emjoi_name, None)
    except:
      print(f"{Fore.RED} Error: Invaild Emjoi!")
  
  def print_emjois(self):
    print(self.emjois)