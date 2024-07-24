def check_network():
    return True


def check_download_url():
    return True


def check_access_allowed():
    return True


def check_dns():
    return True


def download_file():
    if not check_network():
        raise ConnectionResetError("Cannot connect to network")
    if not check_download_url():
        raise ValueError("Invalid URL")
    if not check_access_allowed():
        raise PermissionError("Cannot access resource (permission denied)")
    if not check_dns():
        raise ConnectionError("No DNS")

    return ['c', 'o', 'o', 'l']
