import requests
import sys
import json


def waybackurls(host, with_subs):
    url = 'http://web.archive.org/cdx/search/cdx?url={protocol}://{sub}.{host}/*&output=json&fl=original&collapse=urlkey'.format(
        protocol='*' if with_subs else 'http',
        sub='*' if with_subs else '',
        host=host
    )
    r = requests.get(url)
    results = r.json()
    return results[1:]


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage:\n\tpython3 waybackurl.py <url> <include_subdomains:optional>')
        sys.exit()

    host = sys.argv[1]
    with_subs = False
    if len(sys.argv) > 2:
        with_subs = bool(sys.argv[2])

    urls = waybackurls(host, with_subs)
    if urls:
        filename = f'{host}-waybackurls.json'
        with open(filename, 'w') as f:
            json.dump(urls, f)
        print(f'[*] Saved results to {filename}')
    else:
        print('[-] Found nothing')
