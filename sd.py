class Rekins():
    def __init__(self,klients, veltijums, izmers, materials):
        self.klients = klients
        self.veltijums = veltijums
        self.izmers = izmers
        self.materials = materials
        self.laiks = datetime.datetime.now()

    """
    Klasei Rekins pievieno metodi izdrukat(), kas izvada uz ekrāna glīti noformētu
    informāciju par rēķinu!
    """

    """
    Uzlabo klases Rekins metodi izdrukat(), lai tā drukātu arī aprēķināto apmaksas summu no
    metodes aprekins()!
    """

    """
    Papildini programmu, lai tā izsauc metodi saglabat() pirms rēķina izdrukāšanas!
    """
    def izdrukat(self):
        self.saglabat()
        print("klienta vārds:",self.klients)
        print("veltijums:",self.veltijums)
        print("izmērs(platums, garums. augstums):",self.izmers)
        print("materiāla cena m2:",self.materials)
        print("Rekina summa:",self.aprekins())
        print("Laiks:",self.laiks)
