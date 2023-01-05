    import random
    #random kütüphanesini tanımlıyoruz.
class SupurgeDunyası ():
    def __init__(self):
        self.durumlar = {'lok_A' : random.choice(['Temiz','Kirli']),
                        'lok_B' : random.choice(['Temiz','Kirli'])}
    #sınıfımızı oluşturup fonksiyonumuzu tanımlıyoruz. Sözlük tipini kullanıyoruz. lokasyon a ve b ye bak temiz mi kirli mi, random fonksiyonuyla lokasyonları rastgele seçecek.
        self.done = False
    def hareket_al(self,agent,hareket):
    #False dönerse ajanla hareket al.
        if (hareket == "Sağ"):
            agent.location = "lok_B"
            agent.performance -= 1
    #hareket sağ'a eşitse ajan lokasyonu B ve performansı 1 azalt.
        elif(hareket == "Sol"):
            agent.location = "Lok_A"
            agent.performance -= 1
    #hareket sola eşit ise ajan lokasyonu A ve performansı 1 azalt.
        elif(hareket == "Çek"):
            if(self.durumlar[agent.location] == "Kirli"):
                agent.performance += 10
                self.durumlar[agent.location] = "Temiz"
    #bulundupu lokasyon kirli ise çek yani temizle ve performansı 10 arttır (ödüllendir). bulunan lokasyonu temiz e çevir.
        if (self.durumlar["lok_A"] == "Temiz" and self.durumlar["lok_B"] == "Temiz"):
            self.done = True
    #lokasyon A ve B temiz ise işlem tamam.
    def random_baslangıc(self):
        return random.choice(["lok_A","lok_B"])
    #Ajanlar için başlangıç belirledik.
class Agent():
    def __init__(self,location):
        self.performance = 0
        self.location = location
    def hareket_sec(self):
        return random.choice(["Sağ","Sol","çek"])
    #ajanlarımızın sınıfını oluşturduk.

env = SupurgeDunyası()
agent = Agent(env.random_baslangıc)
    #ajanı random başlattık

while (not env.done):
    #env tamamlanmadığı sürece bunu yap.
    agent_hareket = agent.hareket_sec()
    print(agent_hareket)
    print(agent.location)
    print(env.durumlar)
    env.hareket_al(agent,agent_hareket)


print(agent.performance)