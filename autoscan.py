import subprocess
import subprocess

def run_command(command):
    try:
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            print(f"Erreur lors de l'exécution de la commande '{command}': {stderr.strip()}")
            return ""
        return stdout.strip()
    except Exception as e:
        print(f"Une erreur est survenue lors de l'exécution de la commande '{command}': {e}")
        return ""

def run_sqlmap(url):
    sqlmap_command = f"./sqlmap-dev/sqlmap.py -u {url} --crawl=3 --level=3 --risk=2 --batch"
    return run_command(sqlmap_command)

def run_xsstrike(url):
    xsstrike_command = f"./XSStrike/xsstrike.py -u {url}"
    return run_command(xsstrike_command)

def run_nuclei(url):
    nuclei_command = f"nuclei -u {url}"
    return run_command(nuclei_command)

def run_katana(url):
    katana_command = f"katana -u {url}"
    return run_command(katana_command)
def run_js_crawl(url):
    return "Résultats du crawl de fichier JS ici."

def run_config_error_scan(url):
    return "Résultats de la vérification des erreurs de configuration ici."

def scan(choice, url):
    output = ""  # définissez une valeur par défaut pour output
    if choice == '1':
        print("Recherche des vulnérabilités SQLi...")
        output = run_sqlmap(url)
    elif choice == '2':
        print("Recherche des vulnérabilités XSS...")
        output = run_xsstrike(url)
    elif choice == '3':
        print("Extraction de paramètres avec Katana...")
        output = run_katana(url)
    elif choice == '4':
        print("Crawl de fichiers JS...")
        output = run_js_crawl(url)
    elif choice == '5':
        print("Recherche d'erreurs de configuration...")
        output = run_config_error_scan(url)
    elif choice == '6':
        print("Lancement des scans automatiques")
        output = run_nuclei(url)
    else:
        print("Merci de choisir un nombre entre 1 et 6")
        return exit()

    return output

def main():
    print("Menu principal:")
    print("1: SQLi")
    print("2: XSS")
    print("3: Extraction de paramètres")
    print("4: Crawl de fichiers JS")
    print("5: Erreurs de configuration")
    print("6: Scan global")
    choice = input("Entrez le numéro du scan que vous voulez effectuer: ")
    url = input("Entrez l'URL à tester: ")
    output = scan(choice, url)

    print("Résultats du scan:")
    print(output)

if __name__ == "__main__":
    main()
