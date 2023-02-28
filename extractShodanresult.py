import shodan

api = shodan.Shodan("<apikey>")

try:
    results = api.search("<search>", offset=0)
    total_results = results['total']
    print("Total résultats: {}".format(total_results))

    with open("results.txt", "a") as f:
        for i in range(0, total_results, 100):
            results = api.search("<search>", offset=i, limit=100)

            for result in results['matches']:
                ip_and_ports = result['ip_str']
                print(ip_and_ports)
                f.write(ip_and_ports + "\n")

except shodan.APIError as e:
    print("Erreur de l'API: {}".format(e))
